import os
import json
from translate import *

setEnv()

def handler(event, context):
    print('## ENVIRONMENT VARIABLES\r' + json.dumps(dict(**os.environ)))
    print('## EVENT\r' + json.dumps(event))
    print('## EVENT BODY\r' + event["body"])
    requestBody = json.loads(event["body"])
    translated_text = translate_text(requestBody["text"])
    
    return {
        'statusCode': 200,
        'body': translated_text
    }
