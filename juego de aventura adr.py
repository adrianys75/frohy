#juego de aventura adri
  def aventura():
    print("Te despiertas en un bosque oscuro. Tienes dos caminos frente a ti.")
    print("1. Caminar por el camino de la izquierda.")
    print("2. Caminar por el camino de la derecha.")

#elecciones para el usuario   
    eleccion = input("¿Cuál camino eliges? (1 o 2): ")

    if eleccion == "1":
        print("Te encuentras con un río caudaloso. Puedes:")
        print("1. Intentar cruzar el río.")
        print("2. Seguir el río.")
        
        eleccion_rio = input("¿Qué haces? (1 o 2): ")

        if eleccion_rio == "1":
            print("Logras cruzar el río y encuentras un tesoro escondido. ¡Has ganado!")
        elif eleccion_rio == "2":
            print("Sigues el río y encuentras un pueblo. ¡La aventura continúa!")
        else:
            print("Elección no válida. Fin de la aventura.")

    else eleccion == "2":
        print("Te encuentras con un misterioso anciano. Él te ofrece dos opciones:")
        print("1. Escuchar su historia.")
        print("2. Ignorarlo y seguir adelante.")
        
        eleccion_anciano = input("¿Qué haces? (1 o 2): ")

        if eleccion_anciano == "1":
            print("El anciano te cuenta sobre un tesoro escondido. ¡Ahora sabes dónde ir!")
        elif eleccion_anciano == "2":
            print("Decides ignorar al anciano y te pierdes en el bosque. Fin de la aventura.")
        else:
            print("Elección no válida. Fin de la aventura.")

    else:
        print("Elección no válida. Fin de la aventura.")
        

# fin de la aventura 
aventura()
