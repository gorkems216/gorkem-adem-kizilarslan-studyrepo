my_tuple = ( 0 , 1 , 2 , "hi" , 4 , 5 )
lst = []
for i in my_tuple:
    lst.append(i)
lst[3] = 3
my_tuple = tuple(lst)
print(my_tuple)
