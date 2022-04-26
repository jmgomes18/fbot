import json

from utils.json_encoder import MyJSONEncoder
from infra.repositories.user import UserRepository


def insert_user_handler(event, context):

    UserRepository.insert_user()

    return {
        "statusCode": 201,
        "body": {
            "message": "User Created Successfully",
        },
    }


def list_user_handler(event, context):
    users = UserRepository.list_user()

    return {
        "status_code": 200,
        "body": {
            "message": "Listed Users",
            "users": json.dumps(users, cls=MyJSONEncoder),
        },
    }
