import os

def is_blank(s):
    return bool(not s or s.isspace())

def setEnv():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f"resource/g-translation-dev.json"
    os.environ['project_id'] = "g-translation-dev"

def setEnvLocal():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f"src/lambda/translate/resource/g-translation-dev.json"
    os.environ['project_id'] = "g-translation-dev"