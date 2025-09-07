import string
def count_letters(data):
    """Counts the number of indivdual letters which appear in the string, data"""
    data = data.lower()
    dict = {}
    for char in data:
        if char in string.ascii_lowercase:
            if char in dict.keys():
                num = dict.get(char)
                dict[char] = num + 1
            else: dict.update({char: 1})
    return dict

##with open("frost.txt", "r") as file:
##    data_frost = file.read()
##file.close()
##print(count_letters(data_frost))
