import pulumi_aws as aws
import pulumi

config = pulumi.Config()
app_name = config.require('app_name')
env = config.require('environment')

def mkItemName(name: str) -> str:
   return (app_name+"-"+env+"-"+name)[0:52]

awsProvider: aws.Provider = aws.Provider(resource_name="aws", opts=None)