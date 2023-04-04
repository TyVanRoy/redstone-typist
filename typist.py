# typist.py
import sys
import parse_src
import context_builder
import request_builder
import openai_api
import insert_response


def main(src_path):
    file_path, tag = parse_src.parse_src(src_path)
    context = context_builder.build_context(file_path)
    request = request_builder.build_request(tag, context)
    response = openai_api.get_response(request)
    print(response)
    insert_response.insert_response(file_path, tag, response)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python typist.py <path_to_project>")
        sys.exit(1)

    src_path = sys.argv[1]
    main(src_path)
