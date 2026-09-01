def validate_marketing_output(data: dict):

    required = [
        "title",
        "description",
        "short_description",
        "hashtags",
    ]

    for field in required:
        if field not in data:
            return False

    return True