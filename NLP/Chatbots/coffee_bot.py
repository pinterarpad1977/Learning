def coffee_bot():
    print('Welcome to the Cafe!')
    size = get_size()
    #print(size)
    drink_type = get_drink_type()
    #print(drink_type)
    print(f'Alright, that\'s a {size} {drink_type} ')
    name = input('Can I have your name please? ')
    print(f'Thanks, {name}! Your drink will be ready shortly.')

def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large\n')
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:  # get_size() function is now calling itself, making it a *** recursive *** function
        # answer = get_size() - this is unnecessary, you can return the function call itself
        print_message()
        return get_size()

def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n[d] Back to size\n')
    if res == 'a':
        return 'Brewed Cofee'
    elif res == 'b':
        return 'Mocha'
    elif res == 'c':
        return order_latte()
    elif res == 'd':
        return get_size()
    else:
        print_message()
        return get_drink_type()

def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n[d] Back to type\n')
    if res == 'a':
        return 'Regular Latte'
    elif res == 'b':
        return 'Non-fat Latte'
    elif res == 'c':
        return 'Soy Latte'
    elif res == 'd':
        return get_drink_type()
    else:
        print_message()
        return order_latte()

def print_message():
    print('I\'m sorry, I did not understand your selection. \nPlease enter the corresponding letter for your response.\n')

