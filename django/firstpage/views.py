from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail 
from django.utils import timezone
import datetime
import email
import pandas as pd
import pymongo
from pymongo import MongoClient
from bson.raw_bson import RawBSONDocument
import json
client = MongoClient('localhost')

db = client['traficoDB']
col = db['traficoTabla']



print (client.list_database_names())
   


# Create your views here.

import joblib
reloadModel = joblib.load("D:/jupyter/tesis/xgboostmodel2.pkl")

loaded_model = joblib.load("D:/jupyter/tesis/xgboostmodelmulti.pkl")

def index(request):
    context = {'a': 'a'}
    return render(request,'index.html', context)
    return HttpResponse({'a':1}) 

def predictMPG(request):
    print (request)
    if request.method == "POST":
        temp = {}
        temp['sbytes'] = request.POST.get('sbytes')
        temp['smean'] = request.POST.get('smean')
        temp['ct_srv_src'] = request.POST.get('ct_srv_src')
        temp['sload'] = request.POST.get('sload')
        temp['synack'] = request.POST.get('synack')
        temp['ct_srv_dst'] = request.POST.get('ct_srv_dst')
        temp['ct_dst_src_ltm'] = request.POST.get('ct_dst_src_ltm')



    testDtaa=pd.DataFrame({'x':temp}).transpose().astype(float)
    print (testDtaa.dtypes)
    scoreval = reloadModel.predict(testDtaa)[0]
    multival = loaded_model.predict(testDtaa)[0]
    if multival == 0:
        multival = "Analysis"
    if multival == 1:
        multival = "Backdoor"
    if multival == 2: 
        multival = 'DoS'
    if multival == 3:
        multival = 'Exploits'
    if multival == 4:
        multival = "Fuzzers"
    if multival == 5:
        multival = "Generic"
    if multival == 6:
        multival = "Normal"
    if multival == 7:
        multival = "Reconnaissance"
    if multival == 8:
        multival = "Shellcode"
    if multival == 9:
        multival == "Worms"
    print (testDtaa)
    fck = timezone.now()
    print (fck)
    if scoreval == 1:
        send_mail(
            fck ,
            'Posible ataque: '+ multival + "    Log :" + str(temp),
            'vicentebott@gmail.com',
            ['vicentebott@gmail.com'],
        )
    temp2 = {json.dumps(temp):json.dumps(temp)}
    
    result = col.insert_one(temp2).inserted_id
    for r in col.find():
        print(r)

    context={'scoreval':scoreval,'r':r , 'multival': multival, 'temp': temp, 'send_mail':send_mail}
    
    return render(request,'index.html', context)


def viewDatabase(request):
    results_count = col.count()
    for r in col.find({}):
        r
    context={'r':r,'results_count':results_count}
    return render(request,'viewDB.html', context)

def updateDataBase(request):
    return render(request,'updateDataBase.html', context)

