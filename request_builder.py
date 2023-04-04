# request_builder.py
import prompts
from constants import *


def build_request(tag, context):
    prompt = prompts.load_prompt("tags", tag)
    return f"{prompt}\n{context}"


if __name__ == "__main__":
    tag = NEW_TAG
    context = "<context_here>"
    request = build_request(tag, context)
    print(request)
