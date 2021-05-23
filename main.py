import os.path
from Lexical import Lexical
from Syntactic import runSyntacticAnalysis

path_directory = os.path.dirname(os.path.abspath(__file__))

path_filename = path_directory + \
    os.path.join("/.pas", 'ex_procedure.pas')

# path_filename = path_directory + \
#     os.path.join("/Semantic/SimulatingErrors/", '2d2.pas')

# path_filename = path_directory + \
#     os.path.join("/Semantic/", 'TcS-Semantic.pas')

lexical = Lexical(path_filename)
lexical_dict = lexical.runLexicalAnalysis()

runSyntacticAnalysis(lexical_dict)
