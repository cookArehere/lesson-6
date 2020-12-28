
"""
Task 2

Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock.

"""
if __name__ == '__main__':

    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }



    def sum(stock, prices):

        e = 0

        for i in stock.keys():
           e += stock[i] * prices[i]
        return(e)

    print(sum(stock, prices))



