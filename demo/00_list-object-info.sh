#!/bin/env sh
if [ $# -eq 0 ]; then
    echo "usage: $0 <json configuration file> <bucket name>"
    exit 1
fi
. ./_check_env.sh
CMDLINE="./s3-rest.py -c $1 -m head -b $2 -k $3"
echo "list information for object $2/$3"
echo "$CMDLINE"
sleep 2
$CMDLINE
