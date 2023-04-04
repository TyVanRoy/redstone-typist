import openai
import prompts
from env import *

openai.api_key = OPENAI_API_KEY


def get_response_from_messages(messages, model="gpt-4", tokens=256, temperature=0.8):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages[0],
        max_tokens=tokens,
        temperature=temperature,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    message = response.choices[0].message.content
    return message.strip()


def get_response(prompt, system_prompt=None, model="gpt-4", tokens=256, temperature=0.8):
    if system_prompt is None:
        system_prompt = prompts.load_prompt("system", "default")
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ],
    return get_response_from_messages(messages, model, tokens, temperature)


if __name__ == "__main__":
    user_prompt = "Write a function to reverse a string in Python."
    result = get_response(user_prompt)
    print(result)
