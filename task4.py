
if __name__ == '__main__':

    d = {
        1 : "Mondey",
        2 : "Tuesday",
        3 : "Wednesday",
        4 : "Thursday",
        5 : "Friday",
        6 : "Saturday",
        7 : "Sunday"
    }

    d = [(values, keys) for keys, values in d.items()]
    print(dict(d))