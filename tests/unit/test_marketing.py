from app.ai.marketing.validators import validate_marketing_output


def test_marketing_validator():

    data = {
        "title": "Fresh Mango",
        "description": "Fresh mangoes",
        "short_description": "Fresh mangoes",
        "hashtags": ["#mango"],
    }

    assert validate_marketing_output(data)