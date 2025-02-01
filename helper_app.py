import random

def select_random_topics(topics, num_topics=5):
    """Select random topics."""
    selected_topics = random.sample(topics, num_topics)
    return selected_topics


