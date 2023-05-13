import json
import os


class Equivalent:
    def __init__(self) -> None:
        self.data = dict()
        with open("equivalent.json", "w") as file:
            json.dump(self.data, file, indent=2)

    def add(self, command, function):
        self.data[command] = function
        print("Data is added. \n", self.data)

    def display(self):
        pass 

    def delete_file(self):
        os.remove("equivalent.json")


EVL = Equivalent()
EVL.add("cli", "function")
EVL.delete_file()
