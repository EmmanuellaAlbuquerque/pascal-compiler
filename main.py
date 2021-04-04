from Lexical import Lexical
from Syntactic import runSyntacticAnalysis


lexical = Lexical('test_comments.pas')
lexical_dict = lexical.runLexicalAnalysis()

runSyntacticAnalysis(lexical_dict)
