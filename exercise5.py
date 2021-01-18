input1 = int(input("Enter number 1: "))
input2 = int(input("Enter number 2: "))
input3 = int(input("Enter number 3: "))
input4 = int(input("Enter number 4: "))
input5 = int(input("Enter number 5: "))
input6 = int(input("Enter number 6: "))
input7 = int(input("Enter number 7: "))
input8 = int(input("Enter number 8: "))
input9 = int(input("Enter number 9: "))
input10 = int(input("Enter number 10: "))

list1 = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10]

print("Your list is: ")
print(list1)
print("Your list of positive numbers is: ")
even_list = []
for i in list1:
    if i >= 0:
        even_list.append(i)
even_list.sort()
print(even_list)