def validate_output(response: str):

    if not response:
        return "I couldn't generate a response."

    return response