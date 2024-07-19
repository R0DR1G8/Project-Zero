#numeros primo
print ("ESTE PROGRAMA TE DICE SI\n","LOS NúMEROS QUE HAY\n","ENTRE UNO Y OTRO SON PRIMOS O NO\n")
num1=0
num2=0
n1=int(input("INGRESE EL PRIMER NÚMERO \n"))
n2=int(input("INGRESE EL SEGUNDO NÚMERO \n"))
if n1>n2:
    num1=+n2
    num2=+n1+1
elif n1<n2:
    num1=+n1
    num2=+n2+1
else:
    print("EL MARGEN ENTRE LOS DOS NUMEROS ES MUY CORTO")
for i in range (num1,num2):
    v=i-1
    factorial=1
    k=1
    while(k<=v):
        factorial = k*factorial
        k=k+1
    resultado=factorial+1
    if resultado%i==0:
        print("EL NUMERO",i,"ES PRIMO")
    else:
        print("EL NUMERO",i,"NO ES PRIMO")
    