# Define a class named American which has a static method called printNationality.
# Define a class named American and its subclass NewYorker.

class American():
    @staticmethod
    def printNationality():
        print("I am American")


class NewYorker(American):
    pass


american = American()
american.printNationality()
American.printNationality()
