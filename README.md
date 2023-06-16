# **Whisper+: Convierte videos o audios a texto**

## **Introducción**
Whisper+ es una herramienta que extiende las utilidades principales del proyecto [Whisper AI](https://github.com/openai/whisper). A continuación se presenta una gía de instalación y uso: 

## **Instalación de Whisper+**
El script en cuestión tiene un archivo _requirements.txt_ el cual especifica las dependencias que se necesitan para correr dicho script. 

Para este caso, usted debe tener instalado previamente Python3 y clonado este repositorio: 

```
$ git clone https://github.com/Nicromano/whisper-plus.git
```
Luego haciendo uso de la herramienta pip, instalaremos las dependencias necesarias: 

```
$ pip install -r requirements.txt
```

Una vez instalado todos los requerimientos del script. Puede proceder a usarlo.

## **Agregar Whisper+ a las variables de entorno**

Si deseas llamar a Whisper+ desde cualquier directorio de tu SO, debes agregarlo a las variables de entorno de tu sistema operativo en cuestión. 

### **En Windows:**

1. Abre el Explorador de archivos y navega hasta el directorio que contiene tus scripts.

2. Copia la ruta completa del directorio. Por ejemplo, `C:\ruta\hacia\scripts`

3. Haz clic derecho en el icono de _"Este equipo"_ o _"Equipo"_ en el escritorio y selecciona _"Propiedades"_.

4. En la ventana de _Propiedades del sistema_, haz clic en _"Configuración avanzada del sistema"_ en el panel izquierdo.

5. Se abrirá la ventana _"Propiedades del sistema"_. Haz clic en el botón _"Variables de entorno"_.

6. En la sección _"Variables del sistema"_, busca la variable llamada _"Path"_ y haz clic en _"Editar"_.

7. En la ventana _"Editar variables del sistema"_, haz clic en _"Nuevo"_ y pega la ruta completa del directorio de tus scripts. Asegúrate de agregar un punto y coma `(;)` al final para separarlo de otras rutas existentes. Por ejemplo, `C:\ruta\hacia\scripts;`

8. Haz clic en _"Aceptar"_ en todas las ventanas para guardar los cambios.

Ahora, podrás ejecutar tus scripts desde cualquier ubicación en la línea de comandos de Windows simplemente escribiendo el nombre del script.

### **En Linux:**

1. Abre una terminal y navega hasta el directorio que contiene tus scripts.

2. Copia la ruta completa del directorio. Por ejemplo, `/ruta/hacia/scripts` .

3. Abre el archivo `~/.bashrc` en un editor de texto. Puedes utilizar el siguiente comando para abrirlo con el editor de texto nano:

```
$ nano ~/.bashrc
```

4. Agrega la siguiente línea al final del archivo, reemplazando `/ruta/hacia/scripts` con la ruta completa de tu directorio de scripts:

```
$ export PATH="/ruta/hacia/scripts:$PATH"
```

5. Guarda los cambios y cierra el editor de texto.

6. En la terminal, ejecuta el siguiente comando para actualizar las variables de entorno:

```
$ source ~/.bashrc
```
7. Una vez en el directorio correcto, ejecuta el siguiente comando para otorgar permisos de ejecución al archivo:

```
chmod +x "whisper+.py"
```
Ahora, podrás ejecutar tus scripts desde cualquier ubicación en la terminal de Linux simplemente escribiendo el nombre del script.

Después de seguir estos pasos, podrás llamar a tus scripts desde cualquier ubicación en la línea de comandos tanto en Windows como en Linux sin tener que especificar la ruta completa.


## **Uso de Whisper+**

Para el uso de whisper, se han creado varias banderas o flags: 

### Banderas sin valores
+ `-v --video`. El archivo de entrada es un video
+ `-a --audio`. El archivo de entrada es un audio
+ `-d --directory`. El tipo de entrada es un directorio con videos o audios

### Banderas con valores 
+  `-i --input`. En esta bandera se especifica la ruta de entrada, ya sea: un video, un audio, o un directorio. 
+  `-m --model`. Whisper AI proporciona varios modelos para el algoritmo de trasncripcion, entre ellos:  tiny.en, tiny, base.en , base, small.en, small, medium.en, medium, large-v1, large-v2, large. Consulte la documentación principal de [Whisper AI](https://github.com/openai/whisper) para más información sobre los modelos. 

## **Algunos ejemplos de uso** 

### **De audio a texto**

Para transformar un solo audio a texto simple, usted puede usar: 

``` 
$ whisper+.py -a -i ./audio.mp3 -m base 
```
  

### **De video a texto**
Para transformar un solo video a texto, usted puede utilizar: 
``` 
$ whisper+.py -v -i ./audio.mp3 -m base 
```

### **De directorio de videos a texto**
Para transformar un directorio que contenga varios videos a texto, usted podrá usar: 


``` 
$ whisper+.py -v -d -i ./folder/ -m base 
```
  
Luego de ejecutar este comando, se obtendrá como resultado, un nuevo directorio denominado _output_ en el cual constan cada uno de los archivos de texto que fueron transformados de los videos antes suministrados. 

### **De directorio de audio a texto***
Para transformar un directorio que contenga varios audios a texto, usted podrá usar: 


``` 
$ whisper+.py -a -d -i ./folder/ -m base 
```
  
Luego de ejecutar este comando, se obtendrá como resultado, un nuevo directorio denominado _output_ en el cual constan cada uno de los archivos de texto que fueron transformados de los audios antes suministrados. 








