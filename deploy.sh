#!/bin/bash
set -eo pipefail
./build-layer.sh
cd iac
pip3 list
echo "STARTING PULUMI BUILD"
rm -rf package
pip3 install -r requirements.txt
cd ..
#Pulumi variables
AWS_REGION=ap-south-1
APP_NAME=text-translator
ENV=dev
STACK=$APP_NAME-$ENV
API_VERSION=v1
export PULUMI_CONFIG_PASSPHRASE=seCRetPassPhrase
#Pulumi config
pulumi stack select $STACK -c --cwd iac
pulumi config --stack $STACK --cwd iac set-all  --non-interactive --plaintext environment=$ENV --plaintext aws_region=$AWS_REGION --plaintext rest_api_stage=$ENV --plaintext app_name=$APP_NAME --plaintext api_version=$API_VERSION 
pulumi config set env $ENV --cwd iac
pulumi config set aws:region $AWS_REGION --cwd iac
pulumi plugin install resource aws v6.0.4

#Pulumi commands
#pulumi cancel -y --cwd iac
pulumi refresh -y --cwd iac
pulumi preview --cwd iac
pulumi up -y --cwd iac

#ARTIFACT_BUCKET=$(cat bucket-name.txt)
#aws cloudformation package --template-file template.yml --s3-bucket $ARTIFACT_BUCKET --output-template-file out.yml
#aws cloudformation deploy --template-file out.yml --stack-name blank-python --capabilities CAPABILITY_NAMED_IAM