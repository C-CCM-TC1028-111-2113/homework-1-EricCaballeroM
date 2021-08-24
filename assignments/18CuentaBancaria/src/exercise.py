def main():
    #escribe tu código abajo de esta línea
    #saldo de tu cuenta bancaria 

sm=float(input("give me the balance of the past month: "))
ing=float(input("give me the incomes: "))
exp=float(input("give me the expenses: "))
che=float(input("give me the numer of cheks: "))

st=sm+ing-exp-(che*13)
desc=st*0.925
print("the final balance: ", desc)
    pass

if __name__ == '__main__':
    main()
