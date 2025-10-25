vaca_txt=open('arch_1.txt','r+')
t=vaca_txt.readline()
print(t)

t=input('Ingresa un texto con vaca:')
while(t.lower()).count('vaca')==0:
    t=input('Ingresa un texto con vaca__')
# .write lo escribe al final por que el puntero despues de .readline queda al final del texto
vaca_txt.write(t+'\n')
vaca_txt.close()


vaca_txt=open('arch_1.txt')
todas=vaca_txt.readlines()
for linea in todas:
    print(linea.strip('\n'))
vaca_txt.close()