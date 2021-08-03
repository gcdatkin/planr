#!/bin/bash

docker rm planr-webapp
docker run -it -p 5000:5000 --name planr-webapp planr/webapp serve -s /home/node/build
