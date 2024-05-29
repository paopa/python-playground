class P:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = "c"

    def run(self):
        print("P run")
        print(self.a)
        print(self.b)
        print(self.c)
        self._hidden()

    def _hidden(self):
        print("Hidden")


class C(P):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.c = "cc"

    def run(self):
        print("C run")
        print(self.c)
        self._hidden()
        super().run()


if __name__ == "__main__":
    c = C(1, 2)
    c.run()
