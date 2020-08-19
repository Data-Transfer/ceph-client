#!/bin/env sh
echo $6
./s3-rest.py  -m put -b $2 -k $3 \
           -c $1 -p $4 -f \
           -t "partNumber=$5;uploadId=$6" -H "ETag"