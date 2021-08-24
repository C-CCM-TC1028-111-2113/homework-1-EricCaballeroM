def main():
    #escribe tu código abajo de esta línea
    #publicación en una editorial
def numpag(p):
    b=p/475



e=int(input("give the number of words: "))
a=e%2
t=numpag(e)
x=((numpag(e)+1)*60)*0.90
y=((numpag(e))*60)*0.90


if a!=0:
    numpag(e)+1
    print("the publication cost is: ", x)
else:
    print("the publication cost is: ", y)
    pass


if __name__ == '__main__':
    main()
