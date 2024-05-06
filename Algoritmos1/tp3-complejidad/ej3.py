import time 

# Algoritmo inútil que resta billetes de 100,10 y 1 a un monto dado. 
def entrega_billetes_2(monto):   
  billete=100 
  inc=0 
  billete_actual=billete/(10**inc) 
  while(monto>0): 
    if monto >= billete_actual: 
      monto=monto-billete_actual 
    else: 
      inc=inc+1 
      billete_actual=billete/(10**inc)

start = time.time() 

#LLamamos a la funciòn en ese intervalo 
for monto in range(100000,1000000, 100000): 
  entrega_billetes_2(monto)
end = time.time() 
print(end - start)

