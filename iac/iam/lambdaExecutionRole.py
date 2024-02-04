import pulumi
import pulumi_aws as aws
from util.util import * 
import json

lambdaExecutionRole = aws.iam.Role(
    resource_name=mkItemName("lambda-execution-role"), 
    assume_role_policy=json.dumps({
      "Version": "2012-10-17",
      "Statement": [{
          "Action": "sts:AssumeRole",
          "Effect": "Allow",
          "Sid": "",
          "Principal": {
              "Service": "lambda.amazonaws.com",
          },
       }]
    })
)

lambdaExecutionPolicy = aws.iam.RolePolicy(
  mkItemName("lambda-execution-role-policy"),
  role= lambdaExecutionRole.id,
  policy= json.dumps({
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "AllowLambdaFunctionInvocation",
          "Effect": "Allow",
          "Action": ["lambda:InvokeFunction", "lambda:InvokeAsync"],
          "Resource": ["*"],
        },
        {
          "Sid": "AllowWsManagementInvocation",
          "Effect": "Allow",
          "Action": ["execute-api:Invoke", "execute-api:ManageConnections"],
          "Resource": ["arn:aws:execute-api:*:*:*/*"],
        },
        {
          "Sid": "Logs",
          "Effect": "Allow",
          "Action": [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:DescribeLogGroups",
            "logs:DescribeLogStreams",
            "logs:PutLogEvents",
            "logs:GetLogEvents",
            "logs:FilterLogEvents",
          ],
          "Resource": "arn:aws:logs:*:*:*",
        },
        
        {
          "Sid": "AllowAssumeRole",
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Resource": "*",
        }
      ],
    })
);

aws.iam.RolePolicyAttachment(
  mkItemName('lambdaBasicExecPolicyAtch'),
  role= lambdaExecutionRole,
  policy_arn= aws.iam.ManagedPolicy.AWS_LAMBDA_BASIC_EXECUTION_ROLE
)

# allow services to execute this lambda
aws.iam.RolePolicyAttachment(
  mkItemName("lambdaExecPolicyAtch"),
  role= lambdaExecutionRole,
  policy_arn= aws.iam.ManagedPolicy.AWS_LAMBDA_EXECUTE
)



lambdaExecutionRoleArn = lambdaExecutionRole.arn;
lambdaExecutionPolicyName = lambdaExecutionRole.name;
