# def twosum(nums,target):
#     seen={}
#     for idx,num in enumerate(nums):
#         if (target-num) in seen:
#             return [seen[target-num],idx]
#         seen[num]=idx
            

# target=9
# nums=[2,7,11,13]
# print(twosum(nums,target))
target=9
nums=[2,7,11,13]
seen={}
for idx,num in enumerate(nums):
    if (target-num) in seen:
        print([seen[target-num],idx])
    seen[num]=idx

print(f'{seen}')
            

