
intentos = 6

palabra_adivinar = list(input( 'Introduce una palabra:'))

dibujo =['_']
dibujo_completo = dibujo * len(palabra_adivinar)

print (dibujo_completo)

while intentos > 0:
    
    if dibujo_completo == palabra_adivinar:
        print ('has ganado')
        break
    
    else:
        letra_usuario = input ('introduce una letra: ')
        if letra_usuario in palabra_adivinar:
            
                for pos, letra in enumerate(palabra_adivinar):
                    if letra_usuario == letra:
                        dibujo_completo[pos] = letra_usuario
                    
                print (dibujo_completo) 
      
        else:
            intentos -= 1 
            print ('Te quedan ,', intentos)
            
    if intentos == 0:
        print ('has perdido')
      
        