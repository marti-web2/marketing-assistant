import os
from urllib import response
import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-PlcGDYYTaKojRnkjiV6mhfTj"
openai.api_key = os.getenv('OPEN_API_KEY')
subject="coffee"
prompt = f"Generate upbeat branding snippet for {subject}"
response = openai.Completion.create(engine="davinci-instruct-beta-v3", prompt=prompt, max_tokens=32)
print(response)