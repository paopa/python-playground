class Base(object):
    def __init__(self):
        self.name = "Base"

    def run(self):
        print(self.name, "is running")


class Sub(Base):
    def __init__(self):
        self.name = "Sub"

    def run(self):
        print(self.name, "is running")
