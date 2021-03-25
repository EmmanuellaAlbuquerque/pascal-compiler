from Lexical import runLexicalAnalysis
from Syntactic import runSyntacticAnalysis

lexical_dict = runLexicalAnalysis()

runSyntacticAnalysis(lexical_dict)
