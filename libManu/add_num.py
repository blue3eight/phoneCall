def add_10(x):
    if type(x) not in [int, float]:
        raise TypeError('Int or Flat only.')
    return x + 10