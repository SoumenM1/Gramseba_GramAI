import json


def safe_json_loads(value: str):

    try:
        return json.loads(value)

    except json.JSONDecodeError:
        return None