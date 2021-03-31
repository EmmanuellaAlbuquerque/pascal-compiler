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
  E := E + T| T     -     E → TE'
                    -     E' → +TE'| ε
```
2. Retirar não determinismo: 
```text
  A → αβ    |   A → αC
  A → αγ    |   C → β/γ
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
  lista_de_identificadores: tipo; lista_declarações_variáveis'

lista_declarações_variáveis' →
  lista_de_identificadores: tipo; lista_declarações_variáveis'
  | ε

{--------------------------------------------------------------------------}

{modificado}
lista_de_identificadores →
  id lista_de_identificadores'

lista_de_identificadores' →
  , id lista_de_identificadores'
  | ε

{--------------------------------------------------------------------------}

tipo →
  integer
  | real
  | boolean

{--------------------------------------------------------------------------}

{modificado}
declarações_de_subprogramas →
  declarações_de_subprogramas'

declarações_de_subprogramas' →
  declaração_de_subprograma; declarações_de_subprogramas'
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
  lista_de_identificadores: tipo lista_de_parametros'

lista_de_parametros' →
  ; lista_de_identificadores: tipo lista_de_parametros'

```