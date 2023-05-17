import json
import os
from prettytable import PrettyTable

class Equivalent:
    def __init__(self) -> None:
        self.data = dict()

    def create_file(
        self,
    ) -> None:
        if not os.path.exists("../data"):
            os.makedirs("../data")
        with open("../data/equivalent.json", "w") as file:
            json.dump(self.data, file, indent=2)
            print("File has been created!!")

    def file_status(self) -> bool:
        return os.path.exists("../data/equivalent.json")

    def add(self, command, function) -> None:
        if self.file_status():
            self.data[command] = function
            with open("../data/equivalent.json", "w") as file:
                json.dump(self.data, file, indent=2)
            print("Data is added. \n", self.data)
        else:
            print("File has not been created :(")

    def display(self):
        if self.file_status():
            with open(file="../data/equivalent.json", mode="r") as data_file:
                self.data = json.load(data_file)
            table = PrettyTable(["CLI", "Function"])
            for key, value in self.data.items():
                table.add_row([key, value])
            print(table)
        else:
            print("File does not exist :(")

    def delete_file(self):
        if self.file_status():
            os.remove("../data/equivalent.json")
            print("The file has been deleted!")
        else:
            print("There is no file. Please, create a new file!")


if __name__ == "__main__":
    eql = Equivalent()
    eql.create_file()
    eql.add("cli node command", " Node API function")
    eql.add("cli node command 2", " Node API function 2")
    eql.display()
