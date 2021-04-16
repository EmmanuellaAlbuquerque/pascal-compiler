import sys
sys.tracebacklimit = 0

current_id = 0
lexical_dict = dict()
declaration_key = 0
type_control_stack = list()
identifier_stack = list()


class SymbolsStack:
    def __init__(self):
        self. symbols_stack = list()

    def push(self, tokenItem):
        i = len(self.symbols_stack) - 1
        # while didn't reach the end of the scope
        while (i > 0 and self.symbols_stack[i] != '$'):
            if (self.symbols_stack[i] == tokenItem['Token']):
                raise Exception('variable: ' + tokenItem['Token'] +
                                ' has already been declared')
            i -= 1
        self.symbols_stack.append(tokenItem)

    def pop(self):
        self.symbols_stack.pop(-1)

    def search(self, tokenItem):
        i = len(self.symbols_stack) - 1
        # while didn't reach the end of the scope
        while (i >= 0):
            if (self.symbols_stack[i]['Token'] == tokenItem['Token']):
                if ('Type' in self.symbols_stack[i]
                        and self.symbols_stack[i]['Type'] == 'program'):
                    raise Exception('Semantic error, in line ' + str(self.symbols_stack[i]['Line']) +
                                    '. The program name: "' + self.symbols_stack[i]['Token'] +
                                    '" cannot be used in commands and expressions')

                typeToken = self.symbols_stack[i]
                typeToken['searchLine'] = tokenItem['Line']
                type_control_stack.append(typeToken)
                # print('--------- type control stack ----------')
                # for element in type_control_stack:
                #     print(element)
                # print('---------------------------------------')
                return True
            i -= 1
        symbolsStack.getProgramTokens()
        raise Exception('Semantic error, variable: ' +
                        tokenItem['Token'] + ' used but not declared')

    def closeScope(self):
        i = len(self.symbols_stack) - 1
        # print('\nscope--------------- before ---------------\n')
        # self.getProgramTokens()

        while (self.symbols_stack[i]['Token'] != '$'):
            # self.getProgramTokens()
            self.symbols_stack.pop()
            i -= 1
        self.symbols_stack.pop()
        # print('\nscope--------------- after ---------------\n')
        # self.getProgramTokens()

    def getProgramTokens(self):
        stack = list()
        for element in self.symbols_stack:
            stack.append(str(element))
        print(',\n'.join(stack))

    def setType(self, i, type):
        self.symbols_stack[i]['Type'] = type

    def get(self):
        return self.symbols_stack


symbolsStack = SymbolsStack()


def updateTCS(type='additiveMultiplicativeOp'):
    if (type_control_stack[-1]['Type'] == 'integer' and type_control_stack[-2]['Type'] == 'integer'):
        # updates PCT
        type_control_stack.pop(-1)
        type_control_stack.pop(-1)

        if (type == 'relationalOp'):
            type_control_stack.append(
                {'Token': 'integer (rellOp) integer', 'Type': 'boolean'})
        else:
            type_control_stack.append(
                {'Token': 'integer (addMultOP) integer', 'Type': 'integer'})
    elif (type_control_stack[-1]['Type'] == 'real' and type_control_stack[-2]['Type'] == 'real'):
        # updates PCT
        type_control_stack.pop(-1)
        type_control_stack.pop(-1)

        if (type == 'relationalOp'):
            type_control_stack.append(
                {'Token': 'resultType', 'Type': 'boolean'})
        else:
            type_control_stack.append({'Token': 'resultType', 'Type': 'real'})
    elif (type_control_stack[-1]['Type'] == 'integer' and type_control_stack[-2]['Type'] == 'real'):
        # updates PCT
        type_control_stack.pop(-1)
        type_control_stack.pop(-1)

        if (type == 'relationalOp'):
            type_control_stack.append(
                {'Token': 'resultType', 'Type': 'boolean'})
        else:
            type_control_stack.append({'Token': 'resultType', 'Type': 'real'})
    elif (type_control_stack[-1]['Type'] == 'real' and type_control_stack[-2]['Type'] == 'integer'):
        # updates PCT
        type_control_stack.pop(-1)
        type_control_stack.pop(-1)

        if (type == 'relationalOp'):
            type_control_stack.append(
                {'Token': 'resultType', 'Type': 'boolean'})
        else:
            type_control_stack.append({'Token': 'resultType', 'Type': 'real'})
    elif (type_control_stack[-1]['Type'] == 'boolean' and type_control_stack[-2]['Type'] == 'boolean'):
        # updates PCT
        type_control_stack.pop(-1)
        type_control_stack.pop(-1)
        type_control_stack.append(
            {'Token': 'resultType', 'Type': 'boolean'})
    elif (type_control_stack[-1]['Type'] == 'integer' and type_control_stack[-2]['Type'] == 'procedure'):
        # updates PCT
        type_control_stack.pop(-1)
        type_control_stack.pop(-1)

        if (type == 'relationalOp'):
            type_control_stack.append(
                {'Token': 'resultType', 'Type': 'boolean'})
        else:
            type_control_stack.append({'Token': 'resultType', 'Type': 'void'})
    else:
        line = ''
        if ('searchLine' in type_control_stack[-2]):
            line = type_control_stack[-2]['searchLine']
        raise Exception('in line ' + str(line) + '\n     type1: ' +
                        str(type_control_stack[-1]['Type']) +
                        '\n     type2: ' +
                        str(type_control_stack[-2]['Type']) +
                        '\n     Type mismatch, Incompatibility of Types')


