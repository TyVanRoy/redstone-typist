import re


def extract_imports(file_content):
    import_re = re.compile(r'#\s*\$\$\$IMPORT:\s*(.+)')
    imports = import_re.findall(file_content)
    return imports


def build_context(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()

    imports = extract_imports(file_content)
    context = '\n'.join(imports) + '\n' + file_content
    return context


if __name__ == "__main__":
    file_path = "<path_to_target_file>"
    context = build_context(file_path)
    print(context)
