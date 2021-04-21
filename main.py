import os.path
from Lexical import Lexical
from Syntactic import runSyntacticAnalysis

path_directory = os.path.dirname(os.path.abspath(__file__))

# path_filename = path_directory + \
#     os.path.join("/.pas", 'example.pas')

# path_filename = path_directory + \
#     os.path.join("/Semantic/SimulatingErrors/", '2d.pas')

path_filename = path_directory + \
    os.path.join("/Semantic/", 'TcS-Semantic.pas')

lexical = Lexical(path_filename)
lexical_dict = lexical.runLexicalAnalysis()

runSyntacticAnalysis(lexical_dict)
