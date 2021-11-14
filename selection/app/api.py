def parse_bool_param(param):
    TRUTHY = (True, 'true', 'yes', 'y', '1')
    FALSY = (False, 'false', 'no', 'n', '0')
    if param.lower() in TRUTHY:
        return True
    elif param.lower() in FALSY:
        return False
    else:
        return None
