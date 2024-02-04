import pulumi
import pulumi_aws as aws
from util.util import * 
from iam.lambdaExecutionRole import *

translation_lambda = aws.lambda_.Function(mkItemName("translation-lambda"),
    runtime="python3.12",
    handler="app.handler",
    timeout= 60,
    environment= {
    },
    role=lambdaExecutionRole.arn,
    memory_size= 512,
    code=pulumi.FileArchive("../translation_lambda.zip")
)