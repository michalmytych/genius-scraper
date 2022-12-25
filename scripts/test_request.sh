#!/bin/zsh

if [ -z "$1" ]
  then
    echo "You should provide song ID as script parameter: test_request.sh ID"
    exit -1
fi

curl -XGET -H 'X-Api-Key: 30b3413b-092a-49a6-abd2-3d965a0ad0c0' "http://127.0.0.1:5000/scrape?song_id=$1"
