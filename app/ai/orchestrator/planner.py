class Planner:

    async def create_plan(self, message: str):

        message_lower = message.lower()

        if any(
            word in message_lower
            for word in [
                "marketing",
                "title",
                "description",
                "advertisement",
            ]
        ):
            return {
                "type": "marketing",
                "requires_database": True,
            }

        if any(
            word in message_lower
            for word in [
                "seller",
                "shop",
                "business",
            ]
        ):
            return {
                "type": "seller_search",
                "requires_database": True,
            }

        return {
            "type": "general_chat",
            "requires_database": False,
        }