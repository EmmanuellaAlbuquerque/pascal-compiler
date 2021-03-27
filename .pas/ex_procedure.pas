program exProcedure;
var
   a, b, c,  min: integer;
procedure findMin(x, y, z: integer; m: real); 

begin
   if x < y then
      m:= x
   else
      m:= y;
   
   if z < m then
      m:= z;
end;

begin

end.