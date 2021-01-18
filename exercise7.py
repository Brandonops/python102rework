def list_multi(list):
    for i in range(len(list)):
        list[i] = list[i] * 5
    print(list)




input1 = int(input("Enter number 1: "))
input2 = int(input("Enter number 2: "))
input3 = int(input("Enter number 3: "))
input4 = int(input("Enter number 4: "))
input5 = int(input("Enter number 5: "))

list1 = [input1, input2, input3, input4, input5]
list_multi(list1)

