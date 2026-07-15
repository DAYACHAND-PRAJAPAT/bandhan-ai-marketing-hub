from app.auth.security import hash_password, verify_password

hashed = hash_password("Bandhan123")
print("Hashed:", hashed)

print("Verify:", verify_password("Bandhan123", hashed))