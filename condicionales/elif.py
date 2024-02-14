#Else if ==> Elif
#If anidado

ingreso = 10000
gasto = 2000

if ingreso > 10000:
    if ingreso - gasto < 0:
        print("Estas en deficit")
    elif ingreso - gasto > 3000:
        print("Estas bien en cualquier parte")
    else:
        print("estas gastando una banda")
elif ingreso > 1000:
    print("Estas bien en latinoamerica")
else:
    print("Sos pobre")