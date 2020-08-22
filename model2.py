import pandas as pd  
import joblib
import subprocess
from scapy.all import *
import logging
import graypy
import sklearn
import joblib
import threading

my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFUDPHandler('localhost', 12201)
my_logger.addHandler(handler)

model = joblib.load("D:/jupyter/tesis/modelbi.pkl")
modelo = joblib.load("D:/jupyter/tesis/modelmulti.pkl")


snif = sniff(timeout = 10)
wrpcap('snif.pcap', snif)


subprocess.run('bash  & argus -r snif.pcap -w snif.argus && ra -Lo -s  dur smeansz sbytes ackdat sload dload dmeansz dport , -r snif.argus > snif.csv ')


df = pd.read_csv("D:/jupyter/practica/django/snif.csv", sep = '\s+')
df.columns = ('dur','smean','sbytes','ackdat','sload','dload','dmean','port')


df = df.dropna()

df['sload'] = pd.to_numeric(df['sload'].str.rstrip('*'))
df['dload'] = pd.to_numeric(df['dload'].str.rstrip('*'))
df = df[df.dur != 0]


# preprocesado del dataframe




for i in range(len(sniff)):
    df2 = df.drop(columns =['port'])
    a = df2.iloc[[i]]
    if model.predict(a)[0] == 1:
        multival = modelo.predict(a)[0]
        if multival == 0:
            multival = "Analysis"
        elif multival == 1:
            multival = "Backdoor"
        elif multival == 2: 
            multival = 'DoS'
        elif multival == 3:
            multival = 'Exploits'
        elif multival == 4:
            multival = "Fuzzers"
        elif multival == 5:
            multival = "Generic"
        elif multival == 7:
            multival = "Reconnaissance"
        elif multival == 8:
            multival = "Shellcode"
        elif multival == 9:
            multival == "Worms"
        threading.current_thread().name = multival
        
        my_logger.debug('Log {}'.format(df.iloc[[i]])) 