import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    length, numbers = map(int, input().split())
    numbers = list(str(numbers))
    # print(length, numbers)
    
    while True:
        for idx in range(len(numbers) - 1):
            if numbers[idx] == numbers[idx+1]:
                numbers.pop(idx)
                numbers.pop(idx)
                break
        else:
            break
    
    if numbers[0] == '0':
        numbers.pop(0)

    print('#{}'.format(tc), ''.join(numbers))