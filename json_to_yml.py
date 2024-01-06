import json


def convert_json_to_yml(json_path, yml_path):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

    yml_content = ""
    for intent_data in data.get('intents', []):
        tag = intent_data.get('tag', '')
        patterns = intent_data.get('patterns', [])
        responses = intent_data.get('responses', [])

        yml_content += f'intents:\n  - {tag}\nresponses:\n  utter_{tag}:\n'
        yml_content += '\n'.join([f'    - "{response}"' for response in responses]) + '\n\n'

    with open(yml_path, 'w') as yml_file:
        yml_file.write(yml_content)


if __name__ == "__main__":
    json_file_path = 'intents.json'  # Replace with the actual path to your JSON file
    yml_file_path = 'domain.yml'  # Replace with the desired output path for the domain.yml file

    convert_json_to_yml(json_file_path, yml_file_path)
