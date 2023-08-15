import jwt
import time

import settings
from src.service import error_responses


def execute(client_id: str, client_secret: str, user_id: str) -> str:
    if client_id != settings.JWT_CLIENT_ID or client_secret != settings.JWT_CLIENT_SECRET:
        raise error_responses.InvalidCredentialsAPIError

    payload = {
            'iat': time.time() - 100,
            'exp': time.time() + settings.JWT_TOKEN_EXPIRATION_SECONDS,
            'sub': user_id
        }
    return jwt.encode(payload, settings.JWT_CLIENT_SECRET, algorithm='HS256')