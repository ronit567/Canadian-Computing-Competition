def letters(the_strings):
    answer = []
    for string in the_strings:
        alternating = True
        prev_type = None

        for j in string:
            current_type = "heavy" if string.count(j) > 1 else "light"
            if prev_type == current_type:
                alternating = False
                break
            prev_type = current_type

        answer.append("T" if alternating else "F")

    return answer

T, placeholder = map(int, input().split())
different_strings = []

for i in range(T):
    different_strings.append(input())

answer_in_list = letters(different_strings)
for result in answer_in_list:
    print(result)
