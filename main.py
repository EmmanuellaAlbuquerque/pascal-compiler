from Lexical import Lexical
from Syntactic import runSyntacticAnalysis


lexical = Lexical('signal.pas')
lexical_dict = lexical.runLexicalAnalysis()

runSyntacticAnalysis(lexical_dict)
