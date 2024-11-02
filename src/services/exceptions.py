class ProfilesNotFoundException(Exception):
    """Профили не найдены"""

    pass


class ProfileAlreadyExists(Exception):
    """Профиль с таким именем уже существует"""

    pass


class ProfileNotFound(Exception):
    """Профиль не найден"""

    pass
