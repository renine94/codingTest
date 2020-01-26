
# [10, 7, 6, 3, 5, 1, 8, 4, 3, 5]
price = [1, 1, 5, 2, 1]

revenue = []
cost = []

# 매매가 리스트의 길이
print( len(price) )

# 매매가 최대가 되는날 index
print( price.index(max(price)) )

# 최대 매매값 index가 0이 아니면 그전까진 모두 구입
# 최대 매매값일때 모두 판매
# 