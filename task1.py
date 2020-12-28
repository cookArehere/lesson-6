
"""
Task 1

Make a program that has some sentence (a string) on input and returns a dict containing
all unique words as keys and the number of occurrences as values.

"""

if __name__ == '__main__':

    a = "Привет привет колесо веник даша привет пика колодец веник капа пока пока пока"
    split_a = a.lower().split(" ")
    d = {}

    for i in split_a:
        if i not in d:
            d[i] = split_a.count(i)
    print(d)