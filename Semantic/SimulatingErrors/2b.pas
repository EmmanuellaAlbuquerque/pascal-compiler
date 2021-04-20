{ 
  1. B
  Devem ser identificadas atribuições e inicializações inválidas de variáveis. 
  Por exemplo, variáveis do tipo boolean recebendo números. 
}
Program exemplo;
  var isBoolean: boolean; 
begin
  isBoolean := 10;
end.