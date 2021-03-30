from Lexical import Lexical
from Syntactic import runSyntacticAnalysis


lexical = Lexical('ex_procedure.pas')
lexical_dict = lexical.runLexicalAnalysis()

runSyntacticAnalysis(lexical_dict)
