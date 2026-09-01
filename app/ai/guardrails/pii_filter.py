import re


EMAIL_PATTERN = r"\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b"


def remove_email(text: str):

    return re.sub(
        EMAIL_PATTERN,
        "[REDACTED_EMAIL]",
        text,
    )