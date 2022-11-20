# # creating a tuple using ()
# #  NOTE=tuple is used for not changing the value
# # t =(1, 2, 6, 4)
# # # Printing the value of tupples
# # t1 = () '''empty tuple'''
# # t1=(1) '''wrong way to declare tuple'''
# # t1(1,)  ''' '''
# # print(t[0])
# # # Cannot update the values of a tupples
# # t[0] = 34


# # user define program enter name of fruits
# f1 = input("Enter fruit no 1\n")
# f2 = input("Enter fruit no 2\n")
# f3 = input("Enter fruit no 3\n")
# f4 = input("Enter fruit no 4\n")
# f5 = input("Enter fruit no 5\n")

# myfruitlist = [f1, f2, f3, f4 ,f5]

# print(myfruitlist)
f2 = int(input("Enter student marks no 1\n"))
f1 = int(input("Enter student marks no 2\n"))
f3 = int(input("Enter student marks no 3\n"))
f4 = int(input("Enter student marks no 4\n"))
f5 = int(input("Enter student marks no 5\n"))

mylist = [f1,f2,f3,f4,f5]
mylist.sort()
print(mylist)