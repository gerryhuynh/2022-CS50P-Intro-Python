class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError(f"Number of cookies exceed cookie jar capacity of {self.capacity}.")
        
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("There aren't THAT many cookies!")
        
        self.size -= n

    def add_cookies(self):
        cookies = int(input("Enter number of cookies to add: "))

        self.deposit(cookies)

    def eat_cookies(self):
        cookies = int(input("Enter number of cookies to eat: "))

        self.withdraw(cookies)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Please enter a non-negative capacity for the cookie jar.")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


def main():
    cookie_jar = Jar(-1)
    cookie_jar.add_cookies()
    print(cookie_jar)
    cookie_jar.eat_cookies()
    print(cookie_jar)
    cookie_jar.eat_cookies()
    print(cookie_jar)
    print(cookie_jar.capacity)
    print(cookie_jar.size)



if __name__ == "__main__":
    main()