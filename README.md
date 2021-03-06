# planr
Emerging artist detector for online streaming platforms  
  
***
  
## Instructions for setting up on AWS

1. Copy your AWS Access Key ID and Secret Access Key into lambda_function.py.
2. Create a new S3 bucket called planr744 (if you change this name just be sure to change it in lambda_function.py).
3. Add excluded_labels.txt to the bucket.
4. Create a new DynamoDB table called ArtistTracker (if you change this name just be sure to change it in lambda_function.py). Set the primary key to artist_id (String) and the sort key to artist_followers (Number).
5. Create a new Lambda layer to enable pandas on Lambda (I usually call this python-pandas) using the python-pandas.zip file with a Python 3.7 runtime.
6. Create a new Lambda function called Crawler (you can change this name if you wish).
7. Replace the default lambda_function.py with the one provided. Also add helper_functions.py as a separate file.
8. Add the python-pandas Lambda layer to the Crawler function under the Code tab.
9. Change the function timeout under the Configuration tab.
10. Go to CloudWatch and click on the Rules tab on the left (under Events).
11. Create a new rule and select Schedule. Add Crawler as the target and set the schedule to a fixed rate of 1 minute.
12. The ArtistTracker should now be populated every minute with new artists.


## [Optional] Instructions for using ACloudGuru's AWS Playgrounds

1. Log in to https://acloudguru.com and click Playground.
2. Launch a new AWS Sandbox instance.
3. Open the AWS environment in incognito and sign in using the Username and Password provided.
