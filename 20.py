def isValid(s):
    stack = []
    for i in s:
        if i in "[{(":
            stack.append(i)
        else:
            dict = {"]": "[", ")": "(", "}": "{"}
            if stack and dict[i] == stack[-1]:
                del stack[-1]
            else:
                return False
            
    if len(stack) == 0:
        return True
    return False


s = "()"

print(isValid(s))
