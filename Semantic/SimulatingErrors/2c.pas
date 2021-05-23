{ 
  2. C
  Operações aritméticas:
  V3 := V1 op V2
}
Program exemplo;
  {var v1, v2, v3: integer;} {Integer Integer Integer: OK}

  var v1, v3: integer; v2: real; {Integer Real Integer Inválido}
  {var v2, v3: integer; v1: real;} {Real Integer Integer Inválido}
  {var v1, v2: real; v3: integer;} {Real Real Integer Inválido}

  {var v1, v2: integer; v3: real;} {Integer Integer Real OK}
  {var v2, v3: real; v1: integer;} {Integer Real Real OK}
  {var v1, v3: real; v2: integer;} {Real Integer Real OK}
  {var v1, v2, v3: real;} {Real Real Real OK}

  {var v1, v2, v3: boolean;}
begin
  v3 := v1 + v2;
end.