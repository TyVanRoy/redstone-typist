import argparse
import os
import time
from create_outline import create_outline
from openai_api import generate_response


def create_new_module(requirements_file, source_code_file, output_file=None):
    # Create temporary file for the outline
    temp_outline_file = "temp_outline.txt"
    create_outline(source_code_file, temp_outline_file)

    # Load the operational mode prompt
    with open("operation_mode_prompt.txt", "r") as file:
        operation_mode_prompt = file.read()

    # Load the design requirements
    with open(requirements_file, "r") as file:
        design_requirements = file.read()

    # Combine the prompt, outline, and design requirements
    with open(temp_outline_file, "r") as file:
        outline_content = file.read()

    full_prompt = "{}\n\n{}\n\n{}".format(
        operation_mode_prompt, outline_content, design_requirements)

    # Generate the code using the OpenAI API
    response = generate_response(full_prompt)

    # Save the response to the output file
    if not output_file:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        output_file = f"gpt_response_{timestamp}.txt"

    with open(output_file, "w") as file:
        file.write(response)

    # Remove the temporary outline file
    os.remove(temp_outline_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate code modules using GPT-4")
    parser.add_argument("mode", help="Operational mode ('new')")
    parser.add_argument(
        "requirements", help="Path to the design requirements file")
    parser.add_argument("source_code", help="Path to the source code file")
    parser.add_argument(
        "-o", "--output", help="Path to the output file", default=None)

    args = parser.parse_args()

    if args.mode == "new":
        create_new_module(args.requirements, args.source_code, args.output)
    else:
        print("Invalid operational mode. Please use 'new'.")
