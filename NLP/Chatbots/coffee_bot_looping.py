from coffee_bot import print_message, get_size, order_latte
import sys

yes = ['y', 'sure', 'betcha', 'yes', 'more']
no = ['n', 'no', 'nah', 'thx', 'that\'s it', 'done', 'finished']
stop = ['end', 'stop', 'leave', 'exit', 'bye', 'cya', 'break']

def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large\n').lower()
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    elif res in stop:
        leave()
    else:  # get_size() function is now calling itself, making it a *** recursive *** function
        # answer = get_size() - this is unnecessary, you can return the function call itself
        print_message()
        return get_size()

def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n[d] Back to type\n').lower()
    if res == 'a':
        return 'Regular Latte'
    elif res == 'b':
        return 'Non-fat Latte'
    elif res == 'c':
        return 'Soy Latte'
    elif res == 'd':
        return get_drink_type()
    elif res in stop:
        leave()
    else:
        print_message()
        return order_latte()
    
def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n[d] Back to size\n').lower()
    if res == 'a':
        return 'Brewed Cofee'
    elif res == 'b':
        mocha_type = order_mocha()
        return mocha_type
    elif res == 'c':
        return order_latte()
    elif res == 'd':
        return get_size()
    elif res in stop:
        leave()
    else:
        print_message()
        return get_drink_type()

def order_mocha():
    while True:
        res = input('Would you like to try our special edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time!\n').lower()
        if res.lower() in yes:
            return 'Pepppermint Mocha'
        elif res.lower() in no:
            return 'Regular Mocha'
        elif res in stop:
            leave()
        else:
            print_message()

def leave():
    print('Sorry to see you go come back soon!')
    sys.exit(0)

def coffee_bot_looping():
    print('Welcome to the Cafe!')
    drinks = []
    order_drink = 'y'
    while order_drink == 'y':
        size = get_size()
        #print(size)
        drink_type = get_drink_type()
        #print(drink_type)
        print(f'Alright, that\'s a {size} {drink_type} ')
        drinks.append(size+' '+drink_type)
        while True:    
            more = input('Do you need anything else: \n[y] \n[n]').lower()
            if more in yes:
                order_drink = 'y'
                break
            elif more in no:
                order_drink = more
                break
            elif more in stop:
                leave()
        
    name = input('Can I have your name please? ')
    print(f'Thanks, {name}! \n Okay, so I have:')
    for drink in drinks:
        print('- '+drink)
    if len(drinks) > 1:
        print('Your drinks will be ready shortly.')
    else:
        print('Your drink will be ready shortly.')

coffee_bot_looping()