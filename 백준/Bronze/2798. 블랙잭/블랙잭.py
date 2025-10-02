from itertools import combinations

card_num, target_num = map(int, input().split())
card_list = list(map(int, input().split()))
result = 0

for cards in combinations(card_list, 3):
    temp_num = sum(cards)
    if result < temp_num <= target_num:
        result = temp_num
print(result)