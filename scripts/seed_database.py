import asyncio

from app.database.mongodb import get_database


async def seed():

    db = get_database()

    await db.sellers.delete_many({})
    await db.products.delete_many({})

    sellers = [
        {
            "_id": "seller_001",
            "name": "Rahul",
            "business_name": "Rahul Fresh Vegetables",
            "category": "Vegetables",
        },
        {
            "_id": "seller_002",
            "name": "Amit",
            "business_name": "Amit Grocery Store",
            "category": "Grocery",
        },
    ]

    await db.sellers.insert_many(sellers)

    print("Database seeded successfully.")


if __name__ == "__main__":
    asyncio.run(seed())