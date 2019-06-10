from werkzeug.security import safe_str_cmp
from user import User

# users = [
#     User(1, 'bob', 'asdf')
#
# ]
#
# username_table = {u.username: u for u in users}
# userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = User.find_user_by_name(username)
    # user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_user_by_id(user_id)