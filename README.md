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

### Algoritmo
1. **:heavy_check_mark: Leia a entrada até o fim ou quando nenhuma transição é possível**
2. **:heavy_check_mark: Se o estado corrente for final**
    2.1 Retorne o token e o seu tipo
3. **:heavy_check_mark: Se o estado corrente for não-final**
    3.1 Voltar para último estado aceitável
    3.2 Retornar o token e o tipo deste estado
    3.4 Devolver os caracteres lidos deste ponto em diante para a entrada
4. **:heavy_check_mark: Se a entrada não acabou, reinicie o autômato**

# Analisador Sintático
## Método Top-Down com análise preditiva recursiva direta

Para remover as ambiguidades, devemos reescrever as expressões gramaticais ambíguas:
ex.: da precedência de operadores
### Eliminar:
- [x] recursão a esquerda
- [x] recursão da linguagem
- [x] não determinismo

### Produções e mudanças

#### Regras utilizadas
1. Retirar recursão a esquerda
```text
  A := Aα| β     --\     A := βA'
                 --/     A' := αA'| ε
```
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

### Verificação de Tipos
- [x] Pilha de Controle de Tipos (PcT)
- [x] Expressões Aritméticas
- [x] Comando de Atribuição
- [x] Expressões Relacionais
- [x] Expressões Lógicas
- [x] Compatibilidade de Tipos
