import math 
class Producto:
    def __init__(self, K, D, h):
        self.k = K
        self.D = D
        self.h = h
K_CostoProducto = float(input("Ingresa el Valor de k:  "))
D_Demanda= float(input("Ingresa el Valor de D:  "))
h_CostoMantenimiento= float(input("Ingresa el Valor de h:  "))  
Variables=Producto(K_CostoProducto,D_Demanda,h_CostoMantenimiento) 
def Cantidad_de_Pedido(K, D, h):
    y= math.sqrt(2 * K * D / h)
    print("La cantidad del pedido es:   ", y)
    return y
cantidad_pedido = Cantidad_de_Pedido(Variables.k, Variables.D, Variables.h)  

def Renovacion_de_pedido(y , D):
    RenovacionInventario = (y / D)
    print("El inventario se renueva aproximadamente:   ", RenovacionInventario)  
Renovacion_de_pedido(cantidad_pedido, Variables.D)