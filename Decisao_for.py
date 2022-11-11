import msvcrt

tabuada=int(input("Digite o Numero para exibir a tabuada: "))
print("Tabuada do Numero "+ str(tabuada))
for valor in range(0,11,1):
    print(str(tabuada)+"x"+ str(valor)+"="+str(tabuada*valor))
msvcrt.getch()