import numpy as np
import pandas as pd
import requests

def get_access_token(client_id, client_secret):
    url = 'https://accounts.spotify.com/api/token'
    
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    
    request = requests.post(url=url, data=data)
    
    return request.json()['access_token']

def get_results(url, access_token):
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    request = requests.get(url=url, headers=headers)
    
    return request.json()

def get_releases(query, n, release_type, year, access_token):
    
    # Initialize DataFrame for result storage
    releases = pd.DataFrame(columns=['track_id', 'album_id', 'type', 'name', 'artists', 'popularity'])

    # Max limit is 50 so we need to offset if n > 50
    for i in range((n // 50) + 1):
        
        # Get 50 results unless we are on the last iteration
        limit = (n % 50) if (i == (n // 50)) else 50
        
        # If n is divisible by 50, don't include the last iteration
        if limit == 0:
            break
        
        # Define URL for getting search results
        url = "https://api.spotify.com/v1/search?q=" + query\
            + "%20year:" + str(year)\
            + "&type=" + str(release_type)\
            + "&limit=" + str(limit)\
            + "&offset=" + str(i * 50)
        
        
        # Get results
        results = get_results(url, access_token)[release_type + 's']['items']
        
        # Store results in releases DataFrame
        for result in results:
            
            result_dict = {
                'track_id':   result['id'],
                'album_id':   result['album']['id'],
                'type':       result['type'],
                'name':       result['name'],
                'artists':    result['artists'],
                'popularity': result['popularity']
            }
            
            releases = releases.append(result_dict, ignore_index=True)
    
    # Process artists data
    releases['artist_names'] = releases['artists'].apply(lambda artist_list: list(map(lambda artist_dict: artist_dict['name'], artist_list)))
    releases['artist_ids'] = releases['artists'].apply(lambda artist_list: list(map(lambda artist_dict: artist_dict['id'], artist_list)))
    releases = releases.drop('artists', axis=1)
    
    return releases
            
def filter_on_track_popularity(df, popularity_threshold=5):
    df = df.copy()
    df = df.query("popularity <= @popularity_threshold")
    return df
    
def get_label(album_id, access_token):
    # Get the label associated with the album
    album_url = f"https://api.spotify.com/v1/albums/{album_id}"
    label = get_results(album_url, access_token)['label']
    
    return label
    
def add_record_labels(df, access_token):
    # Add album_id and record_label columns to the DataFrame
    df = df.copy()
    df['record_label'] = df['album_id'].apply(lambda x: get_label(x, access_token))
    
    return df
    
def get_artist_by_id(artist_id, access_token):
    results = get_results(url=f"https://api.spotify.com/v1/artists/{artist_id}", access_token=access_token)
    artist_name = results['name']
    artist_followers = np.int(results['followers']['total'])
    artist_popularity = np.int(results['popularity'])
    return pd.Series([artist_id, artist_name, artist_followers, artist_popularity], index=["artist_id", "artist_name", "artist_followers", "artist_popularity"])

def coerce_scan_types(x):
    if 'N' in x.keys():
        x_float = np.float(x['N'])
        if x_float.is_integer():
            return np.int(x_float)
        else:
            return x_float
    elif 'S' in x.keys():
        return x['S']
    else:
        return x