import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Write a paragraph about the following topic: {paragraph_topic}"}
        ],
        temperature=0.3,
        max_tokens=400
    )
    return response.choices[0].message.content.strip()

keep_writing = True

while keep_writing:
    answer = input('Write a paragraph? Y for yes, anything else for no: ').strip().upper()
    if answer == 'Y':
        paragraph_topic = input('What should this paragraph talk about? ').strip()
        print(generate_blog(paragraph_topic))
    else:
        "Thank you for using the OpenAI CLI Blog Generator! Bye."
        keep_writing = False
