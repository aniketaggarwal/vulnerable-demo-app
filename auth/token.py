import jwt
import datetime

SECRET = "hardcoded_jwt_secret_123"   # hardcoded secret

def generate_token(user_id):
    # JWT with no expiry
    payload = {
        "user_id": user_id,
        # no exp field
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verify_token(token):
    # no error handling
    return jwt.decode(token, SECRET, algorithms=["HS256"])