import json

from infra.repositories.user import UserRepository
def lambda_handler(event, context):

    new_user = UserRepository.insert_user()

    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "User Created Successfully",
            "data": new_user
        }),
    }