import json
import os


class Equivalent:
    def __init__(self) -> None:
        self.data = dict()

    def create_file(
        self,
    ) -> None:
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
        pass

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
