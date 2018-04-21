print("\n \n \t Seleccione una operacion: \n1: Suma \n2: Resta\n3: Division \n4: multiplicacion\n5: Datos \n6: multiplicacion de la clase \n7: salir \n0:Comapar dos numeros")

x=input("\n \n \t Opcion: ")
if x == '1' :
    print("\n\t Suma")
    num1=float(input("Dame un numero: "))
    num2=float(input("Dame otro numero: "))
    resultado=num1+num2
    print("El resultado es:",resultado)
    input("........"),
elif x == '2' :
    print("\n \t Resta")
    num1=float(input("Dame un numero: "))
    num2=float(input("Dame otro numero: "))
    resultado=num1-num2
    print("El resultado es:",resultado)
    input("........"),
elif x == '3' :
    print("\n \t Division")
    num1=float(input("Dame un numero: "))
    num2=float(input("Dame otro numero: "))
    resultado=num1/num2
    print("El resultado es:",resultado)
    input("........"),
elif x == '4' :
    print("\n \t Multiplicacion")
    num1=float(input("Dame un numero: "))
    num2=float(input("Dame otro numero: "))
    resultado=num1+num2
    print("El resultado es:",resultado)
    input("........"),
elif x == '5' :
    print("\n \t Ingresa tus DATOS ")
    nom=input("Nombre: ")
    edad=float(input("Edad: "))
    peso=float(input("Peso: "))
    print("tu nombre es",nom,"tienes ",edad,"tu peso es ",peso)
    input("........"),
elif x == '6' :
    print("\n \t Tablas de multiplicar")
    numero=int(input("De que tabla sera?:"))
    vecez=int(input("Cuantas tablas?:"))
    for x in range (0,vecez):
        print(numero,"*",x+1,"=",numero*(x+1))

    input("....")
elif x == '7' :
    print("\n \t Saliendo")
    input("........"),
elif x == '0' :
    print("Son los numeros iguales?")
    num1=float(input("Dame un numero: "))
    num2=float(input("Dame otro numero: "))
    if num1 == num2:
        print("Los numeros son iguales.")
    elif num1 < num2:
        print(num1," Es menor")
    elif num1 > num2:
        print(num1," Es mayor")
    else:
        print("kkkkkkkkkkkkk")
    input("........"),
else:
    print("Opcion invalida")
    input("...........")
