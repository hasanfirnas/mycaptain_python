str_input = input("Input : ")
list_input = str_input.split(",")
num = 0
while(num < len(list_input)):
    if int(list_input[num]) >= 0:
        print(list_input[num], end = " ")
    num += 1
