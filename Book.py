from read import Books, AudioBook, VideoBook, Magazine
from read import Catalog


def get_start(books, audiobooks, videobooks, magazine):
    hey = Catalog("new")
    key = "Davronbek"
    remaining_chances = 5
    success = False

    while True:  # main menu loop
        print("1 - User\n2 - Admin")
        chack = int(input("Choose the number: "))

        while True:
            password = input("Enter key: ")
            if password == key:
                print("Access granted! Admin menu here...")
                success = True
                break
            else:
                remaining_chances -= 1
                if remaining_chances == 0:
                    print("You are not admin, main menu")
                    break
                elif remaining_chances == 1:
                    print("Last chance!")
                else:
                    print(f"Wrong key! You have {remaining_chances} attempts left.")

        if not success:
            continue

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
1 - see all
2 - add Books
3 - add AudioBooks
4 - add VideoBooks
5 - add Magazine
6 - delete""")
            ask2 = int(input("Choose the option: "))
            if ask2 == 1:
                print("""1 - Books
2 - AudioBooks
3 - VideoBooks
4 - Magazine""")
                link = int(input("Which one: "))
                if link == 1:
                    print(books)
                elif link == 2:
                    print(audiobooks)
                elif link == 3:
                    print(videobooks)
                elif link == 4:
                    print(magazine)

            if ask2 == 2:
                print("Adding books")
                title = input("Enter the title: ")
                page_count = input("Enter the pages: ")
                location = input("Enter the location")
                row = input("Enter the row: ")
                quantity = input("Enter the quantity: ")
                books[title] = {"pages": page_count, "location": location, "row": row, "quantity": quantity}

            elif ask2 == 3:
                title = input("Enter the title: ")
                page_count = input("Enter the pages: ")
                location = input("Enter the location")
                time = input("Enter the time: ")
                audiobooks[title] = {"pages": page_count, "location": location, "time": time}

            elif ask2 == 4:
                title = input("Enter the title: ")
                page_count = input("Enter the pages: ")
                location = input("Enter the location")
                topic = input("Enter the topic: ")
                videobooks[title] = {"pages": page_count, "location": location, "topic": topic}
            elif ask2 == 5:
                title = input("Enter the title: ")
                page_count = input("Enter the pages: ")
                location = input("Enter the location")
                topic = input("Enter the topic: ")
                videobooks[title] = {"pages": page_count, "location": location, "topic": topic}

            elif ask2 == 6:
                uninstall = input("choose item for deleting:")
                if uninstall.isalpha() and uninstall in books:
                    del books[uninstall]
                    print(f"{uninstall} has deleted")
                elif uninstall.isalpha() and uninstall in audiobooks:
                    del audiobooks[uninstall]
                    print(f"{uninstall} has deleted")
                elif uninstall.isalpha() and uninstall in videobooks:
                    del videobooks[uninstall]
                    print(f"{uninstall} has deleted")
                elif uninstall.isalpha() and uninstall in magazine:
                    del magazine[uninstall]
                    print(f"{uninstall} has deleted")
                else:
                    print(f"{uninstall} doesn't exist or invalid value")


get_start(dict(), dict(), dict(), dict())
