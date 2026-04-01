# App configuration
import os

# Database settings
DB_HOST = "localhost"
DB_NAME = "production_db"
DB_USER = "admin"
DB_PASSWORD = "supersecret123"        # hardcoded password

# API Keys
STRIPE_KEY = "sk_live_abc123xyz789"   # hardcoded stripe key
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# JWT
JWT_SECRET = "myjwtsecret"
JWT_EXPIRY = None                      # no expiry set