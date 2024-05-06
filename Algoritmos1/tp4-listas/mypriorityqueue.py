
class PriorityQueue:
  head=None
class PriorityNode:
  value=None
  nextNode=None  
  priority=None

Q = PriorityQueue()

#Agrega un elemento a Q con la prioridad priority (entero), siendo Q una estructura de tipo PriorityQueue
def enqueue_priority(Q,element,priority): 
  newNode =  PriorityNode()
  newNode.value = element 
  newNode.priority = priority 
  currentPos = 0  
  #Si la cola está vacía insertamos un primer nodo (Q.head apunta a newNode)
  if Q.head is None:
    Q.head = newNode 
  #Sino, comparanamos la prioridad de nuevo elemento con el de Q.head, si es mayor, se crea un nuevo nodo y se desplazan los elementos  
  else:
    if priority >= Q.head.priority:
      newNode.nextNode = Q.head
      Q.head = newNode
      
    else:
      currentNode = Q.head
      while currentNode.nextNode is not None and currentNode.nextNode.priority >= priority:
        currentNode = currentNode.nextNode
        currentPos += 1 
      newNode.nextNode = currentNode.nextNode
      currentNode.nextNode = newNode
      #La posición del elemento es la posición siguiente a currentNode 
      return currentPos + 1 
  return currentPos 


#Extrae el primer elemento de la cola Q con la mayor prioridad
def dequeue_priority(Q): 
  if Q.head is None: 
    return None 
  else: 
    currentNode = Q.head 
    Q.head = currentNode.nextNode 
    element = currentNode.value 
    currentNode = None 
    #Devuelve el elemento con mayor prioridad 
    return element 



