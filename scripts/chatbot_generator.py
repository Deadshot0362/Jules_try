def generate_chatbot_from_text(text):
    """
    Generates a simple keyword-matching chatbot from the given text.
    """
    # This is a very simple implementation.
    # It just creates a dictionary where the keys are the first words of each line
    # and the values are the full lines.
    lines = text.strip().split('\n')
    chatbot_dict = {}
    for line in lines:
        if not line:
            continue
        words = line.split()
        if len(words) > 0:
            chatbot_dict[words[0].lower()] = line
    return chatbot_dict
