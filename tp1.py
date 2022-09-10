############################# NO TOCAR ESTE CÓDIGO ############################
from random import randint

def sacar_carta():
    '''
    Esta función toma una carta de un mazo de forma aleatoria. La carta está numerada del 1 al 10 (inclusive).

    params:
        Esta función no tiene parámetros de entrada.
    out:
        carta: int. El número de la carta sacada.
    '''
    carta = randint(1,10)
    return carta


######################## EJEMPLO DE USO DE SACAR_CARTA ########################
#c = sacar_carta()
#print(c)
#En la consola se vería:    8

########################### AQUÍ COMIENZA TU CÓDGIO ###########################
c= sacar_carta()
cartascrupier=[]
cartascrupier.append(c)
cartasjugador=[]
suma_jugador=0
suma_crupier=0
print(f'El crupier saca un {c}')
suma_crupier= suma_crupier + c

print(f'El crupier saco hasta ahora las cartas: {cartascrupier}')
plata=int(500)
apuesta= input (str("Quiere apostar?:"))
print(apuesta)
if apuesta == 'si':
    dineroapostado= int(input('Cuanto quiere apostar?:'))
    while dineroapostado>plata or dineroapostado<0:
        print ("Monto invalido, vuelva a intenarlo")
        dineroapostado= int(input('Cuanto quiere apostar?:'))
        
else:
    dineroapostado = 0

while suma_jugador <=21:
    c=sacar_carta()
    cartasjugador.append(c)
    suma_jugador= suma_jugador +  c
    print(f'Usted saca un : {c}')
    print(f'Por el momento saco las cartas: {cartasjugador}')
    pregunta=input('Quiere sacar otra carta?')
    if pregunta=='si':
        continue
    elif pregunta == 'no':
        break
while suma_crupier <= 16:
    c=sacar_carta()
    cartascrupier.append(c)
    suma_crupier= suma_crupier + c
    print(f'El crupier saca un: {c}, su total es {suma_crupier}')
    print(f'Por elmomento saco las cartas {cartascrupier}')
    print('Pide otra carta')
