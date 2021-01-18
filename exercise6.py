print("This program allows you to enter a list of numbers and creates new list with only postive numbers!")
input1 = int(input("Enter number 1: "))
input2 = int(input("Enter number 2: "))
input3 = int(input("Enter number 3: "))
input4 = int(input("Enter number 4: "))
input5 = int(input("Enter number 5: "))

list1 = [input1, input2, input3, input4, input5]
print("Your list is : " + str(list1))

list2 = []
for i in list1:
    if i >= 0:
        list2.append(i)
print("Your positive numbers in your list are: " + str(list2))
    