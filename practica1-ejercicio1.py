from dataclasses import dataclass

@dataclass
class GeneratePyramid:
  n: int

  def imprimeEstrellas(self, n):
    for i in range(self.n):
      for j in range(i+1):
        print("*", end="")
      print("")

def main():
    n = input("Ingrese el numero de filas: ")
    obj = GeneratePyramid(int(n))
    obj.imprimeEstrellas(5)

if __name__ == "__main__":
    main()