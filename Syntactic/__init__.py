import sys
sys.tracebacklimit = 0

current_id = 0
lexical_dict = dict()


def next():
    global current_id, lexical_dict
    current_id += 1
    return lexical_dict[current_id]


def type():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'integer'
        or lexical_item['Token'].lower() == 'real'
            or lexical_item['Token'].lower() == 'boolean'):
        lexical_item = next()
    else:
        raise Exception(
            'Error: tipo inválido: ' + lexical_item['Token'])


def listOfParameters2():
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
        listOfParameters2()
    else:
        raise Exception('Error: Esperando delimitador ":" veio: ' +
                        lexical_item['Token'])


def arguments():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == '('):
        lexical_item = next()
        listOfParameters()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == ')'):
            lexical_item = next()
        else:
            raise Exception('Error: Esperando ")" veio: ' +
                            lexical_item['Token'])


def relationalOp():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == '='
            or lexical_item['Token'] == '<'
            or lexical_item['Token'] == '>'
            or lexical_item['Token'] == '<='
            or lexical_item['Token'] == '>='
            or lexical_item['Token'] == '<>'):
        lexical_item = next()


def factorC():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == '('):
        lexical_item = next()
        expressionsList()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == ')'):
            lexical_item = next()
        else:
            raise Exception('Error: Esperando ")" veio: ' +
                            lexical_item['Token'])
    else:
        pass


def factor():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):
        lexical_item = next()
        factorC()
        lexical_item = lexical_dict[current_id]
    elif (lexical_item['Token'].isdigit()
          or lexical_item['Token'].isdigit()
          or lexical_item['Token'].lower() == 'true'
          or lexical_item['Token'].lower() == 'false'):
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
            raise Exception('Error at factor Esperando ")" veio: ' +
                            lexical_item['Token'])


def multiplicativeOp():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == '+' or lexical_item['Token'] == '-' or lexical_item['Token'].lower() == 'and'):
        lexical_item = next()
    else:
        pass


def termLine():
    multiplicativeOp()
    factor()
    termLine()


def term():
    factor()
    # termLine()


def sign():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == '+' or lexical_item['Token'] == '-'):
        lexical_item = next()
    else:
        pass


def opAdditive():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == '+' or lexical_item['Token'] == '-' or lexical_item['Token'].lower() == 'or'):
        lexical_item = next()
    else:
        pass


def simpleExpressionLine():
    opAdditive()
    term()


def simpleExpression():
    term()
    sign()
    term()
    simpleExpressionLine()


def expressionC():
    relationalOp()
    simpleExpression()


def expression():
    simpleExpression()
    expressionC()


def expressionsListLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == ','):
        lexical_item = next()
        expression()
        expressionsListLine()
    else:
        pass


def expressionsList():
    # removes left recursion
    expression()
    expressionsListLine()


def variable():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):
        lexical_item = next()


def procedureActivationC():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == '('):
        lexical_item = next()
        expressionsList()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == ')'):
            lexical_item = next()
        else:
            raise Exception('Error: Esperando ")" veio: ' +
                            lexical_item['Token'])


def procedureActivation():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):
        lexical_item = next()
        procedureActivationC()


def partElse():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'else'):
        lexical_item = next()
        command()


def command():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):
        variable()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'] == ':='):
            lexical_item = next()
            expression()
            procedureActivation()
            compositeCommand()
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'if'):
        lexical_item = next()
        expression()
        lexical_item = lexical_dict[current_id]

        if (lexical_item['Token'].lower() == 'then'):
            lexical_item = next()
            command()
            partElse()
        else:
            raise Exception('Error: Esperando "then" veio: ' +
                            lexical_item['Token'])
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'while'):
        lexical_item = next()
        expression()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == 'do'):
            lexical_item = next()
            command()
        else:
            raise Exception('Error: Esperando "do" veio: ' +
                            lexical_item['Token'])


def commandsListLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == ';'):
        lexical_item = next()
        command()
    else:
        # pass
        raise Exception('Error at ' + str(lexical_item['Line']) + ' esperando ";" veio: ' +
                        lexical_item['Token'])


def commandsList():
    command()
    commandsListLine()


def optionalCommands():
    commandsList()


def compositeCommand():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'begin'):
        lexical_item = next()
        optionalCommands()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == 'end'):
            lexical_item = next()
        else:
            raise Exception('Error in line ' + str(lexical_item['Line']) + ' esperando o fechamento do comando composto "end", veio: ' +
                            lexical_item['Token'])


def subprogramDeclaration():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'procedure'):
        lexical_item = next()
        if (lexical_item['Classification'] == 'Identifier'):
            lexical_item = next()
            arguments()
            lexical_item = lexical_dict[current_id]
            if (lexical_item['Token'].lower() == ';'):
                lexical_item = next()
                variableDeclarations()
                subprogramsDeclarations()
                compositeCommand()
            else:
                raise Exception('Error: Esperando ; veio: ' +
                                lexical_item['Token'])
        else:
            raise Exception(
                'Error: sintático, esperando um identificador veio: ' + lexical_item['Token'])
    else:
        pass


def subprogramsDeclarationsLine():
    subprogramDeclaration()
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == ';'):
        lexical_item = next()
        subprogramsDeclarationsLine()
    else:
        pass


def subprogramsDeclarations():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == 'procedure'):
        subprogramsDeclarationsLine()
    else:
        pass


def listOfIdentifiers2():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == ','):
        lexical_item = next()
        if (lexical_item['Classification'] == 'Identifier'):
            lexical_item = next()
            listOfIdentifiers2()
        else:
            raise Exception(
                'Error: sintático, esperando um identificador veio: ' + lexical_item['Token'])
    else:
        pass


def listOfIdentifiers():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):
        lexical_item = next()
        listOfIdentifiers2()
    else:
        raise Exception(
            'Error: sintático, esperando um identificador veio: ' + lexical_item['Classification'])


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
                raise Exception('Error: Esperando ; veio: ' +
                                lexical_item['Token'])
        else:
            raise Exception('Error: Esperando delimitador ":" veio: ' +
                            lexical_item['Token'])
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
            raise Exception('Error in listVariableDeclarations: Esperando ; veio: ' +
                            lexical_item['Token'])
    else:
        raise Exception('Error in listVariableDeclarations: Esperando delimitador ":" veio: ' +
                        lexical_item['Token'])


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
        lexical_item = next()
        if (lexical_item['Classification'] == 'Identifier'):
            lexical_item = next()
            if (lexical_item['Token'] == ';'):
                lexical_item = next()
                variableDeclarations()
                # always get the changes after productions
                lexical_item = lexical_dict[current_id]
                subprogramsDeclarations()
                # always get the changes after productions
                lexical_item = lexical_dict[current_id]
                compositeCommand()
                lexical_item = lexical_dict[current_id]
                if (lexical_item['Token'] != '.'):
                    raise Exception(
                        'Error: Esperando delimitador "." veio: ' + lexical_item['Token'])
            else:
                raise Exception('Error: Esperando ; veio: ' +
                                lexical_item['Token'])
        else:
            raise Exception(
                'Error: sintático, esperando um identificador veio: ' + lexical_item['Classification'])
    else:
        raise Exception(
            'Error: Esperando palavra reservada program, veio: ' + lexical_item['Token'])


def runSyntacticAnalysis(current_dict):
    global current_id, lexical_dict
    lexical_dict = current_dict
    program()
