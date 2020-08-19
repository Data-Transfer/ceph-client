#!/bin/env sh
if [ $# -eq 0 ]; then
    echo "usage: $0 <json configuration file> <bucket name>"
    exit 1
fi
./_check_env.sh
CMDLINE="./s3-rest.py -c $1 -m delete -b $2 -k $3 -l DEBUG"
echo "deleting $2/$3 object"
echo "$CMDLINE"
sleep 2
$CMDLINE
