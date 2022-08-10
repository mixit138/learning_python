memory = 0
result = 0

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n"
msg_5 = "Do you want to continue calculations? (y / n):\n"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)\n"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)\n"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)\n"


def check(v1, v2, v3):
    v1 = float(v1)
    v2 = float(v2)
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2) is True:
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    v = float(v)
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


while True:
    print(msg_0)
    calc = x, operation, y = input().split()
    if x == 'M':
        x = str(memory)
    if y == 'M':
        y = str(memory)
    if not x.replace('.', '', 1).isdigit() or not y.replace('.', '', 1).isdigit():
        print(msg_1)
        continue
    check(x, y, operation)
    if calc[1] == '+' or calc[1] == '-' or calc[1] == '*' or calc[1] == '/':
        try:
            x = float(x)
            y = float(y)
            if calc[1] == '+':
                result = x + y
                print(result)
            elif calc[1] == '-':
                result = x - y
                print(result)
            elif calc[1] == '*':
                result = x * y
                print(result)
            elif calc[1] == '/' and y != '0':
                result = x / y
                print(result)
        except ZeroDivisionError:
            print(msg_3)
            continue
    else:
        print(msg_2)
        continue

    answer_4 = input(msg_4)
    if answer_4 == 'y':
        if is_one_digit(result) is True:
            msg_index = 10
            if msg_index == 10:
                answer_10 = input(msg_10)
                if answer_10 == 'y':
                    if msg_index < 12:
                        msg_index += 1
                    else:
                        memory = result
                else:
                    pass
            if msg_index == 11:
                answer_11 = input(msg_11)
                if answer_11 == 'y':
                    if msg_index < 12:
                        msg_index += 1
                    else:
                        memory = result
            if msg_index == 12:
                answer_12 = input(msg_12)
                if answer_12 == 'y':
                    if msg_index < 12:
                        msg_index += 1
                    else:
                        memory = result
        else:
            memory = result
    else:
        pass

    answer_5 = input(msg_5)
    if answer_5 == 'y':
        pass
    elif answer_5 == 'n':
        break
