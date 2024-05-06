from algo1 import * 


# Busca el elmento en el arreglo y devuleve el índice 
def search(array,element): 
  if element in array: 
    for i in range(len(array)): 
      if array[i] == element: 
        index = i 
    return index
  else: 
    return None
    
#Ingresa un nuevo elemento en una posición indicada 
def insert(array,element,position): 
  #Verificamos que la posicion exista 
  if position < len(array): 
    #Creamos un Array Auxiliar y copiamos los elementos de Array 
    arrayAux = Array(len(array),0)
    for i in range(len(array)): 
      arrayAux[i] = array[i]
    
    #Desplazamos los elementos utlizando como referencia arrayAux 
    for i in range(position, len(array) -1): 
      array[i + 1] = arrayAux[i]
    
    #Ingresamos al arreglo el elemento en la posición indicada 
    if position < len(array): 
       array[position] = element  
    return array
  else: 
    return None 
  

#Elimina un elemento de array pasado como parámetro 
def delete(array,element): 
  if element in array: 
    index = search(array,element) 
    
    #Creamos un array auxiliar y copiamos los elementos de array 
    arrayAux = Array(len(array),0) 
    for i in range(len(array)): 
      arrayAux[i] = array[i]
    
    #Desplazamos los elementos hacia la izquierda y reemplazamos el      último por None 
    for i in range(index +1,len(array)): 
      array[i-1] = arrayAux[i]
    array[len(array)-1] = None 
    return array
  else: 
    return None
  

#Cuenta los elementos activos en array 
def length(array): 
  
  #Si hay posiciones en None contamos todas las que son distintas de   None 
  if None in array: 
    elements = 0 
    for i in range(len(array)): 
      if array[i] != None: 
        elements += 1
  
  #Sino, la cantidad de elementos es igual a la longitud del vector 
  else: 
    elements = len(array) 
  return elements 
