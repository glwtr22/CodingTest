num = input()
l = len(num) // 2

left = 0
right = 0
i = 0

for n in num:
    if i >= l:
        right += int(n)
        continue
    left += int(n)
    i += 1

if left == right:
    print("LUCKY")
else:
    print("READY")



# n = input()
# length = len(n)
# summary = 0
#
# for i in range(length//2):
#     summary += int(n[i])
#
# for i in range(length//2, length):
#     summary -= int(n[i])
#
# if summary == 0:
#     print("LUCKY")
# else:
#     print("READY")