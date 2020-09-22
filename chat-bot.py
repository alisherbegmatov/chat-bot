from random import choice


def get_bot_response(user_response):

    num = int(user_response)
  
    price_1 = ["Nissan Versa", "Mazda 3", "Toyota Corola"]
    price_2 = ["Nissan Altima", "Mazda 6", "Toyota Camry"]
    price_3 = ["Chevrolet Silverado", "Ford F150", "RAM 1500"]
    price_4 = ["Nissan Armada", "Toyota Land Cruiser", "Lexus LX570"]
    price_5 = ["Chevrolet Corvette", "Dodge Viper", "Porsche 911"]

    if num <= 20000:
        return f'The best car in this price range is: {choice(price_1)}'
    elif num <= 40000:
        return f'The best car in this price range is: {choice(price_2)}'
    elif num <= 60000:
        return f'The best car in this price range is: {choice(price_3)}'
    elif num <= 80000:
        return f'The best car in this price range is: {choice(price_4)}'
    elif num <= 100000:
        return f'The best car in this price range is: {choice(price_5)}'
    else:
        return "Please Enter Range Between $0 and $100,000"

def stretch_func(user_response):
    num = int(user_response)

    price_1 = ["Nissan Versa", "Mazda 3","Toyota Corola"]
    price_2 = ["Nissan Altima", "Mazda 6", "Toyota Camry"]
    price_3 = ["Chevrolet Silverado", "Ford F150", "RAM 1500"]
    price_4 = ["Nissan Armada", "Toyota Land Cruiser", "Lexus LX570"]
    price_5 = ["Chevrolet Corvette","Dodge Viper", "Porsche 911"]

    if num <= 20000:
        return price_1
    elif num <= 40000:
        return price_2
    elif num <= 60000:
        return price_3
    elif num <= 80000:
        return price_4
    elif num <= 100000:
        return price_5
    else:
        return "Please Enter Range Between $0 and $100,000"


print("Welcome to car market bot!")

user_response = ''

user_response = input("Please enter your price range: ")
price = user_response

while user_response !='done':

    if user_response != 'show me something different':
        bot_response = get_bot_response(user_response)
        print(bot_response)
    else:
        user_response = input('Please enter the price again: ')
        print(stretch_func(user_response))

    user_response = input('Please type "done" if your done or "show me something different" to continue: ')
    