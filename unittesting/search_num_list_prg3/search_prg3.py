def index_list1(l):
    search=int(input("enter element in list:"))
    for i in range (len(l)):
        if l[i] == search:
            print(i)
index_list1([10,34,45,56])