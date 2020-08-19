#!/bin/env sh
#ln -s to s3-pre-sign-url.py first and set env variables accordingly
#create pre-signed url valid for 1 day: 0 hours : 0 minutes : 0 seconds

./s3-pre-sign-url.py -a $CEPH_ACCESS_KEY -s $CEPH_SECRET -e $CEPH_URL -t 1:0:0:0