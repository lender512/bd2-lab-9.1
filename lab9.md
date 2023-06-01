# Laboratio 9.1 - Base de datos 2
Integrantes
- Luis Alfonso Berrospi Rodriguez
- Mario Jacobo Rios Gamboa
# Busqueda por rango
En la siguiente tabla se pueden ver los resultados:
| Rango | Q15 | Q82 | Q121 |
|-------|-----|-----|------|
| 0.8   | 1.0 | 1.0 | 0.6875 |
| 1.5   | 1.0 | 0.783333 | 0.454545 |
| 2.6   | 0.980392 | 0.531915 | 0.473684 |
# Knn 
<!--     q15  q82    q121
2   1.0  1.0  1.0000
4   1.0  1.0  1.0000
8   1.0  1.0  0.8750
16  1.0  1.0  0.6875
32  1.0  1.0  0.5000 -->
En la siguiente tabla se pueden ver los resultados:
| K | Q15 | Q82 | Q121 |
|-------|-----|-----|------|
| 2   | 1.0 | 1.0 | 1.0000 |
| 4   | 1.0 | 1.0 | 1.0000 |
| 8   | 1.0 | 1.0 | 0.8750 |
| 16  | 1.0 | 1.0 | 0.6875 |
| 32  | 1.0 | 1.0 | 0.5000 |
# Conclusiones

1. ¿Cuál es la complejidad computacional de ambos métodos de búsqueda en función de cálculos de la ED?
   La complejidad para el metodo de busqueda por rango en función de las ED es O(n) ya que se recorren todos los puntos para encontrar los que están dentro del rango. La complejidad para el metodo de busqueda KNN en función de las ED tambien es O(n), sin embargo, utilizando una cola de prioridad, se puede reducir el costo de ordenar al final de la busqueda.
2. ¿Cuál de los dos métodos de búsqueda usted usaría en un ambiente real de recuperación de la información? Sustente su respuesta.
   Los dos métodos dependen de la situación. En el caso de la busqueda por rango, uno necesitaría conocer como es el comportamiento del espacio para poder identificar un rango adecuado para escoger. Puesto que podría darse que un rango ingresado no de ningun resultado y no se sabría si es porque el rango es muy pequeño o de verdad no hay ningun vecino que se parezca al record seleccionado. Por otro lado la búsqueda por knn garantiza que se devuelvan siempre una cantidad determinada de vecinos, sin embargo estos podrían ser completamente diferentes al record seleccionado puesto que no existe otros a una distancia cercana.
