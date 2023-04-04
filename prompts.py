import os

PROMPT_DIRECTORY = "./prompts/"


def get_file_content(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


def load_prompt(prompt_type: str, prompt_name: str) -> str:
    file_path = os.path.join(PROMPT_DIRECTORY, f"{prompt_type}.txt")
    file_content = get_file_content(file_path)

    start_tag = f"<<<{prompt_name}>>>"
    end_tag = "<<<"

    start_index = file_content.find(start_tag)
    if start_index == -1:
        raise ValueError(f"Prompt '{prompt_name}' not found in '{file_path}'")

    end_index = file_content.find(end_tag, start_index + len(start_tag))
    if end_index == -1:
        end_index = len(file_content)

    prompt_content = file_content[start_index +
                                  len(start_tag):end_index].strip()
    return prompt_content


if __name__ == "__main__":
    prompt_type = "system"
    prompt_name = "default"
    prompt = load_prompt(prompt_type, prompt_name)
    print(prompt)
