from abc import ABC, abstractmethod
from typing import List, Dict, Any
import xml.etree.ElementTree as ET
import csv
import json
### Strategy Pattern

# Step 1: Create the FileParser interface
class FileParser(ABC):

    @abstractmethod
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        pass


# Step 2: Implement the file parsers
# TODO: Implement CSVParser, JSONParser, and XMLParser classes
class CSVParser(FileParser):
    def __init__(self):
        self.data = []
        self.file_path = None

    def parse_file(self, file_path: str):
        self.file_path = file_path
        try:
            # Open the file in read mode ('r')
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.data.append(row)

        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        return self.data


class JSONParser(FileParser):
    def __init__(self):
        self.data = None
        self.file_path = None

    def parse_file(self, file_path: str):
        self.file_path = file_path
        try:
            # Open the file in read mode ('r')
            with open(self.file_path, 'r') as file:
                # Use json.load() to parse the file content into a Python dictionary or list
                self.data = json.load(file)


        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from the file '{self.file_path}'. Check the file format.")
        return self.data


class XMLParser(FileParser):
    def _init__(self):
        self.data = None
        self.file_path = None

    def parse_file(self, file_path: str):
        self.file_path = file_path
        try:
            # Parse the XML file
            tree = ET.parse(self.file_path)
            # Get the root element (<items>)
            root = tree.getroot()

            list_of_dicts = []

            # Iterate through all direct children of the root (the <item> elements)
            for child in root:
                item_dict = {}
                # Iterate through the elements within each child (<name>, <color>, etc.)
                for element in child:
                    # Add the tag as the key and the text content as the value
                    item_dict[element.tag] = element.text
                list_of_dicts.append(item_dict)

            self.data = list_of_dicts
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")

        return self.data


# Step 3: Implement the FileReader class
class FileReader:

    def __init__(self, file_parser: FileParser):
        # TODO: Initialize the file reader with the given file_parser
        self.file_parser = file_parser

    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        # TODO: Read the file at the given file_path and return a list of dictionaries using the specified file parser
        return self.file_parser.parse_file(file_path)


# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a file reader with a CSVParser
    reader = FileReader(CSVParser())

    # TODO: Read a sample CSV file and print the list of dictionaries
    data = reader.read_file(r"C:\Users\pdsan\Documents\GitHub\BasicAlgorithms\database\estaciones_bici2.csv")
    print(data)
