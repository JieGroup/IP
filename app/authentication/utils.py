from __future__ import annotations

from werkzeug.security import (
    generate_password_hash, 
    check_password_hash
)

def check_password(user, password):
    return check_password_hash(user['password_hash'], password)