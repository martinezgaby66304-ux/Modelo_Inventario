import math 
class Producto:
    def __init__(self, K, D, h, L):
        self.k = K
        self.D = D
        self.h = h
        self.L = L
K_CostoProducto = float(input("Ingresa el Valor de k:  "))
D_Demanda= float(input("Ingresa el Valor de D:  "))
h_CostoMantenimiento= float(input("Ingresa el Valor de h:  "))  
L_DiasPedido= float(input("Ingresa el numero de dias en que realizas un pedido:  "))  
Variables=Producto(K_CostoProducto,D_Demanda,h_CostoMantenimiento,L_DiasPedido) 
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
    n = (L / To)
    print("El tiempo de renovacion del pedido es de:   ", n)
Tiempo_ocurridos(Variables.L, Renovacion)
     
