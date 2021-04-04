program lexicalTest;
{
  programa de teste:
  nome: LexicalTest
}
var
Valor_1, Valor_Dois, result: integer;
Valor_3: real;
btrue, bfalse, bResult : boolean;

Begin
  Valor_1 := 100;
  Valor_Dois := 10 * 1;
  Valor_3 := 100.10 / 1;
  btrue := true;
  bfalse := false;

  Valor_Dois := (-10) + (-120);

  if Valor_1 = Valor_Dois then
    result := Valor_1;

  if Valor_1 < Valor_Dois then
    result := Valor_1;

  if Valor_1 > Valor_Dois then
    result := Valor_1;

  if ( Valor_1 <= Valor_Dois ) then
    result := Valor_1;

  if ( Valor_1 >= Valor_Dois ) then
    result := Valor_1;
        
  if ( Valor_1 <> Valor_Dois ) then
    result := Valor_1;

  if  (bfalse or bfalse) then
    bresult := true;

  if (btrue and bfalse) then
    bresult := true;
End.