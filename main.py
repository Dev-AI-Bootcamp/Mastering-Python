
name: str = "Your name here"
age: int = 52
height: float = 1.82
is_student: bool = False

# This is a comment
# and next is a function
def greet(username: str) -> str:
    var_not_used = 42  # This variable is not used
    if not username:
        return "Hello, World!"
    else:
        return f"Hello, {username}!"

def SimpleGreet(username):
    return "Hello, " + username + "!"

# a little object oriencted programming example
class Dog: 
    species = "Canis familiaris"
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def bark(self) -> str:
        return "Woof!"

# common wait to start a program only if it's not loaded as a module
def main():
    greet(name)
    SimpleGreet(name)
    charly = Dog("Charly", 3)
    print(charly.name)
    print(charly.bark())

if __name__ == "__main__":
    main()
