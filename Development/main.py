import function
import read
import borrow
read.read_()

newbookprice=0
function.show()
books = function.books()
running=False
while running==False:
        try:
                decision =int(input("\nBorrow[1] \nReturn[2] \nExit[3]"))

                if decision == 1:
                    condition=False
                    while condition==False:
                            try:
                                    bookno = int(input("Enter Book Id:")) - 1
                                    booklist=function.books()
                                    
                                    while bookno<0 or bookno>=len(booklist):
                                        bookno = int(input("\nIncorrect book ID \nEnter The Book Id:")) - 1
                                    bookprice=0
                                    if int(booklist[bookno][2])!=0:
                                        bookprice = int(input("How Many Books You Want to Borrow:"))
                                      
                                        while bookprice<=0 or bookprice>int(booklist[bookno][2]):
                                            bookprice = int(input("\nInvalid bookquantity.\nHow Many Books You Want to Borrow:"))
                                            
                                    else :
                                           print("Book Out Of Stock")
                                           break
                                    name = input("Enter Your Name:")
                                    p=float(booklist[bookno][3].replace("$",""))*bookprice


                                    print(p)
                                    booklistArray=[]
                                    booklistArray.append(booklist[bookno][1])
                                    print(booklistArray)
                                    var_3=input("Do you want Another Transaction:(yes/no)")
                                    
                                    
                                    if var_3!="yes":
                                            newbookprice=p
                                            borrow.borrow(bookno, bookprice)
                                            borrow.forstudent(name,bookno,bookprice,p,booklistArray)
                                
                                
                                    while var_3 == "yes":
                                            
                                        function.show()  
                                        bookno=0
                                        bookno = int(input("Enter The Book Id:")) - 1
                                        booklist=function.books()
                                            
                                        while bookno<0 or bookno>=len(booklist):
                                            bookno = int(input("\nIncorrect book ID \nEnter Book Id:")) - 1
                                        bookprice=0
                                        if int(booklist[bookno][2])!=0:
                                            bookprice = int(input("How Many Books Do You Want to Borrow:"))
                                                   
                                            while bookprice<=0 or bookprice>int(booklist[bookno][2]):
                                                bookprice = int(input("\nInvalid bookquantity.\nHow Many Books Do You Want to Borrow:"))
                                                    
                                        else :
                                                print("\nBook Out Of Stock")
                                                break
                                        if booklist[bookno][1] not in booklistArray:
                                                booklistArray.append(booklist[bookno][1])
                                                print(booklistArray)

                                        newbookprice=p+float(booklist[bookno][3].replace("$",""))*bookprice
                                        var_4=input("\nDo you want Another Transaction:(yes/no)")
                                        if var_4=="yes":
                                            continue
                                        else:
                                            break
                                    
                                    borrow.borrow(bookno, bookprice)
                                    borrow.forstudent(name,bookno,bookprice,newbookprice,booklistArray)
                                    condition=True

                            except:
                                    print("\nInvalid Book Id!")
                    
                    
                elif decision == 2:
                    condition=False
                    function.show()
                    while condition==False:
                        try:
                            bookno = int(input("Enter Book Id:")) -1
                            booklist=function.books()

                            while bookno<0 or bookno>=len(booklist):
                                bookno = int(input("\nIncorrect Book ID \nEnter Book Id:")) - 1
                            bookprice=0
                            if int(booklist[bookno][2])!=0:
                                bookprice = int(input("\nHow Many Books Do You Want to Borrow:"))

                                while bookprice<=0 or bookprice>int(booklist[bookno][2]):
                                    bookprice = int(input("\nInvalid bookprice. \nHow Many Books Do You Want to Borrow:"))
                            else:
                                print("\nBook Out Of Stock")
                                break
                            name = input("Enter Your Name:")
                            booklistArray=[]
                            booklistArray.append(booklist[bookno][1])
                            print(booklistArray)
                            function.returnb(bookno,bookprice)
                            function.forlibrary(name,bookno,bookprice,booklistArray)
                            condition=True
                            var_2=input("\nDo you want Another Transaction:")
                            if var_2 == "yes":
                                function.show()
                                bookno=0
                                bookno=int(input("Enter Book Id:"))-1
                                booklist=function.books()

                                while bookno<0 or bookno>=len(booklist):
                                    bookno = int(input("\n Incorrect Book ID \nEnter The Book Id:"))-1
                                bookprice=0
                                if int(boolist[bookno][2])!=0:
                                    bookprice = int(input("\nHow Many Books Do You Want to Borrow:"))

                                    while bookprice<=0 or bookprice>int(booklist[bookno][2]):
                                        bookprice = int(input("\nInvalid bookprice. \nHow Many Books You Want to Borrow:"))
                                else:
                                    print("\nBook Out Of Stock")
                                    break
                                if booklist[bookno][1] not in booklostArray:
                                    booklistArray.append(booklist[bookno][1])
                                    print(booklistArray)

                                var_1=input("\nDo you want Another Transaction:(yes/no)")
                                if var_1 == "yes":
                                    continue
                                else:
                                    break
                                function.returnb(bookno, bookprice)
                                function.forlibrary(name,bookno,bookprice,booklistArray)
                                condition=True
                        except:
                            print("\nInvalid Book Id!")
                    
                        
                            

                elif decision == 3:
                        break

                else:
                        print("Choose number 1-3")
                        condition=True
                
        except:
                print("Please Enter a Valid Number")

