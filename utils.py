password_history = []

def save_password(password):
    password_history.append(password)
    if len(password_history) > 5:
        password_history.pop(0)
    return password_history
