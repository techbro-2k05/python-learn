import sys

sys.stdout = open('output.txt', 'w')

sys.stdin = open('input.txt', 'r')
t = int(input())

for pl in range(t):
    n = int(input())
    a = input().strip()

    # Case for strings of length 2
    if n == 2:
        print(int(a))
        continue

    # Case for strings of length 3
    if n == 3:
        if "0" in a:
            if a[0] == "0" or a[2] == "0":
                print(0)
            else:
                print(min(int(a[0]) * int(a[2]), int(a[0]) + int(a[2])))
        else:
            ans_1 = min(int(a[0]) * int(a[1:]), int(a[0]) + int(a[1:]))
            ans_2 = min(int(a[2]) * int(a[0:2]), int(a[2]) + int(a[0:2]))
            print(min(ans_2, ans_1))
        continue

    # Case for strings of length > 3
    if "0" in a:
        print("0")
        continue

    # Convert string digits to integers
    a = [int(i) for i in a]

    # Initial minimum value from the first two digits
    mins = a[0] * 10 + a[1]
    index = 0

    # Finding the best adjacent pair to minimize
    for i in range(1, n - 1):
        current_value = a[i] * 10 + a[i + 1]
        if current_value < mins:
            if a[i + 1] == 1 and mins // 10 == a[i]:
                continue
            else:
                mins = current_value
                index = i
        else:
            if mins % 10 == 1 and mins // 10 == a[i]:
                mins = current_value
                index = i

    # Removing the selected pair from the string
    p = a[:index] + a[index + 2:]

    # Summing the remaining digits to the minimum value
    for i in p:
        if i == 1:
            continue
        else:
            mins += i

    print(mins)