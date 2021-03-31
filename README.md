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