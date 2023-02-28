from passlib.context import CryptContext

pwd_config = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000
)

def encrypt_password(user_password):
    return pwd_config.hash(user_password)

# Hashed, unhashed
def verify_password(hashed_password, user_password):
    return pwd_config.verify(user_password, hashed_password)