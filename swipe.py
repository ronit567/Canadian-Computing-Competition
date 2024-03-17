def swiping_direction(lst, dir, val, iindex):
    num_swipes = 0
    if dir == 'R':
        for i in range(len(lst)):
            if lst[i] == val:
                lst[i+1:iindex+1] = [val] * (iindex - i)
                num_swipes = iindex - i
                break
    elif dir == 'L':
        for i in range(len(lst)):
            if lst[i] == val:
                lst[i:iindex] = [val] * (iindex - i)
                num_swipes = iindex - i
                break
    return num_swipes

def checker(list1, list2, N):
    if list1 == list2:
        print("YES")
        print("0")
        return

    if len(list1) != len(list2):
        print("NO")
        return

    total_swipes = 0
    for number in range(N):
        if list1[number] != list2[number]:
            i = max(list1[number], list2[number])
            val = min(list1[number], list2[number])
            dir = 'L' if list1[number] < list2[number] else 'R'
            swipes = swiping_direction(list1, dir, val, i)
            total_swipes += swipes
            if list1 == list2:
                print("YES")
                if dir == 'L':
                    print(f"L {val} {i}")
                else:
                    print(f"R {val} {i}")
                print(total_swipes)
                return
            else:
                print("NO")
                return

N = int(input(""))
list1 = [int(x) for x in input("")]
list2 = [int(x) for x in input("")]

# Checking if transformation is possible
checker(list1, list2, N)
