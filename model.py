import pandas as pd  
import joblib
import subprocess
from scapy.all import *
import logging
import graypy
import sklearn

my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFTLSHandler('localhost', 12201)
my_logger.addHandler(handler)

reloadModel = joblib.load("D:/jupyter/practica/django/djangotut/xgboostmodel.pkl")


snif = sniff(timeout = 5 )
wrpcap('snif.pcap', snif)


subprocess.run('bash  & argus -r snif.pcap -w snif.argus && ra -Lo -s  dur smeansz sbytes ackdat sload dload rate dmeansz dport , -r snif.argus > snif.csv ')


df = pd.read_csv("D:/jupyter/practica/django/snif.csv", sep = '\s+')
df.columns = ('dur','smean','sbytes','ackdat','sload','dload','rate','dmean','port')
df = df.dropna()

df['sload'] = pd.to_numeric(df['sload'].str.rstrip('*'))
df['dload'] = pd.to_numeric(df['dload'].str.rstrip('*'))

# preprocesado del dataframe

for i in range(len(df)):
    df2 = df.drop(columns =['port'])
    a = df2.iloc[[i]]
    if model.predict(a)[0] == 1:
        my_logger.debug('Log {}'.format{df.iloc[[i]]})


    
