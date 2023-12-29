# stack


def solution(s: str):
    answer = True
    if s[0] == ")" or s[-1] == "(":
        return False

    temp = list(s)

    stack = []
    for char in temp:
        
        if stack:
            c = stack.pop()
            if c == '(':
                if c == char:
                    stack.extend([c, char])
            else:
                return False
        else:
            stack.append(char)
    
    if stack:
        answer = False
    return answer



# s, expected = '()()', True
s, expected = '())((()))(()', False
result = solution(s)
assert result == expected