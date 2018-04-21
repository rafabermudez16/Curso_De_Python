
a=int(input("\n\n\tDame un numero: \n "))
b=int(input("\n\n\tDame otro numero: \n "))
c=int(input("\n\n\tDame otro numero: \n "))


if a>b and a>c:
    print("\n \n \t El numero",a ,"es mayor")
elif b>c:
    print("\n \n\t El numero ",b,"es el de enmedio","\n \n \t El numero ",c,"es el menor")
elif b>a and b>c:
    print("\n \n \t El numero",b,"es mayor")
elif a>c:
    print("\n \n\t El numero ",a,"es el de enmedio","\n \n \t El numero ",c,"es el menor")
elif c>a and c>b:
    print("\n \n \t El numero",b,"es mayor")
elif b>a:
    print("\n \n\t El numero ",b,"es el de enmedio","\n \n \t El numero ",a,"es el menor")


input("\n \n \t \t:______________________:")
