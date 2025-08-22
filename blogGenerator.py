import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['API_KEY']