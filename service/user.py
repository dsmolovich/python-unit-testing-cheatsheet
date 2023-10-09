from models.user import User

def create_user(name):
    user = User()
    user.name = name
    return user.name
