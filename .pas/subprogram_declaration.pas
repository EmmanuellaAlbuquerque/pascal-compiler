program teste;
var {-- variableDeclarations}
  valor1: integer;
  valor2: real;
procedure argTeste(a, b: integer; c, d: real); {-- subprogramDeclaration, arguments}
var
  afterprocedure1, afterprocedure2: integer; {-- listOfParameters}
  afterprocedure3: real;
procedure argTeste2(e, f: integer; g, h: real);
begin {-- compositeCommand}
  a := a; {-- commandsList}
  b := b;
end;
begin
{
  e := e; -- optionalCommands
  f := f;
}
end;
begin 
  valor1 := 10 * 2 * 3;
  valor2 := 10.5 / 1;
end.