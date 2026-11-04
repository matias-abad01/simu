from queue import LifoQueue as Pila
"""
 Simulacro Python - Tema 1
Importante

    Template de funciones a implementar acá
    Lista de funciones permitidas acá
    Para testear el código pueden usar este archivo que ya cuenta con todo lo necesario para desarrollar sus propios tests (este archivo no se entrega)

Implementar las siguientes especificaciones en Python.
Ejercicio 1 [2,25 puntos]

problema ejercicio1 (in s: seq⟨Z⟩, in n: Z) : seq⟨Z⟩ {
  requiere: { Existe al menos una subsecuencia de s que suma exactamente n }
  requiere: { Todos los elementos de s son estrictamente mayores a 0 }
  asegura: { res es una subsecuencia consecutiva de s que suma exactamente n }
  asegura: { Si hay más de una subsecuencia de s que suma exactamente n, res es la que tiene el índice de inicio más grande }
}

Ejemplo: ejercicio1([1,3,2,5,4,1,8], 5) debe devolver [4,1]

Ejercicio 2 [2,25 puntos]

Un docente recibe una pila de exámenes (no todos son en compu!), y desea separarlos por tema para facilitar el trabajo de corrección. La pila contiene tuplas con el nombre del alumno y el tema del examen, y desea sacar de dicha pila los exámenes de tema 1 y ponerlos en una nueva pila, manteniendo en ambas pilas el orden original.

problema ejercicio2 (inout examenes: Pila⟨String x Z⟩) : Pila⟨String⟩ {
  requiere: { Todos los elementos de examenes tienen en la segunda componente de la tupla un 1 o un 2 }
  requiere: { Todas las primeras componentes de tupla de examenes son distintas entre sí }
  modifica: { examenes }
  asegura: { res contiene exactamente los nombres cuya segunda componente en examenes@pre tenía tema = 1, en el mismo orden que se encontraban en examenes@pre }
  asegura: { examenes contiene exactamente las tuplas de examenes@pre cuya segunda componente son tema = 2 allí, en el mismo orden que se encontraban originalmente .}
}

Ejemplo: Si examenes contiene (de tope a base) [("Ana",1),("Beto",2),("Caro",1),("Juan",2)], 

entonces se debe devolver ["Ana","Caro"] y examenes contiene [("Beto",2),("Juan",2)]
  

Ejercicio 3 [2,25 puntos]

problema ejercicio3 (inout A: seq⟨seq⟨Z⟩⟩) {
  requiere: { |A| > 0 }
  requiere: { Todos los elementos de A tienen la misma longitud, la cual es estrictamente mayor a 0 }
  modifica: { A }
  asegura: { |A| = |A@pre| }
  asegura: { Todos los elementos de A tienen la misma longitud }
  asegura: {|A[0]| = |A@pre[0]| + 1 }
  asegura: { A[i][j] = A@pre[i][j] para todo i, j en rango tal que j ≠ |A[0]|-1 }
  asegura: { A[i][|A[0]|-1] = minimoDeLista(A@pre[i]) para todo i en rango }
}

Nota: minimoDeLista representa el mínimo valor de una lista
Ejercicio 4 [2,25 puntos]

Contamos con los datos de dos elecciones consecutivas. A pesar de que el voto es secreto, sabemos a qué candidato votó cada persona en cada una de las elecciones, ya que contamos con diccionarios cuyas claves son los ciudadados y cuyos valores son los candidatos a los cuales votó. Implementar la función ejercicio4, que nos permite saber cuantos candidatos conservaron sus votos.

problema ejercicio4 (in eleccion1: dict⟨String, String⟩, in eleccion2: dict⟨String, String⟩) : dict⟨String, Z⟩ {
  requiere: { Las claves de eleccion1 y eleccion2 coinciden }
  asegura: { Las claves de res son un subconjunto de los valores de eleccion1 y eleccion2 }
  asegura: { Un candidato c está en res si y sólo si al menos un mismo ciudadano votó por c en ambas elecciones }
  asegura: { Para cada clave c de res, res[c] es la cantidad de ciudadanos que votaron por c en ambas elecciones }

Ej: ejercicio4 ({"Ana":"X","Beto":"Y","Caro":"X"} ,{"Ana":"X","Beto":"X","Caro":"X"}))
 debe devolver {'X':2}
  

Ejercicio 5 [0,5 punto]

Conteste marcando la opción correcta.
Dado el siguiente código en Python, considere cobertura de ramas vs. cobertura de condiciones básicas:

    def f(a:int, b:int) -> int:
      if a > 0 and b % 2 == 0:
        return 1
      if a == 0 or b > 10:
        return 2
      return 3
    

Cada caso de prueba se indica como (a, b). ¿Cuál conjunto logra 100% de cobertura de ramas pero NO 100% de cobertura de condiciones básicas?

Casos de prueba: (1,2), (1,11), (1,3)
Casos de prueba: (1,2), (0,3), (1,11)
Casos de prueba: (1,2), (1,11), (0,11), (1,1)
Ejercicio 6 [0,5 punto]

Elija un nombre adecuado para la función a definir en el ejercicio 3.
Si tenemos un programa y queremos contar la cantidad de operaciones que realiza para un input particular:

eliminar_fila_con_minimo_de_columna
agregar_fila_con_minimo_de_columna
agregar_columna_con_minimo_de_fila
eliminar_columna_con_minimo_de_fila"""

# Ejercicio 1
def ejercicio1(s: list[int], n: int) -> list[int]:
    inicio: int = 0
    fin: int = 0
    suma: int = 0
    res: list[int] = []

    while fin < len(s):
        suma += s[fin]

        while suma > n:
            suma -= s[inicio]
            inicio += 1

        if suma == n:
            res.clear()
            indice: int = inicio

            while indice <= fin:
                res.append(s[indice])
                indice += 1

        fin += 1

    return res
print(ejercicio1([1,3,2,5,4,1,8], 5))

# Ejercicio 2
def ejercicio2(examenes: Pila[(str, int)]) -> Pila[str]:
    aux: Pila[(str, int)] = Pila()
    temas2: Pila[(str, int)] = Pila()
    nombres: Pila[str] = Pila()
    res: Pila[str] = Pila()

    while not examenes.empty():
        aux.put(examenes.get())

    while not aux.empty():
        examen: tuple[str, int] = aux.get()

        if examen[1] == 1:
            nombres.put(examen[0])
        else:
            temas2.put(examen)

    while not temas2.empty():
        examenes.put(temas2.get())

    while not nombres.empty():
        res.put(nombres.get())

    return res


# Ejercicio 3
def ejercicio3(A: list[list[int]]) -> None:
    fila: int = 0

    while fila < len(A):
        columna: int = 1
        minimo: int = A[fila][0]

        while columna < len(A[fila]):
            if A[fila][columna] < minimo:
                minimo = A[fila][columna]
            columna += 1

        A[fila].append(minimo)
        fila += 1


# Ejercicio 4
def ejercicio4(eleccion1: dict[str, str], eleccion2: dict[str, str]) -> dict[str, int]:
    res: dict[str, int] = {}

    for ciudadano in eleccion1.keys():
        candidato1: str = eleccion1[ciudadano]
        candidato2: str = eleccion2[ciudadano]

        if candidato1 == candidato2:
            if candidato1 in res:
                res[candidato1] += 1
            else:
                res[candidato1] = 1

    return res
