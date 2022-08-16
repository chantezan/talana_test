# codigo

El principal problema que tuve en este ejercicio fue la diferencia entre el orden del enunciado y el orden que muestra en los ejemplos
por ejemplo en el caso del ejemplo1 en el turno 3 dice "Tonyn le da un puñetazo al pobre Arnaldor" pero en el array la posicion 3 esta vacia por
ende me tuve que hacer unos supuestos propios ya que no podia corroborarlo con el enuniciado.
criterios en orden de prioridad:
1- Que tenga una combinacion
1.1 Si el largo de la combinacion es la misma usar el largo de los movimientos que no incluyen a la combinacion
2- Si no hay combinacion usar la cantidad de movimientos
3- Jugador 1

Esta la clase AbstractCharacter que implementa todo lo que debe tener un jugador
y luego las clases Stallone y Arnaldoe, que tienen los combos de cada uno.

Por ultimo esta la clase Game encargada de instancear el juego

# preguntas

1 los commit se pueden editar y agregar archivos con el comando --ammend, si el commit ya fue pusehado se debe volver a subir con git push force, pero esto ultimo
es innecesariamente arriesgado si hay mas personas trabajando en la ramma por lo cual conviene agregar otro commit pero si es ramma de trabajo unica no hay problema.

2 generalmente he usado gitflow, donde tenemos las diferentes ramas de features y hotfix, en las herramientas para deployar generalmente manejo las ramas de develop, qa
y production

3 al usar diferentes ramas y controlar desde donde deben salir las ramas no hay grandes problemas en el dia a dia, pero lo peor que me ha pasado es encontrar un bug
que no pudimos detectar en que commit comenzo y tuvimos que relanzar un reselease anterior donde sabiamos que el bug no existia :/

4 he trabajo con arquitecturas de microservicios principalmente basadas en colas con rabbitmq y llamadas asyncrinas entre ellos

5 Me gusta bastante aws porque tiene facilidades para usar sus servicios y hay bastantes guias para hacer practicamente cualquier cosa viendo un video de 15m
