import random

def r1():
    option = random.randint(1,3)
    if option == 1:
        return '''🌱 **Reto 1: Apaga las luces innecesarias.**
Hoy, trata de apagar todas las luces y electrodomésticos que no estés utilizando. Incluso unos pocos minutos pueden hacer la diferencia en el ahorro de energía.''' 
    elif option == 2:
        return '''🌍 **Reto 1: Usa menos papel.**
Hoy, evita imprimir documentos a menos que sea absolutamente necesario. Opta por notas digitales o recicla papel ya utilizado.'''
    elif option == 3:
        return '''🚴 **Reto 1: Usa transporte sostenible.**
Si es posible, deja el coche en casa hoy. Camina, usa la bicicleta o el transporte público para reducir tu huella de carbono.'''

def r2():
    option = random.randint(1,3)
    if option == 1:
        return '''🚰 **Reto 2: Reduce el uso de agua.**
Mientras te cepillas los dientes o lavas los platos, cierra el grifo cuando no lo estés utilizando. ¡Ahorrarás litros de agua!'''
    elif option == 2:
        return '''🍃 **Reto 2: Come de forma sostenible.**
Hoy, trata de consumir alimentos locales o de temporada. Los productos locales suelen tener un menor impacto ambiental.'''
    elif option == 3:
        return '''🛍️ **Reto 2: Evita el plástico de un solo uso.**
Lleva tu propia bolsa reutilizable al hacer compras y evita comprar productos con embalajes de plástico innecesarios.'''

def r3():
    option = random.randint(1,3)
    if option == 1:
        return '''♻️ **Reto 3: Recicla correctamente.**
Hoy, separa adecuadamente tus residuos en papel, plástico y orgánicos. Asegúrate de que los materiales reciclables estén limpios antes de desecharlos.'''
    elif option == 2:
        return '''🌱 **Reto 3: Planta algo verde.**
Planta una semilla, un árbol o incluso una pequeña planta en una maceta. Ayuda a aumentar la vegetación y reducir el CO2 en el aire.'''
    elif option == 3:
        return '''💡 **Reto 3: Desconecta los dispositivos.**
Desconecta los dispositivos electrónicos que no estés utilizando. Incluso cuando están apagados, muchos dispositivos consumen energía en modo de espera.'''
