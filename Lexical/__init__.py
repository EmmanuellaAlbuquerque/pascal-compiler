import os.path
import re
import sys
sys.tracebacklimit = 0


class Lexical:
    def __init__(self, path_filename):
        self.path_directory = os.path.dirname(os.path.abspath(__file__))

        self.reserved_words = ('program', 'var', 'begin', 'end', 'integer', 'real', 'if', 'then',
                               'else', 'boolean', 'char', 'procedure', 'while', 'do', 'not', 'true', 'false')

        file_src = path_filename

        file = open(file_src, 'r')
        content = file.read()
        self.char_list = list(content)
        self.current_char = -1
        self.current_state = 0
        self.token = ''
        self.line_counter = 1

        self.output_table = dict()
        self.output_list = list()
        self.tabela = []

    def runLexicalAnalysis(self):

        while(True):
            self.current_char += 1

            if (self.current_char == len(self.char_list)):
                self.switchReservedSymbol()
                self.printTable(self.tabela, self.output_list,
                                self.path_directory)
                return self.output_list

            if (self.current_state == 0):
                self.switchToQ0()
                continue

            if (self.current_state == 1):
                self.switchToQ1()
                continue

            if (self.current_state == 2):
                self.switchToQ2()
                continue

            if (self.current_state == 3):
                self.switchToQ3()
                continue

            if (self.current_state == 4):
                self.switchToQ4()
                continue

            if (self.current_state == 5):
                self.switchToQ5()
                continue

            if (self.current_state == 6):
                self.switchToQ6()
                continue

            if (self.current_state == 7):
                self.switchToQ7()
                continue

    def addToken(self, word, sym, line_counter):
        self.output_table['Token'] = word
        self.output_table['Classification'] = sym
        self.output_table['Line'] = line_counter
        self.output_list.append(self.output_table.copy())

    def fill_blanks(self, data, size):
        data = str(data)
        if len(data) > size:
            data = data[:size]
        return str('|  ' + data.ljust(size))

    def printTable(self, table, output_list, path_directory):
        table.append(self.fill_blanks('Token', 30) + self.fill_blanks("Classification",
                                                                      30) + self.fill_blanks('Line', 5) + '  |')
        table.append(
            '================================================================================')
        for item in output_list:
            token = item["Token"].rstrip("\n")
            classification = item["Classification"].rstrip("\n")
            line = item["Line"]
            table.append(self.fill_blanks(token, 30) + self.fill_blanks(classification,
                                                                        30) + self.fill_blanks(line, 5) + '  |')

        with open(path_directory + "/resultado/tabela.txt", "w") as file:
            for i in table:
                # print(i)
                file.write(str(i + '\n'))

    def switchReservedSymbol(self):
        for item in self.output_list:
            if(item['Token'].lower() in self.reserved_words):
                item['Classification'] = 'Reserved Word'
            if(item['Token'] == 'or'):
                item['Classification'] = 'Additive Operator'
            if(item['Token'] == 'and'):
                item['Classification'] = 'Multiplicative Operator'
            if(item['Token'].lower() == 'true' or item['Token'].lower() == 'false'):
                item['Classification'] = 'boolean'

    def switchToQ0(self):

        az = re.findall("[a-zA-Z]", self.char_list[self.current_char])
        digit09 = re.findall("[0-9]", self.char_list[self.current_char])

        if (len(az) > 0):
            self.current_state = 1
            self.token = self.char_list[self.current_char]
        elif (len(digit09) > 0):
            self.current_state = 2
            self.token = self.char_list[self.current_char]
        elif (self.char_list[self.current_char] == ' ' or self.char_list[self.current_char] == '\t'):
            self.current_state = 0
        elif (self.char_list[self.current_char] == ':'):
            self.token = self.char_list[self.current_char]
            self.current_state = 3
        elif (self.char_list[self.current_char] == '\n'):
            self.line_counter += 1
        elif (self.char_list[self.current_char] == '{'):
            self.token = self.char_list[self.current_char]
            self.current_state = 4
        elif (self.char_list[self.current_char] == ';'
              or self.char_list[self.current_char] == ','
              or self.char_list[self.current_char] == '('
              or self.char_list[self.current_char] == ')'
              or self.char_list[self.current_char] == '.'):
            self.addToken(self.char_list[self.current_char], 'Delimiter',
                          self.line_counter)
        elif (self.char_list[self.current_char] == '>'):
            self.token = self.char_list[self.current_char]
            self.current_state = 6
        elif (self.char_list[self.current_char] == '<'):
            self.token = self.char_list[self.current_char]
            self.current_state = 7
        elif (self.char_list[self.current_char] == '='):
            self.addToken(self.char_list[self.current_char],
                          'Relational Operator', self.line_counter)
        elif (self.char_list[self.current_char] == '+' or self.char_list[self.current_char] == '-'):
            self.addToken(self.char_list[self.current_char],
                          'Additive Operator', self.line_counter)
        elif (self.char_list[self.current_char] == '*' or self.char_list[self.current_char] == '/'):
            self.addToken(self.char_list[self.current_char],
                          'Multiplicative Operator', self.line_counter)
        else:
            raise Exception('in line ' + str(self.line_counter) + '. error<Unknown Symbol>: ' +
                            self.char_list[self.current_char])

    def switchToQ1(self):

        az09 = re.findall("\w", self.char_list[self.current_char])
        if (len(az09) > 0):
            self.current_state = 1
            self.token += self.char_list[self.current_char]
        else:
            # print('identifier: ' + token)
            self.addToken(self.token, 'Identifier', self.line_counter)
            self.current_char -= 1
            self.current_state = 0
            self.token = ''

    def switchToQ2(self):

        digit09 = re.findall("[0-9]", self.char_list[self.current_char])
        if(len(digit09) > 0):
            self.current_state = 2
            self.token += self.char_list[self.current_char]
        else:
            if (self.char_list[self.current_char] == '.'):
                self.current_state = 5
                self.token += self.char_list[self.current_char]
                return
            # print('number: ' + token)
            self.addToken(self.token, 'integer', self.line_counter)
            self.current_char -= 1
            self.current_state = 0
            self.token = ''

    def switchToQ3(self):

        if(self.char_list[self.current_char] == '='):
            self.token += self.char_list[self.current_char]
            # print('assignment command: ' + token)
            self.addToken(self.token, 'Assignment Command', self.line_counter)
            self.current_state = 0
            self.token = ''
        else:
            # print('delimiter: ' + token)
            self.addToken(self.token, 'Delimiter', self.line_counter)
            self.current_char -= 1
            self.current_state = 0
            self.token = ''

    def switchToQ4(self):

        self.token += self.char_list[self.current_char]
        if(self.char_list[self.current_char] == '}'):
            # print('comments: ' + token)
            # addToken(token, 'Comments', line_counter)
            self.current_state = 0
            self.token = ''
        elif (self.current_char == (len(self.char_list) - 1)):
            raise Exception('in line ' + str(self.line_counter) +
                            '. error<comment>: Open and not Closed comment')
        elif (self.char_list[self.current_char] == '\n'):
            self.line_counter += 1

    def switchToQ5(self):

        digit09 = re.findall("[0-9]", self.char_list[self.current_char])
        if(len(digit09) > 0):
            self.current_state = 5
            self.token += self.char_list[self.current_char]
        else:
            # print('number: ' + token)
            self.addToken(self.token, 'real', self.line_counter)
            self.current_char -= 1
            self.current_state = 0
            self.token = ''

    def switchToQ6(self):

        if(self.char_list[self.current_char] == '='):
            self.token += self.char_list[self.current_char]
            self.addToken(self.token, 'Relational Operator', self.line_counter)
            self.current_state = 0
            self.token = ''
        else:
            self.addToken(self.token, 'Relational Operator', self.line_counter)
            self.current_char -= 1
            self.current_state = 0
            self.token = ''

    def switchToQ7(self):

        if(self.char_list[self.current_char] == '='):
            self.token += self.char_list[self.current_char]
            self.addToken(self.token, 'Relational Operator', self.line_counter)
            self.current_state = 0
            self.token = ''
        else:
            if(self.char_list[self.current_char] == '>'):
                self.token += self.char_list[self.current_char]
                self.addToken(self.token, 'Relational Operator',
                              self.line_counter)
                self.current_state = 0
                self.token = ''
                return
            self.addToken(self.token, 'Relational Operator', self.line_counter)
            self.current_char -= 1
            self.current_state = 0
            self.token = ''
