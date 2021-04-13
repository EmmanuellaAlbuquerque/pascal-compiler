from Lexical import Lexical
from Syntactic import runSyntacticAnalysis


lexical = Lexical('example.pas')
lexical_dict = lexical.runLexicalAnalysis()

runSyntacticAnalysis(lexical_dict)
