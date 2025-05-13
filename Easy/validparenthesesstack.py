def isValid(s):
    stack = []
    parenthesis = {
        ')':'(',
        ']': '[',
        '}': '{'
    }
    for c in s:
        if c in parenthesis:
            if stack and stack[-1] == parenthesis[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return stack==[]
    