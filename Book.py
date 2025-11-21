from read import Library,Catalog
from read import Books,AudioBook,VideoBook,Magazine

def get_start():
    hey = Catalog("new")
    hey.add_books(Books("shadow", 110, 4, 3, 30))
    info = [["ali"],[],[],[]]
    print("""1 - User
2 - Admin""")
    chack = int(input("Choose the number: "))
    while True:
        if chack == 1:
            print("""0 - exit
1 - Books
2 - AudioBooks
3 - VideoBooks
4 - Magazine""")
            ask = int(input("Choose the option: "))
            if ask == 0:
                break
            elif ask == 1:
                print(" Books \n")
                for x in hey.books:
                    if isinstance(x, Books):
                        print(x.get_information())
            elif ask == 2:
                print(" AudioBooks \n")
                for x in hey.books:
                    if isinstance(x, AudioBook):
                        print(x.get_information())
            elif ask == 3:
                print(" VideoBooks \n")
                for x in hey.books:
                    if isinstance(x, VideoBook):
                        print(x.get_information())
            elif ask == 4:
                print(" Magazines \n")
                for x in hey.books:
                    if isinstance(x, Magazine):
                        print(x.get_information())
            else:
                print("Enter valid number")
        elif chack == 2:
            print("""0 - exit
1 - add Books
2 - add AudioBooks
3 - add VideoBooks
4 - add Magazine
5 - delete""")
            ask2 = int(input("Choose the option: "))

            if ask2 == 2:
                print("Adding books")
                title = input("Enter the title: ")
                page_count = input("Enter the pages: ")
                location = input("Enter the location")
                row = input("Enter the row: ")
                quantity = input("Enter the quantity: ")
                info[1].append(title)
                info[1].append(page_count)
                info[1].append(location)
                info[1].append(row)
                info[1].append(quantity)
            print(info)
            if ask2 == 3:
                title = input("Enter the title: ")
                page_count = input("Enter the pages: ")
                location = input("Enter the location")
                time = input("Enter the time: ")
                info[4].append(title)
                info[4].append(page_count)
                info[4].append(location)
                info[4].append(time)
            if ask2 == 4:
                title = input("Enter the title: ")
                page_count = input("Enter the pages: ")
                location = input("Enter the location")
                topic = input("Enter the topic: ")
                info[6].append(title)
                info[6].append(page_count)
                info[6].append(location)
                info[6].append(topic)
            if ask2 == 5:
                uninstall = input("choose item for deleting:")
                if uninstall in info:
                     del info[0][uninstall]
                     print(f"{uninstall} has deleted")
                else:
                    print(f"{uninstall} is not exist")

get_start()
