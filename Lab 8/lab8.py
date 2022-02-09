f = open("mydata2.txt")
text = f.read()
d = open("dictionary.txt")
dictionary = d.read()


# Problem 1
for i in text.splitlines():
    if i.lower().find("lol") >= 0:
        print(i)


# Problem 2
def dict_to_str(d):
    list_of_items = list(d.items())

    string = str(list_of_items[0][0]) + ", " + str(list_of_items[0][1])

    for keys,values in list_of_items[1:]:
        string += "\n" + str(keys) + ", " + str(values)
    return string

# Problem 3
def dict_to_str_sorted(d):
    list_of_items = list(d.items())
    list_of_items = sorted(list_of_items)

    string = str(list_of_items[0][0]) + ", " + str(list_of_items[0][1])

    for keys,values in list_of_items[1:]:
        string += "\n" + str(keys) + ", " + str(values)
    return string

# Problem 4
dictionary = dictionary.splitlines()
dictionary2 = {}
for i in dictionary:
    dictionary2.update({i.split("  ")[0]: i.split("  ")[1:]})


if __name__ == "__main__":
    d = {1:2, 2:3, 0:1}