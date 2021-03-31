# Analisador Léxico

...


# Analisador Sintático
## Método Top-Down com análise preditiva recursiva direta

### Eliminar:
- [ ] recursão a esquerda
- [x] recursão da linguagem
- [ ] não determinismo

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
```pascal

{--------------------------------------------------------------------------}

programa →
  program id;
  declarações_variáveis
  declarações_de_subprogramas
  comando_composto
  .

{--------------------------------------------------------------------------}

declarações_variáveis →
  var lista_declarações_variáveis
  | ε

{--------------------------------------------------------------------------}

{modificado}
lista_declarações_variáveis →
  lista_de_identificadores: tipo; lista_declarações_variáveis'             '

lista_declarações_variáveis' →                                             '
  lista_de_identificadores: tipo; lista_declarações_variáveis'             '
  | ε

{--------------------------------------------------------------------------}

{modificado}
lista_de_identificadores →
  id lista_de_identificadores'                                             '

lista_de_identificadores' →                                                '
  , id lista_de_identificadores'                                           '
  | ε

{--------------------------------------------------------------------------}

tipo →
  integer
  | real
  | boolean

{--------------------------------------------------------------------------}

{modificado}
declarações_de_subprogramas →
  declarações_de_subprogramas'                                             '

declarações_de_subprogramas' →                                             '
  declaração_de_subprograma; declarações_de_subprogramas'                  '
  | ε

{--------------------------------------------------------------------------}

declaração_de_subprograma →
  procedure id argumentos;
  declarações_variáveis
  declarações_de_subprogramas
  comando_composto

{--------------------------------------------------------------------------}

argumentos →
  (lista_de_parametros)
  | ε

{--------------------------------------------------------------------------}

{modificado}
lista_de_parametros →
  lista_de_identificadores: tipo lista_de_parametros'                      '

lista_de_parametros' →                                                     '
  ; lista_de_identificadores: tipo lista_de_parametros'                    '

{--------------------------------------------------------------------------}

comando_composto →
  begin
  comandos_opcionais
  end

{--------------------------------------------------------------------------}

comandos_opcionais →
  lista_de_comandos
  | ε

{--------------------------------------------------------------------------}

{modificado}
lista_de_comandos →
  comando lista_de_comandos'                                               '
  

lista_de_comandos' →                                                       '
  ; comando lista_de_comandos'                                             '
  | ε

{--------------------------------------------------------------------------}

comando →
  variável := expressão
  | ativação_de_procedimento
  | comando_composto
  | if expressão then comando parte_else
  | while expressão do comando 

{--------------------------------------------------------------------------}

parte_else →
  else comando
  | ε

{--------------------------------------------------------------------------}

variável →
  id

{--------------------------------------------------------------------------}

{modificado}
ativação_de_procedimento →
  id ativação_de_procedimentoC

ativação_de_procedimentoC →
  ε
  |(lista_de_expressões)

{--------------------------------------------------------------------------}

{modificado}
lista_de_expressões →
  expressão lista_de_expressões'                                           '

lista_de_expressões' →                                                     '
  , expressão lista_de_expressões'                                         '
  | ε

{--------------------------------------------------------------------------}

{modificado}
expressão →
  expressão_simples expressãoC

expressãoC →
  ε
  | op_relacional expressão_simples

{--------------------------------------------------------------------------}

{modificado}
expressão_simples →
  termo expressão_simples'                                                 '

expressão_simples' →                                                       '
  op_aditivo termo expressão_simples'                                      '
  | ε

{--------------------------------------------------------------------------}

{modificado}
termo →
  fator termo'                                                             '

termo' →                                                                   '
  op_multiplicativo fator termo'                                           '
  | ε

{--------------------------------------------------------------------------}
















```