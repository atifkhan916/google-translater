#!/bin/bash
set -eo pipefail
export PYTHONDONTWRITEBYTECODE=1
rm -rf package
rm -rf translation_lambda.zip
pip3 install --target package -r requirements.txt
cd package
7z a -tzip ../translation_lambda.zip *
cd ../src/lambda/translate
7z a -tzip ../../../translation_lambda.zip *
cd ../../..
