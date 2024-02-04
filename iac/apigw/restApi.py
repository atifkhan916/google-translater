import pulumi
import pulumi_aws as aws
import pulumi_aws_apigateway as apigateway
from util.util import *
from .responses import *
from lambdas.translationLambda import translation_lambda
from iam.apiGatewayRole import apigatewayRole
from typing import Optional

apiName = 'rest-api'

config = pulumi.Config()
restApiStage = config.require('rest_api_stage')
restApiVersion = config.require('api_version')

routes: Optional[apigateway.RouteArgs] = [
    apigateway.RouteArgs(
        path="/"+restApiVersion+"/translate", 
        method=apigateway.Method.POST, 
        event_handler=translation_lambda
    )
]

apisAccount = aws.apigateway.Account(mkItemName("apigateway-account"),
  cloudwatch_role_arn= apigatewayRole.arn
)

restAPI = apigateway.RestAPI(
    mkItemName('translation-rest-api'),
    routes= routes,
    stage_name= restApiStage,
    gateway_responses= gatewayResponses,
    binary_media_types= [
      'image/png',
      'image/jpeg',
      'multipart/form-data',
      'application/pdf'
    ]
)

#pulumi.export("endpoint_url", stage.invoke_url)
pulumi.export("url", restAPI.url)