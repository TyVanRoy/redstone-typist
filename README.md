# redstone-typist
Redstone Typist is a powerful AI-assisted code generation and modification tool powered by GPT-4. It helps you draft and edit code faster and more efficiently by leveraging GPT-4's extensive knowledge of programming languages and best practices.

## Features
- Supports new code generation with the **`$$$new`** tag
- Allows editing existing code with the **`$$$edit`** and **`$$$end`** tags
- Handles import statements with the **'$$$IMPORT`** tag
- Provides a simple interface to integrate with the OpenAI API

## Installation
1. Clone the repository:

        git clone https://github.com/yourusername/redstone-typist.git

2. Navigate to the project directory:

        cd redstone-typist

3. Install the required packages:

Copy code
pip install -r requirements.txt
Set up your OpenAI API key as an environment variable:

        export OPENAI_API_KEY="your-api-key"

## Usage
Redstone Typist is designed to be easy to use in your day-to-day development. To get started, simply add the appropriate tags to your code:

1. Add the $$$new tag where you want Redstone Typist to generate new code.

2. Use the $$$edit and $$$end tags to mark the beginning and end of a code block that you want Redstone Typist to edit.

3. If your code requires imports from other files, add the $$$IMPORT tag followed by the file path:

        // $$$IMPORT: path/to/your/file.ts

4. Run Redstone Typist on your project:

        python typist.py path/to/your/project

5. Review the output and integrate the suggestions into your code as needed.

Redstone Typist makes it easy to get AI-generated code suggestions and improve your development process. Happy coding!
