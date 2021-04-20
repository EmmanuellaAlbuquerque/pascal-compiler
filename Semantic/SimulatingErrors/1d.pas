{ 
  1. D
  Identificadores de procedimento seguem as regras gerais das variáveis.
}
Program exemplo;
  var a,b: integer; 
  boolean_value: boolean;
  procedure p (x: integer);
    var b,c: integer;
    procedure q (x: integer); {declaração em outro escopo}
      var h: integer;
      begin
        h := 10;
    end;
    begin
        b := x + a;
    end;
  procedure q (x: integer);
    var h: integer;
    begin
      h := 10;
    end;
  procedure p (x: integer); {redeclaração de p}
    var h: integer;
    begin
      h := 10;
    end;
begin

end.