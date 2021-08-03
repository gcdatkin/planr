#!/bin/bash

cd ../..
docker build -t planr/webapp:latest -f deploy/Dockerfile .