#!/bin/bash

export AWS_REGION=us-east-1
export PLANR_BUCKET=planr749

# Create execution role
aws iam create-role --role-name lambda-ex --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

# Save role info
aws iam get-role --role-name lambda-ex > lambda-exec.json &&
    LAMBDA_ROLE_ARN=$(grep -oP '(?<="Arn": ")[^"]*' lambda-exec.json) &&
    rm lambda-exec.json

# Create S3 bucket
aws s3api create-bucket --bucket $PLANR_BUCKET

# Add files to bucket
aws s3 cp ../../s3/excluded_labels.txt s3://$PLANR_BUCKET

# Create ArtistTracker DynamoDB table
aws dynamodb create-table --table-name ArtistTracker --attribute-definitions AttributeName=artist_id,AttributeType=S AttributeName=artist_followers,AttributeType=N --key-schema AttributeName=artist_id,KeyType=HASH AttributeName=artist_followers,KeyType=RANGE --billing-mode PAY_PER_REQUEST

# Create Lambda Layer
aws lambda publish-layer-version --layer-name python37-pandas --description "Python 3.7 with pandas installed" --compatible-runtimes="python3.7" --zip-file fileb://../../lambda/layers/python37-pandas.zip

# Save layer info
aws lambda get-layer-version --layer-name python37-pandas --version-number 1 > python37-pandas.json &&
    LAMBDA_LAYER_ARN=$(grep -oP '(?<="LayerVersionArn": ")[^"]*' python37-pandas.json) &&
    rm python37-pandas.json

# Create Crawler Lambda function
aws lambda create-function --function-name Crawler --runtime python3.7 --role $LAMBDA_ROLE_ARN --handler lambda_function.lambda_handler --zip-file fileb://../../lambda/crawler.zip

# Save function info
aws lambda get-function --function-name Crawler > crawler.json &&
    CRAWLER_ARN=$(grep -oP '(?<="FunctionArn": ")[^"]*' crawler.json) &&
    rm crawler.json

# Add layer to function
aws lambda update-function-configuration --function-name Crawler --layers $LAMBDA_LAYER_ARN --timeout 30

