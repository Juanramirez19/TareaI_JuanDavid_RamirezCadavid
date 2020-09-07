def fact(n): # definicion de una funcion que hara el factorial
    f=1   #inicio del contador o bandera
    for i in range(1,n+1): #inicio del ciclo for para pasar sobre cada numero empezando en 1
        f=f*i # definicion de la funcion factorial
    return f # regresa el valor del contador con el nuevo valor

def bino(n,m): #definicion de una funcion que hara el coeficiente binomial 
    if (n>=m): #consideracion de un condicional para evitar que el valor m>n ya que el factorial negativo no esta definido en nuestro caso
        r=fact(n)/(fact(m)*fact(n-m)) #definicion de la binomial
        return r #regresa el valor del coeficiente binomial
    else: #sino, en el caso de m>n
        print('no es posible coeficiente binomial')
        
def pascal(x): #definicion de una funcion que hara el triangulo de pascal
    n=0 # contador
    m=0 #contador
    while(n<=x): #ciclo anidado
        while(m<=n):
            coe=bino(n,m) #uso de la funcion binomial
            m=m+1 #continuacion contador para m
            print(''),coe,(''),
        print('n='), n # Imprime el numero de fila
        n=n+1 #continuacion contador para n
        m=0
        print('') #imprime con un espacio
        print('') #imprime con doble espacio
        
        
#x=input('digite numero ')

#b=pascal(x)

#n=int(input('ingrese el numero n '))
#m=int(input('ingrese el numero m '))

#a=fact(n)
#b=fact(m)
#c=fact(n-m)
#r=bino(n,m)
#print (a, b, c, r)
        

        
