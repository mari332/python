frutas = {'Plátano':3500, 'Manzana':5300, 'Pera':4500, 'Naranja':5000, 'Fresas':6500, 'Mango':7600, 'Piña':3800, 'Uva':2200}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")