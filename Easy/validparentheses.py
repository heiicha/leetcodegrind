def isValid(s):
    if len(s) <=1:
        return False
    chars =[ char for char in s]
    open = []
    close = []
    for char in chars:
        if char in ['(', '{', '[']:
            open.append(char)
        if char in [')', '}', ']']:
            close.append(char)

    for char in open[::-1]:
        last_index = len(chars) - 1 - chars[::-1].index(char)
        if last_index + 1 < len(chars): 
            last_index = len(chars) - 1 - chars[::-1].index(char)
            pair = chars[last_index] + chars[last_index + 1]
        else:
            return False
        if pair not in ['()', '{}', '[]']:
            return False
        del chars[last_index]
        del chars[last_index]
    if len(chars) == 0:
        return True   
    else:
        return False

isValid("[({(())}[()])]")

