import sys
sys.tracebacklimit = 0

current_id = 0
lexical_dict = dict()


def next():
    global current_id, lexical_dict
    current_id += 1
    return lexical_dict[current_id]


def multiplicativeOp():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == '*' or lexical_item['Token'] == '/' or lexical_item['Token'].lower() == 'and'):
        lexical_item = next()
    else:
        lexical_item = lexical_dict[current_id]
        raise Exception('Error: Esperando multiplicativeOp veio: ' +
                        lexical_item['Token'] + ' in line ' + str(lexical_item['Line']))


def AdditiveOp():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == '+' or lexical_item['Token'] == '-' or lexical_item['Token'].lower() == 'or'):
        lexical_item = next()
    else:
        lexical_item = lexical_dict[current_id]
        raise Exception('Error: Esperando opAdditive veio: ' +
                        lexical_item['Token'] + ' in line ' + str(lexical_item['Line']))


def relationalOp():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == '='
            or lexical_item['Token'] == '<'
            or lexical_item['Token'] == '>'
            or lexical_item['Token'] == '<='
            or lexical_item['Token'] == '>='
            or lexical_item['Token'] == '<>'):
        lexical_item = next()
    else:
        raise Exception('Error: Esperando Relational Operator veio: ' +
                        lexical_item['Classification'])


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
          or lexical_item['Token'].replace(".", "").isdigit()
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
    else:
        lexical_item = lexical_dict[current_id]
        raise Exception('Error: Esperando factor veio: ' +
                        lexical_item['Token'] + ' in line ' + str(lexical_item['Line']))


def termLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Multiplicative Operator'):
        multiplicativeOp()
        factor()
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
    else:
        pass


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
            raise Exception('Error: Esperando ")" veio: ' +
                            lexical_item['Token'])
    else:
        pass


def procedureActivation():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):
        lexical_item = next()
        procedureActivationC()


def variable():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):
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

            lexical_item = lexical_dict[current_id]
            return
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'].lower() == 'if'):
        lexical_item = next()
        expression()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == 'then'):
            lexical_item = next()
            command()
            partElse()
            return
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
            return
        else:
            raise Exception('Error: Esperando "do" veio: ' +
                            lexical_item['Token'])
    compositeCommand()


def commandsListLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == ';'):
        lexical_item = next()
        command()
        commandsListLine()
    else:
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'].lower() == 'end'):
            lexical_item = lexical_dict[current_id]
        else:
            lexical_item = lexical_dict[current_id - 1]
            raise Exception('Error at ' + str(lexical_item['Line'] - 1) + ' esperando ";" veio: ' +
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
    else:
        pass


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
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == 'procedure'):
        subprogramDeclaration()
        lexical_item = lexical_dict[current_id]
        if (lexical_item['Token'] == ';'):
            lexical_item = next()
            subprogramsDeclarationsLine()
        else:
            raise Exception('line ' + str(lexical_item['Line']) + ' \n'
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
            or lexical_item['Token'].lower() == 'boolean'):
        lexical_item = next()
    else:
        raise Exception(
            'Error: tipo inválido: ' + lexical_item['Token'])


def listOfIdentifiersLine():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == ','):
        lexical_item = next()
        if (lexical_item['Classification'] == 'Identifier'):
            lexical_item = next()
            listOfIdentifiersLine()
        else:
            raise Exception(
                'Error: sintático, esperando um identificador veio: ' + lexical_item['Token'])
    else:
        pass


def listOfIdentifiers():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Classification'] == 'Identifier'):
        lexical_item = next()
        listOfIdentifiersLine()
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
                subprogramsDeclarations()
                compositeCommand()
                # always get the changes after productions
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
    print('OK. Syntactic Analysis SUCCESS finished!')
