# Examen Concurrente Y Asincrona

Enlace al repositorio del examen : [GitHub](https://github.com/migueliiin/Examen_ConcurrenteAsincrona.git)

## Problema 1 - Simulación Bancaria (Enunciado)

Un banco necesita controlar el acceso a cuentas bancarias y para ello desea hacer un programa de prueba en Python que permita lanzar procesos que ingresen y retiren dinero a la vez y comprobar así si el resultado final es el esperado.

Se parte de una cuenta con 100 euros y se pueden tener procesos que ingresen 100 euros, 50 o 20. También se pueden tener procesos que retiran 100, 50 o 20 euros euros. Se desean tener los siguientes procesos:

· 40 procesos que ingresan 100

· 20 procesos que ingresan 50

· 60 que ingresen 20.

De la misma manera se desean lo siguientes procesos que retiran cantidades.

· 40 procesos que retiran 100

· 20 procesos que retiran 50

· 60 que retiran 20.

Se desea comprobar que tras la ejecución la cuenta tiene exactamente 100 euros, que era la cantidad de la que se disponía al principio.

## Problema 2 - Simulador de Casino (Enunciado)

Se desea simular los posibles beneficios de diversas estrategias de juego en un casino. La ruleta francesa es un juego en el que hay una ruleta con 37 números (del 0 al 36). Cada 3000 milisegundos el croupier saca un número al azar y los diversos hilos apuestan para ver si ganan. Todos los hilos empiezan con 1.000 euros y la banca (que controla la ruleta) con 50.000. Cuando los jugadores pierden dinero, la banca incrementa su saldo.

· Se puede jugar a un número concreto. Habrá 4 hilos que eligen números al azar del 1 al 36 (no el 0) y restarán 10 euros de su saldo para apostar a ese ese número. Si sale su número su saldo se incrementa en 360 euros (36 veces lo apostado).

· Se puede jugar a par/impar. Habrá 4 hilos que eligen al azar si apuestan a que saldrá un número par o un número impar. Siempre restan 10 euros para apostar y si ganan incrementan su saldo en 20 euros.

· Se puede jugar a la «martingala». Habrá 4 hilos que eligen números al azar. Elegirán un número y empezarán restando 10 euros de su saldo para apostar a ese número. Si ganan incrementan su saldo en 360 euros. Si pierden jugarán el doble de su apuesta anterior (es decir, 20, luego 40, luego 80, y así sucesivamente)

· La banca acepta todas las apuestas pero nunca paga más dinero del que tiene.

· Si sale el 0, todo el mundo pierde y la banca se queda con todo el dinero.