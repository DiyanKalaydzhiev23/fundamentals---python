nums = [int(n) for n in input().split()]
command = input().split()

while "end" not in command:
    if "swap" in command:
        i_1 = int(command[1])
        i_2 = int(command[2])
        nums[i_1], nums[i_2] = nums[i_2], nums[i_1]
    elif "multiply" in command:
        i_1 = int(command[1])
        i_2 = int(command[2])
        result = nums[i_1] * nums[i_2]
        nums[i_1] = result
    elif "decrease" in command:
        for i in range(len(nums)):
            nums[i] -= 1
    command = input().split()

print(f"{', '.join(list(map(lambda x: str(x), nums)))}")
