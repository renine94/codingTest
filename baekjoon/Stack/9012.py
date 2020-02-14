import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T+1):
    data = list(input())
    # print(data)

    # 스택 생성
    stack = []

    res = 'YES'
    for d in data:
        if data[0] == ')': # 데이터의 처음이 ) 이면 바로 종료
            res = 'NO'
            break
        
        if d == '(':    
            stack.append(d)
        elif d == ')':
            if stack:   # 스택에 값이 남아 있으면 pop 해라
                stack.pop()
            else:
                res = 'NO'
                break
    else: # for else 문은 for 가 정상적으로 끝난후에 실행하게됨 ( break 를 만나서 종료되면 else문 실행 안함 )
        if stack: # 반복을 마쳤는데도 스택에 값이 남아있으면..
            res = 'NO'


    print(res)

        
        


    


    



        