from app.core.constants import MAX_MESSAGE_LENGTH


def validate_input(message: str):

    if not message:
        raise ValueError("Message cannot be empty")

    if len(message) > MAX_MESSAGE_LENGTH:
        raise ValueError(
            "Message exceeds maximum length"
        )

    return True