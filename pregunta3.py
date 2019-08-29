"""
Tercera Pregunta – Derivar Contraseña (Ethical Hacking)


Puede recibir como parametros desde la linea de comando argv 1 y 2
1 -> Para la contraseña
2 -> Para el inicio de la contraseña, en el caso de que se desea inicia el str con
     0 para el primer caracter o 1 para el primer caracter o x para el primer
     caracter.

Pasos
1. Se abre el archivo
2. Se convierte en lista
3. Se ordena la lista, y se eliminan los vacios de la lista
4. Se realiza un ciclo sobre las secuencias del archivo y verifica los tamaños y
   asignacion de la mas corta.


3. Se omiten los que tienen ceros, dado que en el enunciado las contraseña inician
    por 1, entonces 0 no tendria posicion y no es una opcion valida para solicitar
    al cliente. Aun que la pregunta dice que todas son correctas.
"""

import sys

if len(sys.argv[1:]) > 0:
    p = sys.argv[1]
else:
    p = "531278"

if len(sys.argv[2:]) > 0:
    init = int(sys.argv[2])
else:
    init = 0

with open('keylog.txt', 'r') as f:
    # Sacamos los vacios
    sec = [x for x in f.read().split("\n") if x != '']
    # sec = [x for x in sec if '0' not in x]
    sec.sort()
    p_new = []
    p_small_len = len(p)
    p_small = p
    print(p_small_len)
    for s in sec:
        temp = ""
        pos1 = int(s[0]) - init
        pos2 = int(s[1]) - init
        pos3 = int(s[2]) - init
        tam_p = len(p)
        if pos1 < tam_p and pos1 >= 0:
            temp = temp + p[pos1]
        if pos2 < tam_p and pos2 >= 0:
            temp = temp + p[pos2]
        if pos3 < tam_p and pos3 >= 0:
            temp = temp + p[pos3]

        # print(s, p, tam_p, temp)
        if temp:
            if len(temp) < p_small_len:
                p_small_len = len(temp)
                p_small = temp

    print("Contraseña mas corta: {} de No. de caracteres {}".format(p_small, p_small_len))

