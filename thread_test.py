import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.condition = threading.Condition()
        self.foo_flag = True
        self.yeah_flag = False

    def foo(self):
        for _ in range(self.n):
            with self.condition:
                while not self.foo_flag:
                    self.condition.wait()
                print("foo", end="")
                self.foo_flag = False
                self.condition.notify_all()

    def bar(self):
        for _ in range(self.n):
            with self.condition:
                while self.foo_flag or self.yeah_flag:
                    self.condition.wait()
                print("bar", end="")
                self.yeah_flag = True
                self.condition.notify_all()

    def yeah(self):
        for _ in range(self.n):
            with self.condition:
                while not self.yeah_flag:
                    self.condition.wait()
                print("yeah")
                self.yeah_flag = False
                self.foo_flag = True
                self.condition.notify_all()


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    foobar = FooBar(n)
    funtion_list = [foobar.foo, foobar.bar, foobar.yeah]
    for f in funtion_list:
        threading.Thread(target=f).start()
