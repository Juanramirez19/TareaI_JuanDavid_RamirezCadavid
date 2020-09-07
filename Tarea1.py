from funciones import*

#Determinacion del factorial
n=int(input('ingrese el numero n ')) 
m=int(input('ingrese el numero m '))
x=input('digite numero ')
a=fact(n)
b=fact(m)
# Determinacion del binomial
c=bino(n,m)
#Determinacion Triangulo Pascal
d=pascal(x)
print('el factorial del numero n es', a)
print('el factorial del numero m es', b)
print('el coeficiente binomial es', c)
#Ejercicio Probabilidad
nn=100
k=10
pa=bino(nn,k)/(2**nn)
print('la probabilidad es \n' + str(pa)+  ' \n de sacar 10 veces cara')

f=0
kk=30
kk-=1
while kk>=0:
    f+=bino(nn,kk)
    kk-=1
t=f/(2**100)
pb=1-t
print('la probabilidad es \n' + str(pb)+  ' \n de sacar una cara mas de 30 veces')
    
