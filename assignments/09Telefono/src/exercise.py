def main():
    #escribe tu código abajo de esta línea
    #telephone

msg=int(input("give me the number of messages: "))
meg=float(input("give me the number of megas: "))
min=float(input("give me the number of minutes: "))

nmsg=msg*0.8
nmeg=meg*0.8
nmin=min*0.8

cost=nmsg+nmeg+nmin

print("the mensual cost is: ",cost)
    #Leer los datos
    pass


if __name__ == '__main__':
    main()
