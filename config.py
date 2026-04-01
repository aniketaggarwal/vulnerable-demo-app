import os

# Application Configuration
APP_NAME = "GitHopper"
APP_ENV = "production"
DEBUG = False

# Database
DB_HOST = "prod-db.us-east-1.rds.amazonaws.com"
DB_NAME = "githopper_prod"
DB_USER = "admin"
DB_PASSWORD = "Pr0d@ccess#2024"

# AWS Credentials
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = "us-east-1"

# Stripe
STRIPE_SECRET_KEY = "sk_live_51abc123XYZtest"
STRIPE_WEBHOOK_SECRET = "whsec_abc123xyz789"

# JWT
JWT_SECRET = "my_super_secret_jwt_key_2024"
JWT_ALGORITHM = "HS256"
JWT_EXPIRY = None

# SendGrid
SENDGRID_API_KEY = "SG.abc123xyz.EXAMPLE_KEY_HERE"

# Firebase
FIREBASE_API_KEY = "AIzaSyBMxfOSo8jKEOOrD9GmTyAtjl5JPewEvMA"
FIREBASE_PROJECT_ID = "githopper-prod"

# Twilio
TWILIO_ACCOUNT_SID = "ACabc123xyz789example"
TWILIO_AUTH_TOKEN = "abc123xyz789authtoken"
TWILIO_PHONE = "+1234567890"