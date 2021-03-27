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


def compositeCommand():
    print('------')


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
        raise Exception('Error: Esperando "procedure" veio: ' +
                        lexical_item['Token'])


def subprogramsDeclarationsLine():
    subprogramDeclaration()
    lexical_item = lexical_dict[current_id]
    print(lexical_item)
    if (lexical_item['Token'] == ';'):
        lexical_item = next()
        subprogramsDeclarationsLine()
    else:
        raise Exception('Error: Esperando ; veio: ' +
                        lexical_item['Token'])


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
    # print(lexical_item)
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
                # Com_Com()
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
