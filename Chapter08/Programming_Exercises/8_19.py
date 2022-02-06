# write a program to implement a user-defined queue

print('--- A Program to implement a user-defined queue ---')
print()

queue=[]
ch=0
while(ch!=4):
    print("-------MENU-------------")
    print("1.INSERT")
    print("2.DELETE")
    print("3.DISPLAY")
    print("4.EXIT")
    ch=int(input("Enter your choice: "))

    if ch==1:
        ele=input("Enter the element to be inserted: ")
        queue.append(ele) #u can also append which will insert the element at the last of the list
    elif ch==2:
        if len(queue)==0:
            print("QUEUE EMPTY")
        else:
            print("DELETED ELEMENT IS : ",queue.pop(0))#if pop is defined without index it will take last value
    elif ch==3:
        if len(queue)==0:
            print("QUEUE EMPTY")
        else:
            print(queue)