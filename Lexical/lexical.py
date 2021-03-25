import os.path
import re

reserved_words = ('program', 'var', 'begin', 'end', 'integer', 'real', 'if', 'then',
                  'else', 'boolean', 'procedure', 'while', 'do', 'not', 'true', 'false')

file_src = os.path.join("../.pas", "test.pas")

file = open(file_src, 'r')
content = file.read()
char_list = list(content)
current_char = -1
current_state = 0
token = ''
line_counter = 1

output_table = dict()
output_list = list()
tabela = []


def addToken(word, sym, line_counter):
    output_table['Token'] = word
    output_table['Symbol'] = sym
    output_table['Line'] = line_counter
    output_list.append(output_table.copy())


def fill_blanks(data, size):
    data = str(data)
    if len(data) > size:
        data = data[:size]
    return str('|  ' + data.ljust(size))


def printTable(table):
    table.append(fill_blanks('Token', 30) + fill_blanks("Classification",
                                                        30) + fill_blanks('Line', 5) + '  |')
    table.append(
        '================================================================================')
    for item in output_list:
        token = item["Token"].rstrip("\n")
        symbol = item["Symbol"].rstrip("\n")
        line = item["Line"]
        table.append(fill_blanks(token, 30) + fill_blanks(symbol,
                                                          30) + fill_blanks(line, 5) + '  |')

    with open("./resultado/tabela.txt", "w") as file:
        for i in table:
            print(i)
            file.write(str(i + '\n'))


def switchReservedSymbol():
    for item in output_list:
        if(item['Token'].lower() in reserved_words):
            item['Symbol'] = 'Reserved Word'
        if(item['Token'] == 'or'):
            item['Symbol'] = 'Additive Operator'
        if(item['Token'] == 'and'):
            item['Symbol'] = 'Multiplicative Operator'


def switchToQ0():
    global token, line_counter, current_state, char_list, current_char

    az = re.findall("[a-zA-Z]", char_list[current_char])
    digit09 = re.findall("[0-9]", char_list[current_char])

    if (len(az) > 0):
        current_state = 1
        token = char_list[current_char]
    elif (len(digit09) > 0):
        current_state = 2
        token = char_list[current_char]
    elif (char_list[current_char] == ' ' or char_list[current_char] == '\t'):
        current_state = 0
    elif (char_list[current_char] == ':'):
        token = char_list[current_char]
        current_state = 3
    elif (char_list[current_char] == '\n'):
        line_counter += 1
    elif (char_list[current_char] == '{'):
        token = char_list[current_char]
        current_state = 4
    elif (char_list[current_char] == ';'
          or char_list[current_char] == ','
          or char_list[current_char] == '('
          or char_list[current_char] == ')'
          or char_list[current_char] == '.'):
        addToken(char_list[current_char], 'Delimiter', line_counter)
    elif (char_list[current_char] == '>'):
        token = char_list[current_char]
        current_state = 6
    elif (char_list[current_char] == '<'):
        token = char_list[current_char]
        current_state = 7
    elif (char_list[current_char] == '='):
        addToken(char_list[current_char],
                 'Relational Operator', line_counter)
    elif (char_list[current_char] == '+' or char_list[current_char] == '-'):
        addToken(char_list[current_char],
                 'Additive Operator', line_counter)
    elif (char_list[current_char] == '*' or char_list[current_char] == '/'):
        addToken(char_list[current_char],
                 'Multiplicative Operator', line_counter)
    else:
        print('error<Unknown Symbol>: ' + char_list[current_char])
    return


def switchToQ1():
    global token, line_counter, current_state, char_list, current_char
    az09 = re.findall("\w", char_list[current_char])
    if (len(az09) > 0):
        current_state = 1
        token += char_list[current_char]
    else:
        # print('identifier: ' + token)
        addToken(token, 'Identifier', line_counter)
        current_char -= 1
        current_state = 0
        token = ''
    return


def switchToQ2():
    global token, line_counter, current_state, char_list, current_char
    digit09 = re.findall("[0-9]", char_list[current_char])
    if(len(digit09) > 0):
        current_state = 2
        token += char_list[current_char]
    else:
        if (char_list[current_char] == '.'):
            current_state = 5
            token += char_list[current_char]
            return
        # print('number: ' + token)
        addToken(token, 'Integer Number', line_counter)
        current_char -= 1
        current_state = 0
        token = ''
    return


def switchToQ3():
    global token, line_counter, current_state, char_list, current_char
    if(char_list[current_char] == '='):
        token += char_list[current_char]
        # print('assignment command: ' + token)
        addToken(token, 'Assignment Command', line_counter)
        current_state = 0
        token = ''
    else:
        # print('delimiter: ' + token)
        addToken(token, 'Delimiter', line_counter)
        current_char -= 1
        current_state = 0
        token = ''
    return


def switchToQ4():
    global token, line_counter, current_state, char_list, current_char
    token += char_list[current_char]
    if(char_list[current_char] == '}'):
        # print('comments: ' + token)
        # addToken(token, 'Comments', line_counter)
        current_state = 0
        token = ''
    elif (current_char == (len(char_list) - 1)):
        print('error<comment>: Open and not Closed comment')
    elif (char_list[current_char] == '\n'):
        line_counter += 1
    return


def switchToQ5():
    global token, line_counter, current_state, char_list, current_char
    digit09 = re.findall("[0-9]", char_list[current_char])
    if(len(digit09) > 0):
        current_state = 5
        token += char_list[current_char]
    else:
        # print('number: ' + token)
        addToken(token, 'Real Number', line_counter)
        current_char -= 1
        current_state = 0
        token = ''
    return


def switchToQ6():
    global token, line_counter, current_state, char_list, current_char
    if(char_list[current_char] == '='):
        token += char_list[current_char]
        addToken(token, 'Relational Operator', line_counter)
        current_state = 0
        token = ''
    else:
        addToken(token, 'Relational Operator', line_counter)
        current_char -= 1
        current_state = 0
        token = ''
    return


def switchToQ7():
    global token, line_counter, current_state, char_list, current_char
    if(char_list[current_char] == '='):
        token += char_list[current_char]
        addToken(token, 'Relational Operator', line_counter)
        current_state = 0
        token = ''
    else:
        if(char_list[current_char] == '>'):
            token += char_list[current_char]
            addToken(token, 'Relational Operator', line_counter)
            current_state = 0
            token = ''
            return
        addToken(token, 'Relational Operator', line_counter)
        current_char -= 1
        current_state = 0
        token = ''
    return


while(True):
    current_char += 1

    if (current_char == len(char_list)):
        switchReservedSymbol()
        printTable(tabela)
        exit()

    if (current_state == 0):
        switchToQ0()
        continue

    if (current_state == 1):
        switchToQ1()
        continue

    if (current_state == 2):
        switchToQ2()
        continue

    if (current_state == 3):
        switchToQ3()
        continue

    if (current_state == 4):
        switchToQ4()
        continue

    if (current_state == 5):
        switchToQ5()
        continue

    if (current_state == 6):
        switchToQ6()
        continue

    if (current_state == 7):
        switchToQ7()
        continue
