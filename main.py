#diego vargas
#4D teleco
nombre  =  input("ingrese  el  producto:  ")
precio  =  int(input("ingrese  un  precio:  "))
cantidad  =  int(input("¿cuantos productos lleva?:  "))
subtotal  =  (precio*cantidad)
iva  =  (precio*19/100)
print("nombre del producto:",  nombre)
print("cantidad:",  cantidad)
print("iva:",  iva)
print("total:",  subtotal+iva)