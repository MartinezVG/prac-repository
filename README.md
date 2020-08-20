# prac-repository

Instalación y como utilizar modulo monitoring y sensor de el trafico de la Red.

1.- instalar Npcap https://nmap.org/npcap/windows-10.html, es una libreria para poder analizar archivos pcap, en este caso es para que python con la librearia scapy pueda 
analizar el trafico de la red y guardarlo como formato pcap.

2.- Instalar Argus, al igual que la base de datos propuesta por moustafa que fue creada analizada por argus.
Argus procesa los archivos pcap y genera resumenes del trafico. Se analizan ciertos filtros que son aplicados al modelo posteriormente para poder clasificar si es ataque o no.
para ubuntu: sudo apt-get install argus-server argus-client

3.- El modelo fue creado en visual studio code, para ejecutarlo se necesita instalar ciertas librerias con el comando pip en el prompt de python

pip install pandas
pip install scapy
pip install graypy
pip install joblib
pip install sklearn

4.- Cambiar los directorios de el archivo del modelo y del csv que se creará
5.- ejecutar script
