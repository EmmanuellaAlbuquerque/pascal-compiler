## Dupla
Emmanuella Faustino Albuquerque <br>
Vanessa Gabriele Lima Pessoa <br>

# Analisador Léxico

- [x] Tabela de símbolos com os seguintes elementos: <br>
a. Token <br>
b. Tipo de Token <br>
c. Linha correspondente a posição do token <br>

- [x] Não considerar <br>
a. Espaços em branco <br>
b. Caracteres formatadores (tabulação, nova linha, novo parágrafo) <br>

- [x] Comentários {} <br>
a. Contagem de linhas <br>

- [x] Tokens considerados <br>
a. Palavras Chaves <br>
b. Identificadores [a..Z]+ [\w]* <br>
c. Números inteiros [0..9]+ <br>
d. Números reais ([0..9]+.[0..9]*) <br>
e. Delimitadores ; . : ( ) , <br>
f. Comando de atribuição := <br>
e. Operadores relacionais = < > <= >= <> <br>
g. Operadores aditivos + - or <br>
h. Operadores multiplicativos * / and <br>

- [x] Detecção de erros <br>
a. Comentário aberto e não fechado; <br>
b. Símbolos não pertencentes a linguagem. <br>

# Analisador Sintático
## Método Top-Down com análise preditiva recursiva direta

### Eliminar:
- [x] recursão a esquerda
- [x] recursão da linguagem
- [x] não determinismo

### Produções e mudanças

#### Regras utilizadas
1. Retirar recursão a esquerda
```text
  E := E + T| T     --\     E → TE'
                    --/     E' → +TE'| ε
```
2. Retirar não determinismo: 
```text
  A → αβ      --\     A → αC
  A → αγ      --/     C → β|γ
```

#### Especificação da Gramática

[Produções da Gramática](/Syntactic/README.md)

# Analisador Semântico

### Tabela de Símbolos com estrutura de dados destrutiva e com pilha

