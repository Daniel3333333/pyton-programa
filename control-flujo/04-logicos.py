#and dos condiciones, si los dos son tru todo es tue si uno falla todo false
#or: dos condiciones, si uno es true todo es true 
#not: niega el resultado

#operador de cotro circuito: todas las evaluaciones tienen que ser true y si la primera es false, no va a evaluar a las demas, es una ayuda para ahorrar

gas = False
encendido = True
edad = 18
if not gas and encendido and edad > 17:
    print("puedes avanzar")
    
# gas = True 
# encendido = True 
# if gas or encendido:
#     print("puedes avanzar")

# gas = True 
# encendido = True 
# if gas not encendido:
#     print("puedes avanzar")