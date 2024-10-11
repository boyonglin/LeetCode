def career(name):
    def decorator(func):
        def wrap():
            print("Yer a {}, {}.".format(func.__name__, name))
            return func()
        return wrap
    return decorator

name = "Harry"

@career(name)
def wizard():
    print("I'm a what?")

if __name__ == "__main__":
    wizard()
    # Yer a wizard, Harry.
    # I'm a what?