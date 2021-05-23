program exProcedure;
var
   a, b, c, min, m, z: integer;
procedure findMin(x, y, z: integer; m: real);

begin
   if (x < y) then
      m:= x
   else
      m:= y + findMin;
   
   if (z < m) then
      m:= z;


   while (z < m) do
   begin
      m:= z;
   end;
end;

begin
   m:= z;
end.