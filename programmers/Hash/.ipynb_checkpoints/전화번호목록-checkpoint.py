# 문제
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        temp = phone_book[i]
        for j in range(i+1, len(phone_book)):
            if temp in phone_book[j]:
                return False
    return True