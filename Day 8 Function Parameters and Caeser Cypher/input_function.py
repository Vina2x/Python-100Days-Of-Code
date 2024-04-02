# normal function
def greet():
    print("Hello World")
    print("How are you today?")
    print("Nice to meet you!")

greet()

# function that can take input
# name is the parameter here and whatever is passed through it is Argument e.g Jack :)
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you today {name}?")
    print(f"Nice to meet you {name}!")

greet_with_name("Jack")


def greet_with(name,location):
    print(f"Hello {name}!")
    print(f"How's the weather in {location}?")

# positional arguments
greet_with("Jack", "Japan")

# keyword arguments
greet_with(location="Japan", name="Jack")