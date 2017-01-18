# boot_For_The_School
Este bot esta creado con el fin de ahorrar tiempo al momento de evaluar a los profesores de la facultad. 
Para su desarrollo utilize Selenium y los webdrivers tanto de Firefox como de Chrome, en estos momentos los programas que utilizan el driver de Firefox (Todos los que tienen nombre "evaluación") no funcionan correctamente por incompatibilidades con las versiones. 
El programa desarrollado con el driver de Chrome es actualmente operativo. 

Como correrlo:

1. Preparar el ambiente:
    - Este requiere de Selenium instalado (http://selenium-python.readthedocs.io/installation.html), ya sea en un entorno virtual o de manera global, para funcionar correctamente.
    - Si utilizaran un etorno virtual recomiendo virtualvenv con Python 2.7.
    - De igual manera necesita del Webdriver de Chrome para funcionar (https://sites.google.com/a/chromium.org/chromedriver/downloads), este debe descargarse, descomprimirse, y colocarse en el path indicado, en caso de macOS se guarda en /usr/local/bin/"chromedriver".  
  
2. Pasos:

Si utilizaran un entorno virtual:
      
      1. Crearlo: virtualenv --python=python2.7 "nombre_del_entorno"
      
      2. Activarlo: source "nombre_del_entorno"/bin/activate
      
      3. Instalar Selenium: pip install selenium
      
      4. Descargar la herramienta ChromeDriver - Webdriber, descomprimirla, y colocar el descomprimido en el path indicado para cada sistema operativo.
      
      5. Agregar sus correspondientes llaves en el archivo de llaves.py
      
      6. Correrlo: python chrome_driver.py
    
Si no utilizaras un entorno virtual:

      1. installar Selenium de manera global: pip install selenium
      
      2. Descargar la herramienta ChromeDriver - Webdriber (https://sites.google.com/a/chromium.org/chromedriver/downloads), descomprimirla, y colocar el descomprimido en el path indicado para cada sistema operativo.
      
      En el caso de MacOS:
      
        1. Descomprimir el archivo:
        unzip "nombre_del_archivo"
        
        2. Mover el descomprimido a el path correspondiente:
        mv "nombre_del_descomprimido" /usr/local/bin/
        
        3. Reiniciar la terminal.
          
      En el caso de Ubuntu:
      
        1. Descomprimir el archivo:
        unzip "nombre_del_archivo"
            
        2. Mover el descomprimido a el path correspondiente:
        sudo mv "nombre_del_descomprimido" /usr/local/bin/
        
           
        3. Reiniciar la terminal.
        
        5. Agregar sus correspondientes llaves en el archivo de llaves.py
        
        6. Correrlo: python chrome_driver.py
      
** Este programa requiere tanto de Python 2.7 como de su manejador de paquetes PIP para poder funcionar correctamente. 
      
