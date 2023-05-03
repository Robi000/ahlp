#!/bin/bash
# Content Length
curl -sI "$1" | grep -Fi Content-Length |  awk -v FS=": " '/^Content-Length/{print $2}' 
