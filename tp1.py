############################# NO TOCAR ESTE CÓDIGO ############################
from ast import While
from cgitb import reset
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
juego = True
tepasaste = False

plata=int(500)
while juego == True:
    dineroapostado = 0
    c= sacar_carta()
    cartascrupier=[]
    cartascrupier.append(c)
    cartasjugador=[]
    suma_jugador=0
    suma_crupier=0
    print(f'El crupier saca un {c}')
    suma_crupier= suma_crupier + c

    print(f'El crupier saco hasta ahora las cartas: {cartascrupier}')
    
    apuesta= input (str("Quiere apostar?:"))

    if apuesta == 'si':
        dineroapostado= int(input('Cuanto quiere apostar?:'))
        while dineroapostado>plata or dineroapostado<0:
            print ("Monto invalido, vuelva a intenarlo")
            dineroapostado= int(input('Cuanto quiere apostar?:'))
        plata = plata - dineroapostado
        print('apostaste')    
    elif apuesta == 'no':
        print('usted juega sin apostar')
    
    while suma_jugador <=21:
            c=sacar_carta()
            cartasjugador.append(c)
            suma_jugador= suma_jugador +  c
            print(f'Usted saca un : {c}, tiene {suma_jugador} puntos')
            print(f'Por el momento saco las cartas: {cartasjugador}')

            if suma_jugador >21:
                print('Te pasaste') 
                tepasaste = True
                break
            else:
                pregunta=input('Quiere sacar otra carta?')
                if pregunta=='si':
                    continue
                elif pregunta == 'no':
                    break
    while suma_crupier <= 16 and tepasaste == False:
            c=sacar_carta()
            cartascrupier.append(c)
            suma_crupier = suma_crupier + c
            print(f'El crupier saco un : {c} , tiene {suma_crupier} puntos')
            print(f'Por el momento saco las cartas: {cartascrupier}')
            if suma_crupier <= suma_jugador and suma_crupier <= 16:
                continue
            else:
                break
    if suma_jugador > suma_crupier and suma_jugador <= 21:
            print('El ganador es el Jugador')
            plata = plata + dineroapostado * 2
    elif suma_jugador > suma_crupier and suma_jugador>21:
            print('El ganador es el Crupier')
    elif suma_jugador < suma_crupier and suma_crupier <= 21:
            print('El ganador es el Crupier')
    elif suma_jugador < suma_crupier and suma_crupier > 21:
            print('El ganador es el Jugador')
            plata = plata + dineroapostado * 2
    elif suma_jugador == suma_crupier or (suma_jugador and suma_crupier) > 21:
            print('Empate')
            plata = plata + dineroapostado
    print(f'tu plata es {plata}')
    jugar_otra_vez= input('Quiere jugar otra vez?')
    if jugar_otra_vez == 'si':
            
            suma_crupier = 0
            suma_jugador = 0
            cartascrupier = []
            cartasjugador = []
            juego == True
    elif jugar_otra_vez == 'no':
            juego == False
            print(f'te retiraste con {plata} pesos')
            break