def next():
    global current_id, lexical_dict
    current_id += 1
    if (current_id >= len(lexical_dict)):
        lexical_item = lexical_dict[current_id - 1]
        raise Exception('next, in line ' + str(lexical_item['Line']) + ' \n'
                        + 'error, waiting "next" but came: '
                        + '"'
                        + 'anything' + '"')
    return lexical_dict[current_id]


def multiplicativeOp():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == '*' or lexical_item['Token'] == '/' or lexical_item['Token'].lower() == 'and'):

        # if (lexical_item['Token'].lower() == 'and'):
        #     position = (len(type_control_stack) - 1) - 1
        #     # print(position)
        #     type_control_stack.insert(position,
        #                               {'Token': 'andResult', 'Classification': 'boolean', 'Line': 7, 'Type': 'boolean'})
        # print(type_control_stack)
        # exit()

        lexical_item = next()


def AdditiveOp():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == '+' or lexical_item['Token'] == '-' or lexical_item['Token'].lower() == 'or'):
        lexical_item = next()

    # print('--------- type control stack ----------')
    # for element in type_control_stack:
    #     print(element)
    # print('---------------------------------------')
    # exit()


def relationalOp():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == '='
            or lexical_item['Token'] == '<'
            or lexical_item['Token'] == '>'
            or lexical_item['Token'] == '<='
            or lexical_item['Token'] == '>='
            or lexical_item['Token'] == '<>'):
        lexical_item = next()


def sign():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == '+' or lexical_item['Token'] == '-'):
        lexical_item = next()
    else:
        pass


def factorC():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == '('):
        lexical_item = next()
        expressionsList()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == ')'):
            lexical_item = next()
        else:
            lexical_item = lexical_dict[current_id]
            raise Exception('factorC, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting ")" but came: '
                            + '"'
                            + lexical_item['Token'] + '"')
    else:
        pass


def factor():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):

        # print('factor' + str(lexical_item))
        if (declaration_key == 0):
            symbolsStack.push(lexical_item)
        else:
            symbolsStack.search(lexical_item)

        lexical_item = next()
        factorC()
        lexical_item = lexical_dict[current_id]
    elif (lexical_item['Token'].isdigit()
          or lexical_item['Token'].replace(".", "").isdigit()
          or lexical_item['Token'].lower() == 'true'
            or lexical_item['Token'].lower() == 'false'):
        lexical_item['Type'] = lexical_item['Classification']
        type_control_stack.append(lexical_item)
        lexical_item = next()
    elif (lexical_item['Token'].lower() == 'not'):
        lexical_item = next()
        factor()
        lexical_item = lexical_dict[current_id]
    elif (lexical_item['Token'].lower() == '('):
        lexical_item = next()
        expression()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == ')'):
            lexical_item = next()
        else:
            lexical_item = lexical_dict[current_id]
            raise Exception('factor, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting ")" but came: '
                            + '"'
                            + lexical_item['Token'] + '"')
    else:
        lexical_item = lexical_dict[current_id]
        raise Exception('factor, in line ' + str(lexical_item['Line']) + ' \n'
                        + 'error, waiting "factor item" but came: '
                        + '"'
                        + lexical_item['Token'] + '"')


def termLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Multiplicative Operator'):
        multiplicativeOp()
        factor()

        print('--------- Multiplicative type control stack ----------')
        for element in type_control_stack:
            print(element)
        print('---------------------------------------')

        updateTCS()

        print('--------- Multiplicative deleted type control stack ----------')
        for element in type_control_stack:
            print(element)
        print('---------------------------------------')

        termLine()
    else:
        pass


def term():
    factor()
    termLine()


def simpleExpressionLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Additive Operator'):
        AdditiveOp()
        term()

        print('--------- Additive type control stack ----------')
        for element in type_control_stack:
            print(element)
        print('---------------------------------------')

        updateTCS()

        print('--------- Additive deleted type control stack ----------')
        for element in type_control_stack:
            print(element)
        print('---------------------------------------')

        simpleExpressionLine()
    else:
        pass


def simpleExpression():
    sign()
    term()
    simpleExpressionLine()


def expressionC():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Relational Operator'):
        relationalOp()
        simpleExpression()

        updateTCS(type='relationalOp')

        print('--------- Relational type control stack ----------')
        for element in type_control_stack:
            print(element)
        print('---------------------------------------')
        # exit()
    else:
        pass


def expression():
    simpleExpression()
    expressionC()

    print('--------- expression type control stack ----------')
    for element in type_control_stack:
        print(element)
    print('---------------------------------------')

    # if (len(type_control_stack) > 1):
    #     updateTCS()

    print('--------- expression deleted type control stack ----------')
    for element in type_control_stack:
        print(element)
    print('---------------------------------------')


def expressionsListLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == ','):
        lexical_item = next()
        expression()
        expressionsListLine()
    else:
        pass


def expressionsList():
    expression()
    expressionsListLine()


def procedureActivationC():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == '('):
        lexical_item = next()
        expressionsList()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == ')'):
            lexical_item = next()
        else:
            raise Exception('procedureActivationC, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting ")" but came: '
                            + '"'
                            + lexical_item['Token'] + '"')
    else:
        pass


def procedureActivation():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):

        if (declaration_key == 0):
            symbolsStack.push(lexical_item)
        else:
            symbolsStack.search(lexical_item)

        lexical_item = next()
        procedureActivationC()


def variable():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):

        if (declaration_key == 0):
            symbolsStack.push(lexical_item)
        else:
            symbolsStack.search(lexical_item)
            # print('variable' + str(lexical_item))
            # print(symbolsStack.getProgramTokens())

        lexical_item = next()
    else:
        pass


def partElse():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'else'):
        lexical_item = next()
        command()
    else:
        pass


def command():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):
        variable()
        procedureActivationC()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'] == ':='):
            lexical_item = next()
            expression()
            # Assignment Command: atributes result to identifier here
            print('--------- Assignment Command type control stack ----------')
            for element in type_control_stack:
                print(element)
            print('---------------------------------------')

            updateTCS()

            print('--------- Additive deleted type control stack ----------')
            for element in type_control_stack:
                print(element)
            print('---------------------------------------')
            return

        print('--------- Procedure type control stack ----------')
        for element in type_control_stack:
            print(element)
        print('---------------------------------------')

        updateTCS()

        print('--------- Procedure deleted type control stack ----------')
        for element in type_control_stack:
            print(element)
        print('---------------------------------------')
        return
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'if'):
        lexical_item = next()
        expression()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == 'then'):
            lexical_item = next()
            command()  # or better commandsList()
            partElse()
            return
        else:
            lexical_item = lexical_dict[current_id]
            raise Exception('command, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting "then" but came: '
                            + '"'
                            + lexical_item['Token'] + '"')
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'while'):
        lexical_item = next()
        expression()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == 'do'):
            lexical_item = next()
            command()
            return
        else:
            lexical_item = lexical_dict[current_id]
            raise Exception('command, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting "do" but came: '
                            + '"'
                            + lexical_item['Token'] + '"')
    compositeCommand()


def commandsListLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == ';'):
        lexical_item = next()
        command()
        commandsListLine()
    else:
        pass


def commandsList():
    command()
    commandsListLine()


def optionalCommands():
    commandsList()


def compositeCommand():
    global declaration_key
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'begin'):
        declaration_key += 1
        lexical_item = next()
        optionalCommands()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == 'end'):
            declaration_key -= 1
            if (declaration_key == 0):
                symbolsStack.closeScope()
            lexical_item = next()
        else:
            if (lexical_item['Classification'] == 'Identifier' or lexical_item['Classification'] == 'Reserved Word'):
                raise Exception('compositeCommand, in line ' + str(lexical_item['Line'] - 1) + ' \n'
                                + 'error, waiting ";" but came: '
                                + '"'
                                + lexical_item['Token'] + '"')
            raise Exception('compositeCommand, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting closing the composite command "end" but came: '
                            + '"'
                            + lexical_item['Token'] + '"')


def listOfParametersLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == ';'):
        lexical_item = next()
        listOfParameters()


def listOfParameters():
    listOfIdentifiers()
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == ':'):
        lexical_item = next()
        type()
        listOfParametersLine()
    else:
        raise Exception('listOfParameters, in line ' + str(lexical_item['Line']) + ' \n'
                        + 'error, waiting ":" but came: '
                        + '"'
                        + lexical_item['Token'] + '"')


def arguments():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == '('):
        lexical_item = next()
        listOfParameters()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == ')'):
            lexical_item = next()
        else:
            raise Exception('arguments, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting ")" but came: '
                            + '"'
                            + lexical_item['Token'] + '"')
    else:
        pass


def subprogramDeclaration():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'procedure'):
        lexical_item = next()
        if (lexical_item['Classification'] == 'Identifier'):

            if (declaration_key == 0):
                lexical_item['Type'] = 'procedure'
                symbolsStack.push(lexical_item)
                symbolsStack.push(
                    {'Token': '$', 'Classification': 'initMark', 'Line': lexical_item['Line']})
            else:
                symbolsStack.search(lexical_item)

            lexical_item = next()
            arguments()
            lexical_item = lexical_dict[current_id]
            if (lexical_item['Token'].lower() == ';'):
                lexical_item = next()
                variableDeclarations()
                subprogramsDeclarations()
                compositeCommand()
            else:
                raise Exception('subprogramDeclaration, in line ' + str(lexical_item['Line']) + ' \n'
                                + 'error, waiting ";" but came: '
                                + '"'
                                + lexical_item['Token'] + '"')
        else:
            raise Exception('subprogramDeclaration, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting "Identifier" but came: '
                            + '"'
                            + lexical_item['Classification'] + '"')
    else:
        pass


def subprogramsDeclarationsLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == 'procedure'):
        subprogramDeclaration()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'] == ';'):
            lexical_item = next()
            subprogramsDeclarationsLine()
        else:
            raise Exception('subprogramsDeclarationsLine in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, end of procedure declaration: waiting ";" but came: '
                            + '"'
                            + lexical_item['Token'] + '"')
    else:
        pass


def subprogramsDeclarations():
    subprogramsDeclarationsLine()


def type():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'integer'
        or lexical_item['Token'].lower() == 'real'
        or lexical_item['Token'].lower() == 'char'
            or lexical_item['Token'].lower() == 'boolean'):

        symbolsArray = symbolsStack.get().copy()
        for i in range(0, len(symbolsArray)):
            if ('Type' in symbolsArray[i]
                    and symbolsArray[i]['Type'] == 'Mark'):
                symbolsStack.setType(i, lexical_item['Token'])
        # print(symbolsStack.getProgramTokens())

        lexical_item = next()

    else:
        raise Exception('type, in line ' + str(lexical_item['Line']) + ' \n'
                        + 'error, invalid type: '
                        + '"'
                        + lexical_item['Token'] + '"')


def listOfIdentifiersLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == ','):
        lexical_item = next()
        if (lexical_item['Classification'] == 'Identifier'):

            if (declaration_key == 0):
                lexical_item['Type'] = 'Mark'
                symbolsStack.push(lexical_item)
                identifier_stack.append(lexical_item['Token'])
            else:
                symbolsStack.search(lexical_item)

            lexical_item = next()
            listOfIdentifiersLine()
        else:
            raise Exception('listOfIdentifiersLine, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting "Identifier" but came: '
                            + '"'
                            + lexical_item['Classification'] + '"')
    else:
        pass


def listOfIdentifiers():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):

        if (declaration_key == 0):
            lexical_item['Type'] = 'Mark'
            symbolsStack.push(lexical_item)
            identifier_stack.append(lexical_item['Token'])
        else:
            symbolsStack.search(lexical_item)

        lexical_item = next()
        listOfIdentifiersLine()
    else:
        raise Exception('listOfIdentifiers, in line ' + str(lexical_item['Line']) + ' \n'
                        + 'error, waiting "Identifier" but came: '
                        + '"'
                        + lexical_item['Classification'] + '"')


def listVariableDeclarationsLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):
        listOfIdentifiers()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'] == ':'):
            lexical_item = next()
            type()
            # always get the changes after productions
            lexical_item = lexical_dict[current_id]
            if (lexical_item['Token'] == ';'):
                lexical_item = next()
                listVariableDeclarationsLine()
            else:
                raise Exception('listVariableDeclarationsLine, in line ' + str(lexical_item['Line']) + ' \n'
                                + 'error, waiting ";" but came: '
                                + '"'
                                + lexical_item['Token'] + '"')
        else:
            raise Exception('listVariableDeclarationsLine, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting ":" but came: '
                            + '"'
                            + lexical_item['Token'] + '"')
    else:
        pass


def listVariableDeclarations():
    listOfIdentifiers()
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == ':'):
        lexical_item = next()
        type()
        # always get the changes after productions
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'] == ';'):
            lexical_item = next()
            listVariableDeclarationsLine()
        else:
            raise Exception('listVariableDeclarations, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting ";" but came: '
                            + '"'
                            + lexical_item['Token'] + '"')
    else:
        raise Exception('listVariableDeclarations, in line ' + str(lexical_item['Line']) + ' \n'
                        + 'error, waiting ":" but came: '
                        + '"'
                        + lexical_item['Token'] + '"')


def variableDeclarations():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'var'):
        lexical_item = next()
        listVariableDeclarations()
    else:
        pass


def program():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'program'):
        symbolsStack.push(
            {'Token': '$', 'Classification': 'initMark', 'Line': lexical_item['Line']})
        lexical_item = next()
        if (lexical_item['Classification'] == 'Identifier'):

            if (declaration_key == 0):
                lexical_item['Type'] = 'program'
                symbolsStack.push(lexical_item)
                # print(symbolsStack.getProgramTokens())
            else:
                symbolsStack.search(lexical_item)

            lexical_item = next()
            if (lexical_item['Token'] == ';'):
                lexical_item = next()
                variableDeclarations()
                subprogramsDeclarations()
                compositeCommand()
                # always get the changes after productions
                lexical_item = lexical_dict[current_id]
                if (lexical_item['Token'] != '.'):
                    raise Exception('program, in line ' + str(lexical_item['Line']) + ' \n'
                                    + 'error, waiting "." but came: '
                                    + '"'
                                    + lexical_item['Token'] + '"')

            else:
                raise Exception('program, in line ' + str(lexical_item['Line']) + ' \n'
                                + 'error, waiting ";" but came: '
                                + '"'
                                + lexical_item['Token'] + '"')
        else:
            raise Exception('program, in line ' + str(lexical_item['Line']) + ' \n'
                            + 'error, waiting "Identifier" but came: '
                            + '"'
                            + lexical_item['Classification'] + '"')

    else:
        raise Exception('program, in line ' + str(lexical_item['Line']) + ' \n'
                        + 'error, waiting "program" but came: '
                        + '"'
                        + lexical_item['Token'] + '"')


def runSyntacticAnalysis(current_dict):
    global current_id, lexical_dict, symbolsStack, declaration_key, type_control_stack, identifier_stack
    lexical_dict = current_dict

    program()
    print('Syntactic Analysis SUCCESS! finished!')

    # for element in type_control_stack:
    #     print(element)
