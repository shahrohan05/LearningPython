import json


def print_value_from_json(data, key):
    if isinstance(data,list):
        for d in data:
            if isinstance(d,dict):
                print_value_from_json(d, key)
    elif isinstance(data,dict):
        for k in data.keys():
            # print(str(k).strip(),key)
            if str(k).strip() == key:
                print("value : {}".format(data[key]))
                return
            if isinstance(data[k], dict) or isinstance(data[k], list):
                print_value_from_json(data[k], key)


class JSONParer:

    def __init__(self, filename):
        try:
            file = open(filename,"r")
            self.data = json.load(file)
        except FileNotFoundError as e:
            print("Error! File not found.")
        finally:
            file.close()

    def find_value(self, key):
        print_value_from_json(self.data, key)


if __name__ == "__main__":
    parser = JSONParer(input("json file name : "))
    parser.find_value(input("key : "))
