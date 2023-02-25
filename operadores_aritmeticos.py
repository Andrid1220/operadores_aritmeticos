# programa para implementar operadores aritmeticos

print("------------------------------")
print("-----OPERADORES ARITMETICOS---")
print("------------------------------")

# input

x = int(input("digite al valor de x: "))
y = int(input("digite el valor de y: "))

# procesing

s = x + y
r = x - y
m = x * y
d = x / y
mod = x % y
de = x // y
p = x ** y

# output
print("----------------------------------------")
print("------------RESULTADOS------------------")
print("----------------------------------------")
print("suma: " + str(s))
print("resta: " + str(r))
print("multiplicacion " + str(m) )
print("division: " + str(d))
print("modulo: " + str(mod))
print("dividion entera: " + str(de))
print("potencia: " + str(p))