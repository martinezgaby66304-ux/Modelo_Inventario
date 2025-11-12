import math 
class Producto:
    def __init__(self, K, D, h, L):
        self.k = K
        self.D = D
        self.h = h
        self.L = L
K_costo_producto = float(input("Ingresa el Valor de k:  "))
D_demanda= float(input("Ingresa el Valor de D:  "))
h_costo_mantenimiento= float(input("Ingresa el Valor de h:  "))  
L_dias_pedido= float(input("Ingresa el numero de dias en que realizas un pedido:  "))  
Variables=Producto(K_costo_producto, D_demanda, h_costo_mantenimiento, L_dias_pedido ) 
def Cantidad_de_Pedido(K, D, h):
    y= math.sqrt(2 * K * D / h)
    print("La cantidad del pedido es:   ", y)
    return y
cantidad_pedido = Cantidad_de_Pedido(Variables.k, Variables.D, Variables.h)  

def Renovacion_de_pedido(y , D):
    To = (y / D)
    print("El inventario se renueva aproximadamente:   ", To) 
    return To
Renovacion = Renovacion_de_pedido(cantidad_pedido, Variables.D)

def Tiempo_ocurridos(L , To):
    n = L / To
    n_redondeado = round(n)
    print("El numero de tiempos ocurridos es de:   ", n)
    return n_redondeado
Tiempo = Tiempo_ocurridos(Variables.L, Renovacion)

def Inventario_restante(L, n, To):
    Le = L - (n * To)
    print("El inventario restante es de:   ", Le)
    return Le
Inventario = Inventario_restante(Variables.L, Tiempo, Renovacion)

def Unidades_en_inventario(Le, D):
    U = Le *  D
    print("Cantidad de unidades que quedan en el inventario son :   ", U)
    return U
Unidades_en_inventario(Inventario, Variables.D)

def Costo_total(K, D, h, y):
    CTU = ( (K * D) / y ) + ( (h * y) / 2 )
    print("El costo total :   ", CTU)
Costo_total(Variables.k, Variables.D, Variables.h, cantidad_pedido) 
