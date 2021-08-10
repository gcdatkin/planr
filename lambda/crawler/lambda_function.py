import json
import boto3
import numpy as np
import pandas as pd
import random

from helper_functions import *

def lambda_handler(event, context):
    
    # Important information
    AWS_ACCESS_KEY_ID = 'AKIAT2U3KSJOEV3AYSGB'
    AWS_SECRET_ACCESS_KEY = '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'

    SPOTIFY_CLIENT_ID = '184eaab7c86845eeaa6f779f47d37ce0'
    SPOTIFY_CLIENT_SECRET = 'c9c02ad8cfa941c78eb99e03faeb5458'
    SPOTIFY_ACCESS_TOKEN = get_access_token(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
    
    EXCLUDED_LABELS_BUCKET = 'planr749'
    EXCLUDED_LABELS_FILE = 'excluded_labels.txt'

    # AWS Session
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name='us-east-1'
    )

    # S3 Client
    s3_client = session.client('s3')

    # Get excluded labels
    excluded_labels = session.client('s3').get_object(
        Bucket=EXCLUDED_LABELS_BUCKET,
        Key=EXCLUDED_LABELS_FILE
    )['Body'].read().decode('utf-8').splitlines()

    # Define query
    query = chr(random.randint(97, 122))

    # Get new releases
    release_df = get_releases(query=query, n=20, release_type='track', year=2021, access_token=SPOTIFY_ACCESS_TOKEN)
    release_df = filter_on_track_popularity(release_df)
    release_df = add_record_labels(release_df, SPOTIFY_ACCESS_TOKEN)
    release_df = release_df.query("record_label not in @excluded_labels")
    
    # Get artists from releases
    unique_artists = list(release_df['artist_ids'].explode().unique())
    artist_df = pd.DataFrame(columns=["artist_id", "artist_name", "artist_followers", "artist_popularity"])
    for artist_id in unique_artists:
        artist_series = get_artist_by_id(artist_id=artist_id, access_token=SPOTIFY_ACCESS_TOKEN)
        artist_df = artist_df.append(artist_series.T, ignore_index=True)
    
    # DynamoDB Client
    db_client = session.client('dynamodb')
    
    # Add artists to ArtistTracker
    for artist_info in artist_df.to_dict(orient='records'):
        db_client.put_item(
            TableName='ArtistTracker',
            Item={
                'artist_id': {
                    'S': str(artist_info['artist_id'])
                },
                'artist_name': {
                    'S': str(artist_info['artist_name'])
                },
                'artist_followers': {
                    'N': str(artist_info['artist_followers'])
                },
                'artist_popularity': {
                    'N': str(artist_info['artist_popularity'])
                }
            }
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('SUCCESS')
    }