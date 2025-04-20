from database.mongo import users_col

async def save_user(user_id, session_name):
    users_col.update_one(
        {"_id": user_id},
        {"$set": {"session": session_name}},
        upsert=True
    )

async def get_user_session(user_id):
    user = users_col.find_one({"_id": user_id})
    return user["session"] if user else None

async def save_user_settings(user_id, source, target, filters=None):
    users_col.update_one(
        {"_id": user_id},
        {"$set": {"source": source, "target": target, "filters": filters or {}}},
        upsert=True
    )

async def get_user_settings(user_id):
    user = users_col.find_one({"_id": user_id})
    return user if user else {}

async def delete_user(user_id):
    users_col.delete_one({"_id": user_id})

async def get_all_users():
    return users_col.find()