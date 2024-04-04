# https://school.programmers.co.kr/learn/courses/30/lessons/176962?language=python3

from datetime import datetime, timedelta


def solution(plans):
    answer = []

    stack = []
    for i in range(len(plans)):
        name, start, playtime = plans[i]

        start_obj = datetime.strptime(start, "%H:%M")
        playtime_obj = timedelta(minutes=int(playtime))

        if i + 1 <= len(plans) - 1:
            nname, nstart, nplaytime = plans[i + 1]
            nstart_obj = datetime.strptime(nstart, "%H:%M")
            if start_obj + playtime_obj <= nstart_obj:
                answer.append(name)
            else:
                stack.append(name)
    return answer


plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
expected = ["korean", "english", "math"]

result = solution(plans)
assert result == expected
