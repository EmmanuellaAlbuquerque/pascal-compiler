import sys
sys.tracebacklimit = 0

current_id = 0
lexical_dict = dict()


def next():
    global current_id, lexical_dict
    current_id += 1
    return lexical_dict[current_id]


def variableDeclarations():
    print('----')


def program():
    lexical_item = lexical_dict[current_id]
    if (lexical_item['Token'] == 'program'):
        lexical_item = next()
        if (lexical_item['Classification'] == 'Identifier'):
            lexical_item = next()
            if (lexical_item['Token'] == ';'):
                lexical_item = next()
                variableDeclarations()
                # Dec_Subp()
                # Com_Com()
                if (lexical_item['Token'] != '.'):
                    raise Exception(
                        'Error: Esperando delimitador "." veio: ' + lexical_item['Token'])
            else:
                raise Exception('Error: Esperando ;, veio: ' +
                                lexical_item['Token'])
        else:
            raise Exception('Error: sintático ', + lexical_item['Token'])
    else:
        raise Exception(
            'Error: Esperando palavra reservada program, veio ' + lexical_item['Token'])


def runSyntacticAnalysis(current_dict):
    global current_id, lexical_dict
    lexical_dict = current_dict
    program()
