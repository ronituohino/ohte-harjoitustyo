def username_validation(username):
    """Validoi käyttäjänimen

    Args:
        username: Käyttäjänimi

    Returns:
        Taulukon, joka sisältää mahdolliset virheviestit
    """

    errors = []
    if not username:
        errors.append("Username is required")
    if not username or len(username) < 2:
        errors.append("Username must be at least 2 characters long")
    return errors


def password_validation(password):
    """Validoi salasanan

    Args:
        password: Salasana

    Returns:
        Taulukon, joka sisältää mahdolliset virheviestit
    """

    errors = []
    if not password:
        errors.append("Password is required")
    if not password or len(password) < 4:
        errors.append("Password must be at least 4 characters long")
    return errors


def password_again_validation(password, password_again):
    """Validoi salasana -uudestaan kentän

    Args:
        password: Salasana
        password_again: Sama salasana uudestaan

    Returns:
        Taulukon, joka sisältää mahdolliset virheviestit
    """

    errors = []
    if password != password_again:
        errors.append("Passwords have to match")
    return errors
