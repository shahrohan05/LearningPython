import xml.etree.ElementTree as et
import os


def print_element_with_children(element):
    if len(list(element)) > 0:
        for child in element:
            elem_str = "{}:{}".format(child.tag, child.attrib)
            if child.text is not None and child.text.strip() != "":
                elem_str += ", text : {}".format(child.text)
            print(elem_str)
            print_element_with_children(child)
    else:
        pass
        # print(element.tag, element.attrib)


class XMLParser:
    def __init__(self, filename):
        try:
            file = open(filename)
            self.data = et.parse(file)
            print("File Ready : {}".format(os.getcwd() + "\\" + filename))
        except FileNotFoundError as e:
            print(e)
            self.data = None
        finally:
            file.close()

    def print_tree(self):
        if self.data is None:
            print("Error! Cannot find the specified file.")
            return
        root = self.data.getroot()
        print_element_with_children(root)


if __name__ == "__main__":
    parser = XMLParser(input("XML File Source : "))
    parser.print_tree()
