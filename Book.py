from abc import abstractmethod, ABC


class Library(ABC):
    number = 0

    def __init__(self, title, page_count, location):
        self.title = title
        self.page_count = page_count
        self.location = location
        self.number += 1

    @abstractmethod
    def get_information(self):
        pass

    @classmethod
    def count_of_books(cls):
        return cls.number


class Books(Library):
    def __init__(self, title, page_count, location, row, quantity):
        super().__init__(title, int(page_count), location)
        self.quantity = quantity
        self.row = row

    def get_information(self):
        return f"""title ({self.title.title()}),
pages ({self.page_count}),
location ({self.location}th floor),
row ({self.row}th),
quantity ({self.quantity}).
"""


class AudioBook(Library):
    def __init__(self, title, page_count, location, time):
        super().__init__(title, int(page_count), location)
        self.time = time

    def get_information(self):
        return f"""title ({self.title.title()}),
pages ({self.page_count}),
location ({self.location}),
time ({self.time}hour).
"""


class VideoBook(Library):
    def __init__(self, title, page_count, location, time, quality):
        super().__init__(title, int(page_count), location)
        self.quality = quality
        self.time = time

    def get_information(self):
        return f"""title {self.title.title()}
pages ({self.page_count}),
location ({self.location}),
time ({self.time}),
quality ({self.quality}p).
"""


class Magazine(Library):
    def __init__(self, title, page_count, location, topic):
        super().__init__(title, int(page_count), location)
        self.topic = topic

    def get_information(self):
        return f"""title ({self.title.title()}),
pages ({self.page_count}),
location ({self.location}th floor),
topic ({self.topic})."""


new = Books("shadow", 110, 4, 3, 30)
new2 = AudioBook("shadow2", 100, "local.com", 3)
new3 = VideoBook("shadow3", 43, "local.com", 3, 750)
new4 = Magazine("shadow4", 50, "NewYork 30-store", "cars")
print(new.get_information())
print(new2.get_information())
print(new3.get_information())
print(new4.get_information())
