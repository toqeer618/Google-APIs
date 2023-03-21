'''
    google cloud translation: we first to create services account for api then download the json
    
'''
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

# create a credentials object
credentials = service_account.Credentials.from_service_account_file('json from services account')

# create a client object
translate_client = translate.Client(credentials=credentials)

# the text to translate
text = 'incomplete'

# the target language
target = 'ur'

# translate the text
result = translate_client.translate(text, target_language=target)

# print the result
print(result['input'])
print(result['translatedText'])
