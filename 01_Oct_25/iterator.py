class CountDown:
    def __init__(self, start):  #This is the constructor of the class, it initializes countdown obj with start num start
        self.current = start    #It sets self.current to start, that keep track of the current countdown value.

    def __iter__(self): #method called  when python want to iterate fromm your
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1


# Using custom iterator
print("Countdown from 5:")
for number in CountDown(5):
    print(number)


# Built-in iterators example
my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
