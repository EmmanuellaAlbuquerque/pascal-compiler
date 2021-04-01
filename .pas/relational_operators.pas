Program relationalOperators;
Var
a, b: integer;
result : boolean;

Begin
   a := 100;
   b := 10;
   
   if a = b then
      result := true;
   
   if  a < b then
      result := true;

   if  a > b then
      result := true;
   
   if ( a <= b ) then
      result := true;
   
   if ( b >= a ) then
      result := true;
         
   if ( a <> b ) then
      result := true;
End.