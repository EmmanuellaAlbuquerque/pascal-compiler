current_id = 0
lexical_dict = dict()


def program():
    print(lexical_dict[current_id])


def runSyntacticAnalysis(current_dict):
    global current_id, lexical_dict
    lexical_dict = current_dict
    program()
