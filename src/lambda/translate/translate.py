from google.cloud import translate_v2 as translate
from utils import *

def translate_text(text: str, target = "da") -> dict:
    if is_blank(text):
        return ''
        
    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result["translatedText"]


def main():
    setEnvLocal()
    print(translate_text('good bye honey'))
    
if __name__ == "__main__":
    main()