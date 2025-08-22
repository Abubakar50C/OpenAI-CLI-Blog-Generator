import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Write a paragraph about the following topic: {paragraph_topic}',
        max_tokens=400,
        temperature=0.3
    )
    return response.choices[0].text.strip()

keep_writing = True
