def count(N):
    facingeachother = 0
    hat_numbers = [] 
    for person in range(N):
        hat_numbers.append(int(input("")))
        
    for person in range(N):
        opposite_person = (person + N // 2) % N
        if hat_numbers[person] == hat_numbers[opposite_person]:
            facingeachother += 1
    return facingeachother



N = int(input(""))
print(count(N))  