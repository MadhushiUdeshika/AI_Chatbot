import json


def convert_json_to_nlu_md(json_file, output_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    with open(output_file, 'w') as md_file:
        for intent_data in data.get('intents', []):
            tag = intent_data.get('tag', '')
            patterns = intent_data.get('patterns', [])

            md_file.write(f"## intent:{tag}\n")
            for pattern in patterns:
                md_file.write(f"- {pattern}\n")


if __name__ == "__main__":
    json_file_path = 'intents.json'  # Replace with the actual path to your JSON file
    nlu_md_output_path = 'data/nlu.md'  # Replace with the desired output path for the NLU Markdown file

    convert_json_to_nlu_md('intents.json', 'data/nlu.md')
