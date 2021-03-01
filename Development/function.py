import datetime

def show():
    file = open("books.txt","r")
    print(file.read())

def books():
    books = []
    file = open("books.txt","r")
    for a in file:
        books.append(a.strip('\n').split(","))

    return books
  
def returnb(bookno, bookprice):
    book = books()
    change = int(book[bookno][2])
    change += bookprice
    book[bookno][2] = str(change)
    
    file = open("books.txt","w")
    print(file)
    for a in range(len(book)):
        file.write(str(book[a][0])+","+str(book[a][1])+","+str(book[a][2])+","+str(book[a][3])+"\n")
    

def forlibrary(name, bookno, bookprice,booklistArray):
    var_5=int(input("Enter Number of Day:"))
    while var_5 <=0:
        print("Enter a valid day")
        a=int(input("Enter Number of Day:"))
    var_6=var_5-10
    if var_6 >= 0:
        print("The price of fine is",var_6*2)
        
    else:
        print("No fine")
        
    book = books()
    now = datetime.datetime.now()
    todaysDate = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")    
    file = open(name+str(now)+".txt","w")
    file.write("Date:"+str(todaysDate)+"\n")
    file.write("name:"+name+"\n")
    file.write("Fine:"+str(a))
    for a in booklistArray:
        file.write(str(a)+"\n")




    
