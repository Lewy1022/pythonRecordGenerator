# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:58:58 2020

@author: Woland
"""
import cx_Oracle
from random import randrange

import time
from generatorLibrary import  Generator
import sys


con = cx_Oracle.connect('s95475/s95475@217.173.198.135:1522/orcltp.iaii.local')


"""
cur = con.cursor()
cur.execute('select count(*) from Trener')
wartosc = cur.fetchone()
ostatnieIdKlienta = int(wartosc[0])
"""


#Generator.connect('hr','hr','orcl4')

if len(sys.argv)==3:
    print('pierwszy argument:' + sys.argv[1])  
    if sys.argv[1]=='klient' or sys.argv[1]=='Klient':
         Generator.insertKlient(int(sys.argv[2]))
    elif sys.argv[1]=='Trener' or sys.argv[1]=='trener':
        Generator.insertTrener(int(sys.argv[2]))
    elif sys.argv[1]=='Kontakty' or sys.argv[1]=='kontakty':
        Generator.insertContacts(int(sys.argv[2]))
    elif sys.argv[1]=='cennik' or sys.argv[1]=='Cennik':
        Generator.insertCennik(int(sys.argv[2]))
    elif sys.argv[1]=='Cwiczenia' or sys.argv[1]=='cwiczenia':
        Generator.insertCwiczenie(int(sys.argv[2]))
    elif sys.argv[1]=='Grafik' or sys.argv[1]=='grafik':
        Generator.insertGrafik(int(sys.argv[2]))
    elif sys.argv[1]=='plan_treningu' or sys.argv[1]=='Plan_treningu':
        Generator.insertPlan(int(sys.argv[2]))
    elif sys.argv[1]=='Plan_cwiczen' or sys.argv[1]=='plan_cwiczen':
        Generator.insertPlanCwiczen(int(sys.argv[2]))
    elif sys.argv[1]=='Rejestr_wejsc_wyjsc' or sys.argv[1]=='rejestr_wejsc_wyjsc':
        Generator.insertRejestrWejsc(int(sys.argv[2]))
    elif sys.argv[1]=='Adresy' or sys.argv[1]=='adresy':
        Generator.insertAdresses(int(sys.argv[2]))
        
        
        
else:
    print('bledna liczba argumentow')

