program additive_operators;
var
a,b,result : integer;
ttrue, tfalse, tresult: boolean;

begin
   a := 20;
   b := 50;
   ttrue := true;
   tfalse := false;

   result := a + b;

   result := a - b;

   if  (tfalse or tfalse) then
      tresult := true
   
end.