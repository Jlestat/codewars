def are_you_playing_banjo(name: str) -> str:
    if name[0].lower() != 'r':
        return f'{name} does not play banjo'
    else:
        return f'{name} plays banjo'