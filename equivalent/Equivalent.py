import json
import os


class Equivalent:
    def __init__(self) -> None:
        self.data = dict()

    def create_file(self,)-> None:
        with open("../data/equivalent.json", "w") as file:
            json.dump(self.data, file, indent=2)

    def add(self, command, function):
        self.data[command] = function
        print("Data is added. \n", self.data)

    def display(self):
        pass 

    def delete_file(self):
        os.remove("../data/equivalent.json")


EVL = Equivalent()
#EVL.create_file()
EVL.delete_file()
