from Lexical import Lexical
from Syntactic import runSyntacticAnalysis


lexical = Lexical('subprogram_declaration.pas')
lexical_dict = lexical.runLexicalAnalysis()

runSyntacticAnalysis(lexical_dict)
