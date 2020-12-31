import string
"""
Task 1

Make a program that has some sentence (a string) on input and returns a dict containing
all unique words as keys and the number of occurrences as values.

"""

if __name__ == '__main__':

    a = "Привет привет колесо ! веник! даша, привет пика.. колодец# веник # капа пока пока)) пока."

    for i in a.split(" "):
        for j in i:
            if j in string.punctuation:
                a = a.replace(j, "")
    a = a.replace("  ", " ")
    print(a.split(" "))

    d = {}

    for e in a.lower().split(" "):
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1
    print(d)
    print(d['веник'])









