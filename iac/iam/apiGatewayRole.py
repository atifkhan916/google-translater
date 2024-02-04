import pulumi
import pulumi_aws as aws
from util.util import * 
import json

apigatewayRole = aws.iam.Role(
    mkItemName("apigateway-iam-role"), 
    assume_role_policy=json.dumps({
      "Version": "2012-10-17",
      "Statement": [{
          "Action": "sts:AssumeRole",
          "Effect": "Allow",
          "Sid": "",
          "Principal": {
              "Service": "apigateway.amazonaws.com",
          },
       }]
    })
)

apigatewayRolePolicy = aws.iam.RolePolicy(
  mkItemName("apigateway-role-policy"),
  role= apigatewayRole.id,
  policy= json.dumps({
      "Version": "2012-10-17",
      "Statement": [
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
        }
      ],
    })
)
