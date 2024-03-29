from re import split


def camelize(str_: str) -> str:
    """
    :param str_: str
    :return: str
    """
    return ''.join(i.capitalize() for i in split('([^a-zA-Z0-9])', str_) if i.isalnum())


print(camelize('cODE warS'))