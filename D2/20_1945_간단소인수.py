"""
숫자 N은 아래와 같다.
N=2^a x 3^b x 5^c x 7^d x 11^e
N이 주어질 때 a, b, c, d, e 를 출력하라.

[제약 사항]
N은 2 이상 10,000,000 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.
10  
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
#1 3 2 2 3 1
#2 6 1 2 3 0
#3 6 4 2 0 1
#4 0 0 2 3 0
#5 0 3 4 0 1
#6 4 4 1 0 0
#7 7 3 0 3 0
#8 0 8 0 0 0
#9 0 0 2 0 0
#10 1 3 3 2 0

"""

# v = int(input())
# i = 2
# # 입력받은 v 가 1 이 아니라면 while문 실행
# while v != 1:
#     # 만약 v 를 i=2 로 나눠서 나머지가 0 이라면
#     if v % i == 0:  
#         v = v/i 
#         print(i, end=' ')
#     else:
#         i += 1

T = int(input())
prime_list = [2, 3, 5, 7, 11]
temp_dic = {}
 
for i in range(1, T+1):
    number = int(input())
    
    for prime in prime_list:
        cnt = 0

        while number % prime == 0:
            cnt += 1
            number = number/prime

        temp_dic[prime] = cnt
     
    print('#{0} {1} {2} {3} {4} {5}'.format(i, temp_dic[2], temp_dic[3], temp_dic[5], temp_dic[7], temp_dic[11]))
