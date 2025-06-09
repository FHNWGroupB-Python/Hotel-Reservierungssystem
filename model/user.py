ROLE_PERMISSIONS = {
    "admin": {"get_all_bookings", "get_all_rooms_with_equipment", "update_room"},
    "guest": {},
}


def requires_permission(action):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user = kwargs.get("user")
            if not user:
                raise Exception("User context missing.")
            if action not in ROLE_PERMISSIONS.get(user.role, set()):
                raise PermissionError(f"User with role {user.role} can't perform {action}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


class User:
    def __init__(self, role='guest'):
        self.role = role  # 'admin' or 'guest'
