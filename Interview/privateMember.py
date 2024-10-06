class School():
    def __init__(self):
        self.__isWizard = True
        self.__spells = 0

    def __learn(self):
        self.__spells += 1

    def cast(self):
        if self.__isWizard:
            self.__learn()
            print("Lumos!")
        else:
            print("(Nothing happens)")

    def library(self):
        print(f"Spells: {self.__spells}")

if __name__ == "__main__":
    harry = School()

    harry.__learn()
    # AttributeError: 'School' object has no attribute '__learn'

    harry.cast()
    # Setter: Lumos!

    harry.library()
    # Getter: Spells: 1

    harry._Academy__spells = 10
    harry.library()
    # Spells: 10