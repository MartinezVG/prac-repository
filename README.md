# Practica-repository

# Instalación y utilización modulo monitoring y sensor de el trafico de la Red.

1.- En caso de utilizar windows, instalar Npcap https://nmap.org/npcap/windows-10.html, y wincap https://www.winpcap.org/install/default.htm es una libreria para poder analizar archivos pcap, en este caso es para que python con la libreria scapy pueda  analizar el trafico de la red y guardarlo como formato pcap.



2.- en caso de utilizar windows instalar la terminal de linux \\
        
        * 2.1.- Activar el modo desarrollador \\
        Settings>Update & Security > For Developers.
        
        * 2.2.- Habilita Windows Subsystem for Linux (Beta):
        Control Panel>Programs> Activar o desactivar  las caracteristicas de windows
        Habilitar subsistema de windows para linux
        * 2.3 Descargar terminal de ubuntu para poder utilizar bash ( ya que argus no funciona en windows)
        https://www.microsoft.com/es-cl/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab

3.- Instalar Argus, al igual que la base de datos propuesta por moustafa que fue creada analizada por argus.
Argus procesa los archivos pcap y genera resumenes del trafico. Se analizan ciertos filtros que son aplicados al modelo posteriormente para poder clasificar si es ataque o no.

Para instalar argus en linux: sudo apt-get install argus-server argus-client

Para windows con bash activado: 

        sudo apt-get install build-essential
        sudo apt install flex
        sudo apt install bison
        sudo apt-get update -y
        sudo apt-get install -y libpcap-dev


                ARGUS SERVER
        wget http://qosient.com/argus/dev/argus-3.0.8.2.tar.gz
        tar zxf /argus-3.0.8.2.tar.gz
        cd argus-3.0.8.2
        sudo ./configure
        sudo make
        sudo make install  

                ARGUS CLIENT
        wget http://qosient.com/argus/dev/argus-clients-3.0.8.2.tar.gz
        tar zxf /argus-clients-3.0.8.2.tar.gz
        cd argus-clients-3.0.8.2
        sudo ./configure
        sudo make
        sudo make install  

4.- El modelo fue creado en visual studio code, para ejecutarlo se necesita instalar ciertas librerias con el comando pip en el prompt de python

```
pip install pandas
pip install scapy
pip install graypy
pip install joblib
pip install sklearn
pip install xgboost
```
5.- Cambiar los directorios de el archivo del modelo y del csv que se creará en el script


6.- ejecutar script


# Reporte de Práctica

1. Objetivo de la práctica

Desarrollar un módulo de clasificación de eventos maliciosos entrenados con un dataset público para ser integrado en el subproducto de ciberdefensa.


1.2. Objetivos específicos

         A.Crear Método para clasificar eventos malicios utiizando métodos de machine learning.
         B.Crear Módulo de monitoring.
         C.Crear Módulo de sensoring.
 
 


2.  .- Materiales

        2.1 Computador Intel Core i5-6400 con 16GB Ram para correr los diversos programas para llevar a cabo los objetivos, tales como
        2.2 Jupyter Notebook
        2.3 Visual Studio Code
        2.4 Argus y el respectivo ambiente de ubuntu para hacerlo funcionar
        2.5 Wireshark


3.   .- Procesos y procedimientos

         3.1 Leer lo esscrito anteriormente

4.    .- Contenido académico durante la practica profesional: descripción de nuevas habilidades


          Implementación de técnicas de Data mining para el entendimiento y analisis de la base de datos pública para llevar a cabo el modelo de predicción de eventos maliciosos.
          Utilización de visual studio code con el ambiente de Python para la creación del script que analiza, predice y entrega resultados al graylog.


Conclusión:
Las principales competencias adquiridas en el periodo de práctica temprana fueron limpieza y análisis de la base de datos pública, uso de diversas librerías de Python, preprocesado de nuevos datos para la integración del modelo.

