class Book:

    def __init__(self, title, author,Book_value,inventory):
        self.title = title
        self.author = author
        self.Book_value = Book_value
        self.inventory = inventory

    def __str__(self):
        return "title : "+self.title+" - Author : "+self.author+" - Book : "+str(self.Book_value)+" - Inventory : "+str(self.inventory)

book1 = Book("hate story","dk abdul",350,4)
print(book1)
book2 = Book("hate story","dk abdul",350,4)
print(book2)
book3 = Book("toy story"," abdu",550,5)
print(book3)
book4 = Book("mahabharat"," ram",550,10)
print(book4)

Book_dictionary = { 1:Book("hate story","dk abdul",350,4),2: Book("hate story","dk abdul",350,4),3:Book("toy story"," abdu",550,5),4:Book("mahabharat"," ram",550,10)}

for key,value in Book_dictionary.items():
    print(f"key: {key},value: {value}")
