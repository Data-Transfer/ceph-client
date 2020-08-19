#!/bin/env sh
./s3-rest.py -c $1 -b $2 -k $3 -m post -t"uploads=" -X .//aws:UploadId