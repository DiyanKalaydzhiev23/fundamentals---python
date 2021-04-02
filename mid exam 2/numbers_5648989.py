nums = [int(n) for n in input().split()]
average = sum(nums) / len(nums)
bigger_then_avg = []

for el in nums:
    if el > average:
        bigger_then_avg.append(el)

if bigger_then_avg:
    if len(bigger_then_avg) >= 5:
        for i in range(5):
            print(max(bigger_then_avg), end=" ")
            bigger_then_avg.remove(max(bigger_then_avg))
    else:
        for i in range(len(bigger_then_avg)):
            print(max(bigger_then_avg), end=" ")
            bigger_then_avg.remove(max(bigger_then_avg))
else:
    print("No")
