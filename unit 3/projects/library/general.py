def str_clean(inp):
    inp = str(inp)
    return ''.join([*filter(str.isalnum, inp)])