; ===== TAC  —  inicio de programa =====
x = 5
y = 2.5
mensaje = "Hola mundo"
activo = true
bandera = false
a = 99

; --- func float floatfn ---
begin_func floatfn
return 3.1416
end_func floatfn


; --- func int suma ---
begin_func suma
param_decl int a
param_decl int b
t1 = a + b
return t1
end_func suma


; --- func int doble ---
begin_func doble
param_decl int n
t2 = n * 2
return t2
end_func doble


; --- func bool esMayor ---
begin_func esMayor
param_decl int a
param_decl int b
t3 = a > b
return t3
end_func esMayor


; --- func void saludar ---
begin_func saludar
print "hola soy una funcion void"
end_func saludar


; --- func void saludar2 ---
begin_func saludar2
return "hola soy una funcion void con return"
end_func saludar2

param x
param 3
t4 = call suma, 2
x = t4
print a
t5 = y / 2
y = t5
print x
print mensaje
t6 = x + 1
print t6
t7 = x > 5
t8 = t7 && activo
ifFalse t8 goto L1
print "x es mayor que 5 y activo es true"
goto L2
L1:
print "No se cumplio la condicion"
L2:
t9 = !bandera
t10 = x == 8
t11 = t9 || t10
ifFalse t11 goto L3
print "Prueba de operador logico NOT y OR"
L3:
L4:
t12 = x < 12
ifFalse t12 goto L5
t13 = x + 1
x = t13
print x
goto L4
L5:
x = 0
L6:
t14 = x < 3
ifFalse t14 goto L7
print x
t15 = x + 1
x = t15
goto L6
L7:
param 10
param 20
t16 = call suma, 2
param 4
t17 = call doble, 1
param 7
param 2
t18 = call esMayor, 2
t19 = call saludar, 0
t20 = call saludar2, 0
print t20
t21 = call floatfn, 0
print t21
; ===== TAC  —  fin de programa   =====
