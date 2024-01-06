import json
import random


def load_intents(file_path):
    # Load intents from a JSON file
    with open(file_path, 'r') as file:
        intents = json.load(file)
    return intents['intents']


def get_intents_by_pattern(intents, message):
    # Find all intents that match the user input
    matching_intents = []
    for intent in intents:
        for pattern in intent['patterns']:
            if pattern.lower() in message.lower():
                matching_intents.append(intent)
                break  # Once a match is found, move to the next intent
    return matching_intents


def get_responses(matching_intents):
    # Accumulate all responses from matching intents
    all_responses = []
    for intent in matching_intents:
        all_responses.extend(intent['responses'])
    return all_responses


def eliza_chatbot(intents_file):
    # Introduction
    print("Eliza: Hello! I'm Eliza, your psychotherapist chatbot. Type 'exit' to end the conversation.")

    # Load intents from the provided file
    intents = load_intents(intents_file)

    while True:
        # User input
        user_input = input("You: ")

        # Check for exit command
        if user_input.lower() == 'exit':
            print("Eliza: Goodbye! Take care of yourself.")
            break

        # Find all matching intents
        matching_intents = get_intents_by_pattern(intents, user_input)
        if matching_intents:
            # Get all responses from matching intents
            all_responses = get_responses(matching_intents)

            # Randomly select a response from all responses
            response = random.choice(all_responses)
            print(f"Eliza: {response}")
        else:
            # If no intent matches, provide a generic response
            print("Eliza: I'm here to listen. Can you tell me more about that?")


if __name__ == "__main__":
    # Replace with the actual path to your intents JSON file
    intents_file_path = 'intents.json'
    eliza_chatbot(intents_file_path)
