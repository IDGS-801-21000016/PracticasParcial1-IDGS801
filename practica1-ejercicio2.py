
from dataclasses import dataclass

@dataclass
class countNumbers:
  listSize: int

  def sortList(self, list):
    for i in range(len(list)):
      for j in range(len(list)-1):
        if list[j] > list[j+1]:
          aux = list[j]
          list[j] = list[j+1]
          list[j+1] = aux
    return list

  def is_Even(self, number):
    if number % 2 == 0:
      return True
    else:
      return False

  def print_is_Even(self, list):
    even=[]
    odd=[]
    for i in range(len(list)):
      if self.is_Even(list[i]):
        even.append(list[i])
      else:
        odd.append(list[i])

    return even, odd

  def showRepiteNumbers(self, list):
    for i in range(len(list)):
      if list.count(list[i]) > 1:
        print(list[i], "se repite", list.count(list[i]), "veces")





def main():
  listSize = int(input("Ingrese el tamaño de la lista: "))
  obj = countNumbers(listSize)
  list = []
  for i in range(listSize):
    list.append(int(input("Ingrese el numero: ")))
  print(f"La lista es original: {list}")
  orderedList = obj.sortList(list)
  print(f"La lista ordenada es: {orderedList}")
  even, odd = obj.print_is_Even(orderedList)
  print(f"Los numeros pares son: {even}")
  print(f"Los numeros impares son: {odd}")
  obj.showRepiteNumbers(orderedList)



if __name__ == "__main__":
  main()