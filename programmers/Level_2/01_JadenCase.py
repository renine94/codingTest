# https://school.programmers.co.kr/learn/courses/30/lessons/12951


def solution(s):
    words = s.split(" ")
    return " ".join(list(map(lambda x: x.capitalize(), words)))


s, expected = "3people unFollowed me", "3people Unfollowed Me"
result = solution(s)

assert result == expected
