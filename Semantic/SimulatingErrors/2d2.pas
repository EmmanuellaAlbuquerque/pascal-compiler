{ 
  2. D parte 2
  Operações lógicas só podem ser realizadas entre valores 
  booleanos. 
}
Program exemplo;
  var a,b: integer; 
  boolean_value: boolean;
  procedure p (x: integer);
    var b,c: integer;
    begin
      {boolean_value := 10.5 or 10.8; -- or: real x real }
      {boolean_value := 1 or 1; -- or: integer x integer}
      {boolean_value := 10.9 or 1; -- or: integer x real}
      {boolean_value := 1 or 11.5; -- or: real x integer}

      {boolean_value := 10.5 and 10.8; -- and: real x real}
      {boolean_value := 1 and 1; -- and: integer x integer}
      {boolean_value := 10.9 and 1; -- and: integer x real}
      boolean_value := 1 and 11.5; {-- and: integer x real}
      if (1 and 1) then
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