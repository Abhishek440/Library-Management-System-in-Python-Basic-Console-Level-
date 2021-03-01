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
def borrow(bookno,bookprice):
    book = books()
    change = int(book[bookno][2])
    change -= bookprice
    book[bookno][2] = str(change)


    
    file = open("books.txt","w")

    for a in range(len(book)):
        file.write(str(book[a][0])+","+str(book[a][1])+","+str(book[a][2])+","+str(book[a][3])+"\n")

def forstudent(name, bookno, bookprice,newbookprice,booklistArray):
    print(newbookprice)
    book = books()
    now=datetime.datetime.now()
    todaysDate=datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    
    
    
    p=float(book[bookno][3].replace("$",""))*bookprice
    file = open(name+str(now)+".txt","w")
    file.write("Entry Date:"+todaysDate+"\n")
    file.write("Customer Name:"+name+"\n")        
    file.write("Total Price:"+str(newbookprice)+"\n")
    file.write("Name of The Book:\n")
    for a in booklistArray:
        file.write(str(a)+"\n")
