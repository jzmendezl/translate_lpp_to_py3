# Traducctor de lenguaje LPP a Python Utilizando ANTLR4

En este proyecto se toma como entrada un script en lenguaje ``LPP`` y se traduce a lenguaje ``Python3``, como observaciones a este proyecto se veran que las salidas pueden distar un poco de las originales de `LPP`, esto debido a las peculiaridades del lenguaje `Python`.

### Posibles cambios en la salida

Se identificaron dos posibles cambios que puedan surgir al ejecutar el script obtenido al traducir de `LPP` a `Python`, estos son:

* Al declarar un entero y utilizar una divición, el lenguaje automaticamente lo cambia a decimal, aunque este sea un entero.

  * ej. 
`(2 / 4 = 2.0)`

* El segundo caso de cambio es en el trucar una cadena de texto al tamaño declarado en la careacion de esta variable, lo cual es complicado ya que `Python` por defecto no crea variables con estas condiciones.

  * ej. `LPP declaración` 
  `
    - cadena[10] mi_cadena
    - inicio
    - mi_cadena <- "Lenguajes de Programación"
    - escriba mi_cadena

    output: // Lenguajes
  `

  en `Python` una forma de solucionarlo es con un slice pero se decidio no hacerlo para mostrar las diferencias de los dos lenguajes.


# Reacomendaciones

* Abrir el proyecto desde Pycharm, esto con el fin de hacer mas facil la ejecucion y visualizacion del proyecto.

* Tener instalado el Plugin de ANTLR4 y ANTRL4 Tools, los cuales son muy utiles al momento de visualizar el arbol sintactico y ayuda a la creacion del codigo.


# Instalación

Inicialmente se debe instalar ANTLR4, para ello se deja un archivo del runtime de antlr en la raiz del proyecto. 

Si desea instalarlo desde consola utilice el siguiente comando para instalar el runtime de ANTLR4
```sh 
pip install antlr4-python3-runtime
```
Utiliza el siguiente comando para instalar ANTRL4 Tools
```sh
pip install antlr4-tools
```

# Gramatica y generadores

Una vez instalado el runtime de ANTLR4, navegue hasta la carpeta `./grammar` en ella encontrara un archivo llamado `LPP.g4` en el se encuentra la gramatica utilizada para este proyecto, la cual obtuvimos de otro proyecto (`https://github.com/LenguajeLPP/lpp`), aunque sufrio algunas modificaciones.

Dentro de este archivo puede daar click derecho y hacer click en la opcion de `Generate ANTLR Recognizer`, una vez hecho esto se creara una carpeta llamada `./gen`, la cual contiene archivos como los de parser y listener que se utilizaron en este proyecto.

## Importante
Asegurece que la carpeta gen esta seleccionada como carpeta source, para ello una vez creada la carpeta ubicarse sobre ella y dar click derecho y luego en la opcion `Mark directory As`, selecciona la opcion `Sources Root`

## Visualizar el arbol sintactico

Si desea visualizar el arbol sintactico el el archivo de la gramatica `LPP.g4` ubiquese sobre la primera regla, en este caso es ``programa`` y de click derecho y luego en la opción de ``Test Rule progrma`` con esto se abrira una ventana en la cual puede introducir de forma manual una entrada para ver el arbol sintactico generado por dicha entrada.

# Ejecucion del proyecto

Para ejecutar este proyecto debe ejecutar el archivo `./main.py` en cual va a generar dos cosas.

* La primera es una salida en consola con la traducción obtenida a el lenguaje `Python`

* La segunda es un archivo llamado `./output.py` el cual tambien contiene la traducción del archivo pero este es el archivo de salida listo para su ejecucción.

# Universidad Nacional De Colombia - Sede Bogota D.C

 # Integrantes:

 * Joe Zafir Méndez León
 * Juan Diego
 * Juan Pablo