# -*- coding: utf-8 -*-
"""library management.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11Gmoq69t-HJpxE60r8gt4p2nLm2goMFV
"""

class Library():
    def __init__(self,Title,Author,ISBN):
        self.Books=[]
        self.Title=Title
        self.Author=Author
        self.ISBN=ISBN


    def showBooks(self):
        print(self.Books)


    def addBook(self):
      Title = input("Enter Book Title: ").upper()
      Author = input("Enter Book Author: ").split(",")
      Author = [x.strip().upper() for x in Author]

      if len(Author) < 1:
        print("Invalid Author Name: At least 1 Author Should Be Present")
        return

      ISBN = input("Enter Book ISBN: ")

      if len(ISBN) != 13:
        print("Invalid ISBN: ISBN Should Contain 13 Digit Number")
        return

      self.Books.append([Title, Author, ISBN])
      print("Book Added Successfully")


    def search_Title(self):
      title = input("Enter Book Title: ").upper()
      for book in self.Books:
        if title in book[0]:
            print("Book Found")
            print(book)
            found = True
            break
      if not found:
        print("Book Not Found")


    def search_Author(self):
      author = input("Enter Book Author: ").upper()
      found = False
      for book in self.Books:
        if author in book[1]:
            print("Book Found:")
            print(book)
            found = True

      if not found:
        print("No Books Found With This Author")


    def search_ISBN(self):
        isbn=input("Enter Book ISBN: ")
        found = False
        for book in self.Books:
            if isbn in book[2]:
                print("ISBN Found")
                print(book)
                found = True
                break
        if not found:
            print("No Book With This ISBN")

library=Library("My Library", "Unknown Author", "9781614841002")
while True:
  print("Show all Books --> 1")
  print("To Add Book --> 2")
  print("To Search Book By Title --> 3")
  print("To Search Book By Author --> 4")
  print("To Search Book By ISBN --> 5")
  print("To Exit --> 6")

  choice=(input("Enter Your Choice: "))

  if choice=="1":
    library.showBooks()
  elif choice=="2":
    library.addBook()
  elif choice=="3":
    library.search_Title()
  elif choice=="4":
    library.search_Author()
  elif choice=="5":
    library.search_ISBN()
  elif choice=="6":
    break
  else:
    print("Invalid Choice")