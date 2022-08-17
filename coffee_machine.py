espresso = {'water': 250, 'coffee_beans': 16, 'money': 4}
latte = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'money': 7}
cappuccino = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'money': 6}
ingredients = {'water': 400, 'milk': 540, 'coffee_beans': 120, 'disposable_cup': 9, 'money': 550}


def coffee_machine():
    print(f'''The coffee machine has:
{ingredients['water']} ml of water
{ingredients['milk']} ml of milk
{ingredients['coffee_beans']} g of coffee beans
{ingredients['disposable_cup']} disposable cups
${ingredients['money']} of money
''')
    return action()


def action():
    print('Write action (buy, fill, take, remaining, exit):')
    user_action = input()
    if user_action == 'buy':
        buy_coffee()
    elif user_action == 'fill':
        insert_item()
    elif user_action == 'take':
        give_money()
    elif user_action == 'remaining':
        coffee_machine()
    elif user_action == 'exit':
        pass


def buy_coffee():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    coffee = input()
    if coffee == '1':
        if ingredients['water'] - espresso['water'] < 0:
            print('Sorry, not enough water!')
            return action()
        else:
            ingredients['water'] -= espresso['water']

        if ingredients['coffee_beans'] - espresso['coffee_beans'] < 0:
            print('Sorry, not enough coffee beans')
            return action()
        else:
            ingredients['coffee_beans'] -= espresso['coffee_beans']

        if ingredients['disposable_cup'] - 1 < 0:
            print('Sorry, not enough disposable cup')
            return action()
        else:
            ingredients['disposable_cup'] -= 1
        ingredients['money'] += espresso['money']

    elif coffee == '2':
        if ingredients['water'] - latte['water'] < 0:
            print('Sorry, not enough water')
            return action()
        else:
            ingredients['water'] -= latte['water']
        if ingredients['milk'] - latte['milk'] < 0:
            print('Sorry, not enough milk')
            return action()
        else:
            ingredients['milk'] -= latte['milk']
        if ingredients['coffee_beans'] - latte['coffee_beans'] < 0:
            print('Sorry, mot enough coffee beans')
            return action()
        else:
            ingredients['coffee_beans'] -= latte['coffee_beans']
        if ingredients['disposable_cup'] - 1 < 0:
            print('Sorry, not enough disposable cup')
            return action()
        else:
            ingredients['disposable_cup'] -= 1
        ingredients['money'] += latte['money']

    elif coffee == '3':
        if ingredients['water'] - cappuccino['water'] < 0:
            print('Sorry, not enough water')
            return action()
        else:
            ingredients['water'] -= cappuccino['water']
        if ingredients['milk'] - cappuccino['milk'] < 0:
            print('Sorry, not enough milk')
            return action()
        else:
            ingredients['milk'] -= cappuccino['milk']
        if ingredients['coffee_beans'] - cappuccino['coffee_beans'] < 0:
            print('Sorry, not enough coffee beans')
            return action()
        else:
            ingredients['coffee_beans'] -= cappuccino['coffee_beans']
        if ingredients['disposable_cup'] - 1 < 0:
            print('Sorry, not enough disposable cup')
            return action()
        else:
            ingredients['disposable_cup'] -= 1
        ingredients['money'] += cappuccino['money']

    elif coffee == 'back':
        pass

    return action()


def insert_item():
    print('Write how many ml of water you want to add:')
    water_i = int(input())
    print('Write how many ml of milk you want to add:')
    milk_i = int(input())
    print('Write how many grams of coffee beans you want to add:')
    coffee_beans_i = int(input())
    print('Write how many disposable cups you want to add:')
    disposable_cup_i = int(input())
    ingredients['water'] += water_i
    ingredients['milk'] += milk_i
    ingredients['coffee_beans'] += coffee_beans_i
    ingredients['disposable_cup'] += disposable_cup_i
    return action()


def give_money():
    print(f"I gave you ${ingredients['money']}\n")
    ingredients['money'] = 0
    return action()


action()
