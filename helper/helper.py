from openai import OpenAI
import random
from typing import Dict, Any
import json
import re

from openai import OpenAI
import helper.creden as cre
client = OpenAI(api_key=cre.OPENAI_API_KEY)

def get_completion_from_messages(messages, model, temperature=0, max_tokens_values = 100):
    """get the message from openai api"""
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens_values,
    )
    return response.choices[0].message.content


def select_random_topics(topics, num_topics=5):
    selected_topics = random.sample(topics, num_topics)
    return selected_topics


def select_random_test(json_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extracts a random example from the data that's in JSON format.
    """
    if len(json_data["topics"]) == 0:
        raise ValueError("The 'topics' list is empty.")
    
    random_number = random.randint(0, len(json_data["topics"]) - 1)
    return json_data["topics"][random_number]


def parse_conversation(text):
    """Convert the text into json from the full conversation"""

    messages = text.split('\n')

    # Initialize conversation list
    conversation = []
    current_message = None
    current_content = []

    for line in messages:
        # Skip empty lines
        if not line.strip():
            continue

        # Check if line starts with 'assistant:' or 'user:'
        if line.startswith(('assistant:', 'user:')):
            # If we have a previous message, add it to conversation
            if current_message is not None:
                conversation.append({
                    'role': current_message,
                    'content': '\n'.join(current_content).strip()
                })

            # Start new message
            current_message = line.split(':')[0].strip()
            current_content = [':'.join(line.split(':')[1:]).strip()]
        else:
            # Continue adding content to current message
            if current_message is not None:
                current_content.append(line)

    # Add the last message
    if current_message is not None:
        conversation.append({
            'role': current_message,
            'content': '\n'.join(current_content).strip()
        })

    # Extract results if they exist
    results = {}
    results_pattern = r'"results":\s*{([^}]+)}'
    results_match = re.search(results_pattern, text)
    if results_match:
        results_text = "{" + results_match.group(1) + "}"
        try:
            results = json.loads(results_text)
        except json.JSONDecodeError:
            pass

    # Create final JSON structure
    json_output = {
        "conversation": conversation,
        "metadata": {
            "interview_topic": "Delivery Route Optimization",
            "interview_results": results.get("results", {})
        }
    }

    return json_output
