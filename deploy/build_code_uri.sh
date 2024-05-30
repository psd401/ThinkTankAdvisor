#!/bin/bash

rm -rf ./code_uri
mkdir code_uri
cd code_uri && mkdir aichatcore/ && cd ..

cp -r ../aichatcore/. ./code_uri/aichatcore
cp -r ../server/. ./code_uri/server

poetry export --without-hashes -f requirements.txt --output requirements.txt
mv requirements.txt ./code_uri/
