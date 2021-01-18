input1 = int(input("Enter number 1: "))
input2 = int(input("Enter number 2: "))
input3 = int(input("Enter number 3: "))
input4 = int(input("Enter number 4: "))
input5 = int(input("Enter number 5: "))


list1 = [input1, input2, input3, input4, input5]
print("Your list is: ")
print(list1)
print("The largest number in your list is: ")
list1.sort()
print(list1[-1])