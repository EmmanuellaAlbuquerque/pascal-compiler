Program TcS;
  var a,b: integer; 
  boolean_value: boolean;
  procedure p (x: integer);
    var b,c: integer;
    begin
      if (true and false) then { Result 1: Boolean }
        b := x + a; { Result 2: Integer }
      if ((10 > 11) or false) then { Result 3: Boolean}
        b := x + a; { Result 4: Integer }
      boolean_value := 10 > 11; { Result 5: Boolean }
      boolean_value := 10 + 15 > 11 + 20; { Result 6: Boolean }
      b := 10 + a * 11; { Result 7: Integer }
    end;
  procedure d (x: integer);
    var h: integer;
    begin
      h := 10; { Result 8: Integer }
      boolean_value := true; { Result 9: Boolean }
      p(h); { Result 10: void }
      boolean_value := false; { Result 11: Boolean }
    end;
begin

end.