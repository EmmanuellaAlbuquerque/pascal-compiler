{ 
  2. D parte 1
  Operações relacionais só podem ser realizadas entre valores 
  numéricos.
}
Program exemplo;
  var a,b: integer; 
  boolean_value: boolean;
  procedure p (x: integer);
    var b,c: integer;
    begin
      boolean_value := true > false;
      if (true and false) then
        b := x + a;
      if ((10 > 11) or false) then
        b := x + a;
      boolean_value := 10 > 11;
      boolean_value := 10 + 15 > 11 + 20;
      b := 10 + a * 11;
    end;
  procedure d (x: integer);
    var h: integer;
    begin
      h := 10;
      boolean_value := true;
      p(h);
      boolean_value := false;
    end;
begin

end.