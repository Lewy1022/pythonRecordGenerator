# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:13:49 2020

@author: Woland
"""
import cx_Oracle
from random import randrange
import random
import time

class Generator:
    
    def saveToFileInserts(insert):
        file = open("inserty.txt","a")
        file.write(insert+"\n")
        file.close()

    def connect(userName,password,databaseName):
        con = cx_Oracle.connect(''+userName+'/'+password+'@127.0.0.1/'+databaseName+'')
        cur = con.cursor()
    
    
  
    def insertKlient(numberOfInserts):
        

        con = cx_Oracle.connect('s95475/s95475@217.173.198.135:1522/orcltp.iaii.local')
    
        cur = con.cursor()
        
        cur.execute('select count(*) from Klient')
        wartosc = cur.fetchone()
        ostatnieIdKlienta = int(wartosc[0])
    
        cur.execute('select count(*) from Adresy')
        wartosc = cur.fetchone()
        ostatnieIdAdresu = int(wartosc[0])
   
    
        cur.execute('select count(*) from Cennik')
        wartosc = cur.fetchone()
        ostatnieIdKarnetu = int(wartosc[0])
    
    
        cur.execute('select count(*) from Trener')
        wartosc = cur.fetchone()
        ostatnieIdTrenera = int(wartosc[0])
      
    
        cur.execute('select count(*) from Adresy')
        wartosc = cur.fetchone()
        ostatnieIdAdresu = int(wartosc[0])
       
    
        cur.execute('select count(*) from Kontakty')
        wartosc = cur.fetchone()
        ostatnieIdKontaktu = int(wartosc[0])
        
    
    
    
    
        nameFile =open("imiona.txt","r",encoding="utf-8")
    
        nameList = [line.rstrip('\n') for line in open("imiona.txt","r",encoding="utf-8")]
        sureNameList = [line.rstrip('\n') for line in open("nazwiska.txt","r",encoding="utf-8")]
        Generator.saveToFileInserts('\n\n')
        
        for x in range(1,numberOfInserts+1):
            querry ="Insert INTO Klient VALUES ("+str(ostatnieIdKlienta+3)+",'"+nameList[randrange(0,len(nameList)-1)]+"','"+sureNameList[randrange(0,(len(sureNameList)-1))]+"',"+(str(randrange(1,ostatnieIdKarnetu)))+","+(str(randrange(1,ostatnieIdTrenera)))+","+(str(randrange(1,ostatnieIdKontaktu)))+","+(str(randrange(1,ostatnieIdAdresu)))+",TO_DATE('2020/"+str(randrange(1,12))+"/"+str(randrange(1,30))+" 21:02:44', 'yyyy/mm/dd hh24:mi:ss'))"
            cur.execute(querry)
            Generator.saveToFileInserts(querry)
            ostatnieIdKlienta=ostatnieIdKlienta+1
            time.sleep(0.01)
        
    
    
    
        cur.execute('commit')
        
        print('Pomyslnie dodano do tabeli Klient '+str(numberOfInserts)+" wierszy")
        
    def insertTrener(numberOfInserts):
        

        con = cx_Oracle.connect('s95475/s95475@217.173.198.135:1522/orcltp.iaii.local')
    
        cur = con.cursor()
        
        cur.execute('select count(*) from Trener')
        wartosc = cur.fetchone()
        ostatnieIdTrenera = int(wartosc[0])
    

        cur.execute('select count(*) from Adresy')
        wartosc = cur.fetchone()
        ostatnieIdAdresu = int(wartosc[0])
        print(ostatnieIdAdresu)
    
        cur.execute('select count(*) from Kontakty')
        wartosc = cur.fetchone()
        ostatnieIdKontaktu = int(wartosc[0])
        print(ostatnieIdKontaktu)
    
    
    
        Generator.saveToFileInserts('\n\n')
        nameFile =open("imiona.txt","r",encoding="utf-8")
    
        nameList = [line.rstrip('\n') for line in open("imiona.txt","r",encoding="utf-8")]
        sureNameList = [line.rstrip('\n') for line in open("nazwiska.txt","r",encoding="utf-8")]
    
    
        for x in range(1,numberOfInserts+1):
            querry ="Insert INTO Trener VALUES ("+str(ostatnieIdTrenera+1)+",'"+nameList[randrange(0,len(nameList)-1)]+"','"+sureNameList[randrange(0,(len(sureNameList)-1))]+"',"+(str(randrange(1,ostatnieIdKontaktu)))+","+(str(randrange(1,ostatnieIdAdresu)))+")"
            cur.execute(querry)
            Generator.saveToFileInserts(querry)
            ostatnieIdTrenera=ostatnieIdTrenera+1
            time.sleep(0.01)
        
    
    
    
        cur.execute('commit')
        print('Dodawanie wierszy do tabli trener zakonczono pomyslnie')
        
    def insertContacts(numberOfInserts):
        

        con = cx_Oracle.connect('s95475/s95475@217.173.198.135:1522/orcltp.iaii.local')
    
        cur = con.cursor()
     

        cur.execute('select count(*) from Adresy')
        wartosc = cur.fetchone()
        ostatnieIdAdresu = int(wartosc[0])
        print(ostatnieIdAdresu)
    
        cur.execute('select count(*) from Kontakty')
        wartosc = cur.fetchone()
        ostatnieIdKontaktu = int(wartosc[0])
        print(ostatnieIdKontaktu)
    
        Generator.saveToFileInserts('\n\n')
    
    
        nameFile =open("imiona.txt","r",encoding="utf-8")
    
        nameList = [line.rstrip('\n') for line in open("imiona.txt","r",encoding="utf-8")]
        sureNameList = [line.rstrip('\n') for line in open("nazwiska.txt","r",encoding="utf-8")]
    
        
        for x in range(1,numberOfInserts+1):
            querry ="Insert INTO Kontakty VALUES ("+str(ostatnieIdKontaktu+1)+",'"+"+48 "+str(randrange(700000000,799999999))+"',NULL,'"+sureNameList[randrange(0,(len(sureNameList)-1))]+str(randrange(1,100))+"@gmail.com"+"',NULL)"
            cur.execute(querry)
            Generator.saveToFileInserts(querry)
            ostatnieIdKontaktu=ostatnieIdKontaktu+1
            time.sleep(0.01)
        
    
    
    
        cur.execute('commit')
        print('Dodawanie wierszy do tabli Kontakty zakonczono pomyslnie')
        
    def insertAdresses(numberOfInserts):
        
   
            
    
        con = cx_Oracle.connect('s95475/s95475@217.173.198.135:1522/orcltp.iaii.local')
        
        cur = con.cursor()
         
    
        cur.execute('select count(*) from Adresy')
        wartosc = cur.fetchone()
        ostatnieIdAdresu = int(wartosc[0])
        print(ostatnieIdAdresu)
        
        cur.execute('select count(*) from Kontakty')
        wartosc = cur.fetchone()
        ostatnieIdKontaktu = int(wartosc[0])
        print(ostatnieIdKontaktu)
        
    
        Generator.saveToFileInserts('\n\n')
        
        nameFile =open("imiona.txt","r",encoding="utf-8")
        
        nameList = [line.rstrip('\n') for line in open("imiona.txt","r",encoding="utf-8")]
        sureNameList = [line.rstrip('\n') for line in open("nazwiska.txt","r",encoding="utf-8")]
        cityList = [line.rstrip('\n') for line in open("miasta.txt","r",encoding="utf-8")]
        streetList = [line.rstrip('\n') for line in open("ulice.txt","r",encoding="utf-8")]
            
      
        
        #INTO Adresy  VALUES (1, 'Opole',NULL,'Opolskie','Opolski','45-111','MIKOLAJCZYKA','5',NULL)
        for x in range(1,numberOfInserts+1):
            randCityNAme = cityList[randrange(0,(len(cityList)-1))]
            querry ="Insert INTO Adresy VALUES ("+str(ostatnieIdAdresu+1)+",'"+randCityNAme+"',NULL,'"+randCityNAme+"','"+randCityNAme+"','"+str(randrange(1,100))+"-"+str(randrange(100,200))+"','"+streetList[randrange(0,(len(streetList)-1))]+"','"+str(randrange(1,100))+"',NULL)"
            cur.execute(querry)
            Generator.saveToFileInserts(querry)
            ostatnieIdAdresu=ostatnieIdAdresu+1
            time.sleep(0.01)
            
        
        
        
        cur.execute('commit')
        print('Dodawanie wierszy do tabli Adresy zakonczono pomyslnie')
        
    def insertCennik(numberOfInserts):
        
   
            
    
        con = cx_Oracle.connect('s95475/s95475@217.173.198.135:1522/orcltp.iaii.local')
        
        cur = con.cursor()
         
    
        cur.execute('select count(*) from Cennik')
        wartosc = cur.fetchone()
        ostatnieIdCennika = int(wartosc[0])
        print(ostatnieIdCennika)
        
        cur.execute('select count(*) from Kontakty')
        wartosc = cur.fetchone()
        ostatnieIdKontaktu = int(wartosc[0])
        print(ostatnieIdKontaktu)
        
    
        
        

       
        loremIpsum =  open("lorem.txt","r",encoding="utf-8")
        loremIpsum = loremIpsum.read().split(' ')
       
        Generator.saveToFileInserts('\n\n')
        
        #INTO Cennik  VALUES (1,'karnet 3-miesięczny','260')
        for x in range(1,numberOfInserts+1):
            randStr  = ""
            for x in range(1,4):           
                randStr = randStr + loremIpsum[randrange(0,(len(loremIpsum)-1))]+ " "
            querry ="Insert INTO Cennik VALUES ("+str(ostatnieIdCennika+1)+",'"+randStr+"','"+str(randrange(1,666))+"')"
            cur.execute(querry)
            Generator.saveToFileInserts(querry)
            ostatnieIdCennika=ostatnieIdCennika+1
            time.sleep(0.01)
            
        
        
        
        cur.execute('commit')
        print('Dodawanie wierszy do tabli Cennik zakonczono pomyslnie')
        
        
        
        
    def insertCwiczenie(numberOfInserts):
        
   
                

        con = cx_Oracle.connect('s95475/s95475@217.173.198.135:1522/orcltp.iaii.local')
        
        cur = con.cursor()
         
    
        cur.execute('select count(*) from Cwiczenia')
        wartosc = cur.fetchone()
        ostatnieIdCwiczenia = int(wartosc[0])
        print(ostatnieIdCwiczenia)
        
        cur.execute('select count(*) from Kontakty')
        wartosc = cur.fetchone()
        ostatnieIdKontaktu = int(wartosc[0])
        print(ostatnieIdKontaktu)
        
    
        
        

       
        loremIpsum =  open("lorem.txt","r",encoding="utf-8")
        loremIpsum = loremIpsum.read().split(' ')
       
        Generator.saveToFileInserts('\n\n')
        
        #INTO Cwiczenia  VALUES (1,'Wspięcia na palce stojąc ze sztangą na karku','Łydki','na siłę','sztanga','początkujący')
        for x in range(1,numberOfInserts+1):
            randStr  = ""
            randStr2  = ""
            randStr3  = ""
            randStr4  = ""
            randStr5  = ""
            for x in range(1,randrange(2,4)):           
                randStr = randStr + loremIpsum[randrange(0,(len(loremIpsum)-1))]+ " "
            for x in range(1,randrange(2,4)):           
                randStr2 = randStr2 + loremIpsum[randrange(0,(len(loremIpsum)-1))]+ " "
            for x in range(1,randrange(2,4)):           
                randStr3 = randStr3 + loremIpsum[randrange(0,(len(loremIpsum)-1))]+ " "
            for x in range(1,randrange(2,4)):           
                randStr4 = randStr4 + loremIpsum[randrange(0,(len(loremIpsum)-1))]+ " "
            for x in range(1,randrange(2,4)):           
                randStr5 = randStr5 + loremIpsum[randrange(0,(len(loremIpsum)-1))]+ " "
            querry ="Insert INTO Cwiczenia VALUES ("+str(ostatnieIdCwiczenia+1)+",'"+randStr+"','"+randStr2+"','"+randStr3+"','"+randStr4+"','"+randStr5+"')"
            cur.execute(querry)
            Generator.saveToFileInserts(querry)
            ostatnieIdCwiczenia=ostatnieIdCwiczenia+1
            time.sleep(0.01)
            
        
        
        
        cur.execute('commit')
        print('Dodawanie wierszy do tabli Cwiczenia zakonczono pomyslnie')


    def insertGrafik(numberOfInserts):
        
   
            
    
        con = cx_Oracle.connect('s95475/s95475@217.173.198.135:1522/orcltp.iaii.local')
        
        cur = con.cursor()
         
    
        cur.execute('select count(*) from Grafik')
        wartosc = cur.fetchone()
        ostatnieIdGrafiku = int(wartosc[0])
        print(ostatnieIdGrafiku)
        
        cur.execute('select count(*) from Kontakty')
        wartosc = cur.fetchone()
        ostatnieIdKontaktu = int(wartosc[0])
        print(ostatnieIdKontaktu)
        
        cur.execute('select count(*) from Trener')
        wartosc = cur.fetchone()
        ostatnieIdTrenera = int(wartosc[0])

        
    
        
        
        nameFile =open("imiona.txt","r",encoding="utf-8")
        
        nameList = [line.rstrip('\n') for line in open("imiona.txt","r",encoding="utf-8")]
        sureNameList = [line.rstrip('\n') for line in open("nazwiska.txt","r",encoding="utf-8")]
        cityList = [line.rstrip('\n') for line in open("miasta.txt","r",encoding="utf-8")]
        streetList = [line.rstrip('\n') for line in open("ulice.txt","r",encoding="utf-8")]
            
        Generator.saveToFileInserts('\n\n')
        
        #INTO Grafik VALUES (1,1,8.00,16.00)
        for x in range(1,numberOfInserts+1):
            querry ="Insert INTO Grafik VALUES ("+str(ostatnieIdGrafiku+1)+","+str(randrange(1,ostatnieIdTrenera))+","+str(randrange(1,10))+".00"+","+str(randrange(12,20))+".00"+")"
            cur.execute(querry)
            Generator.saveToFileInserts(querry)
            ostatnieIdGrafiku=ostatnieIdGrafiku+1
            time.sleep(0.01)
            
        
        
        
        cur.execute('commit')
        print('Dodawanie wierszy do tabli Grafik zakonczono pomyslnie')

    def insertPlan(numberOfInserts):
        
   
            
    
        con = cx_Oracle.connect('s95475/s95475@217.173.198.135:1522/orcltp.iaii.local')
        
        cur = con.cursor()
         
    
        cur.execute('select count(*) from Plan_treningu')
        wartosc = cur.fetchone()
        ostatnieIdPlanu = int(wartosc[0])
        print(ostatnieIdPlanu)
        
        cur.execute('select id_klienta from Klient')
        wartosc = cur.fetchall()
        ostatnieIdKlienta = wartosc
    
        
        cur.execute('select count(*) from Trener')
        wartosc = cur.fetchone()
        ostatnieIdTrenera = int(wartosc[0])

        
    
        
        
            
        Generator.saveToFileInserts('\n\n')
        klient = ostatnieIdKlienta
        #INTO INTO Plan_treningu VALUES (1,1)
        for x in range(1,numberOfInserts+1):
            klient = ostatnieIdKlienta[randrange(1,len(ostatnieIdKlienta))]
            klient = str(klient[0])
            querry ="Insert INTO Plan_treningu VALUES ("+str(ostatnieIdPlanu+1)+","+str(klient)+")"
            cur.execute(querry)
            Generator.saveToFileInserts(querry)
            ostatnieIdPlanu=ostatnieIdPlanu+1
            time.sleep(0.01)
            
        
        
        
        cur.execute('commit')
        print('Dodawanie wierszy do tabli Plan_treningu zakonczono pomyslnie')


    def insertPlanCwiczen(numberOfInserts):
        
   
            
    
        con = cx_Oracle.connect('s95475/s95475@217.173.198.135:1522/orcltp.iaii.local')
        
        cur = con.cursor()
         
    
        cur.execute('select count(*) from Plan_cwiczen')
        wartosc = cur.fetchone()
        ostatnieIdPlanCwiczen = int(wartosc[0])
        print(ostatnieIdPlanCwiczen)
        
        cur.execute('select count(*) from Kontakty')
        wartosc = cur.fetchone()
        ostatnieIdKontaktu = int(wartosc[0])
        print(ostatnieIdKontaktu)
        
        cur.execute('select count(*) from Trener')
        wartosc = cur.fetchone()
        ostatnieIdTrenera = int(wartosc[0])
        
        cur.execute('select count(*) from Cwiczenia')
        wartosc = cur.fetchone()
        ostatnieIdCwiczenia = int(wartosc[0])
        print(ostatnieIdCwiczenia)
        
        cur.execute('select count(*) from Plan_treningu')
        wartosc = cur.fetchone()
        ostatnieIdPlanu = int(wartosc[0])
        print(ostatnieIdPlanu)

        
    
        
        
        nameFile =open("imiona.txt","r",encoding="utf-8")
        
        nameList = [line.rstrip('\n') for line in open("imiona.txt","r",encoding="utf-8")]
        sureNameList = [line.rstrip('\n') for line in open("nazwiska.txt","r",encoding="utf-8")]
        cityList = [line.rstrip('\n') for line in open("miasta.txt","r",encoding="utf-8")]
        streetList = [line.rstrip('\n') for line in open("ulice.txt","r",encoding="utf-8")]
        loremIpsum =  open("lorem.txt","r",encoding="utf-8")
        loremIpsum = loremIpsum.read().split(' ')
            
        Generator.saveToFileInserts('\n\n')
        
        # INTO Plan_cwiczen VALUES (1,'PN',3,3,1,15 )
        for x in range(1,numberOfInserts+1):
            querry ="Insert INTO Plan_cwiczen VALUES ("+str(ostatnieIdPlanCwiczen+1)+",'"+str(loremIpsum[randrange(1,len(loremIpsum))])+"',"+str(randrange(1,5))+","+str(randrange(1,ostatnieIdCwiczenia))+","+str(randrange(1,ostatnieIdPlanu))+","+str(randrange(1,30))+")"
            cur.execute(querry)
            Generator.saveToFileInserts(querry)
            ostatnieIdPlanCwiczen=ostatnieIdPlanCwiczen+1
            time.sleep(0.01)
            
        
        
        
        cur.execute('commit')
        print('Dodawanie wierszy do tabli Plan_cwiczen zakonczono pomyslnie')


    def insertRejestrWejsc(numberOfInserts):
        
   
            
    
        con = cx_Oracle.connect('s95475/s95475@217.173.198.135:1522/orcltp.iaii.local')
        
        cur = con.cursor()
         
    
        cur.execute('select count(*) from Rejestr_wejsc_wyjsc')
        wartosc = cur.fetchone()
        ostatnieIdRejestr_wejsc_wyjsc = int(wartosc[0])
        print(ostatnieIdRejestr_wejsc_wyjsc)
        
        cur.execute('select count(*) from Kontakty')
        wartosc = cur.fetchone()
        ostatnieIdKontaktu = int(wartosc[0])
        print(ostatnieIdKontaktu)
        
        cur.execute('select count(*) from Trener')
        wartosc = cur.fetchone()
        ostatnieIdTrenera = int(wartosc[0])
        
        cur.execute('select count(*) from Cwiczenia')
        wartosc = cur.fetchone()
        ostatnieIdCwiczenia = int(wartosc[0])
        print(ostatnieIdCwiczenia)
        
        cur.execute('select count(*) from Plan_treningu')
        wartosc = cur.fetchone()
        ostatnieIdPlanu = int(wartosc[0])
        print(ostatnieIdPlanu)
        
        cur.execute('select id_klienta from Klient')
        wartosc = cur.fetchall()
        ostatnieIdKlienta = wartosc
    

        
    
        
        
        Generator.saveToFileInserts('\n\n')
        
        # INTO Rejestr_wejsc_wyjsc VALUES (1,1,TO_TIMESTAMP( '2019-03-02 14:53:20','YYYY-MM-DD HH24:MI:SS'),TO_TIMESTAMP( '2019-03-02 16:33:20','YYYY-MM-DD HH24:MI:SS') )

        for x in range(1,numberOfInserts+1):
            klient = ostatnieIdKlienta[randrange(1,len(ostatnieIdKlienta))]
            klient = str(klient[0])
            querry ="Insert INTO Rejestr_wejsc_wyjsc VALUES ("+str(ostatnieIdRejestr_wejsc_wyjsc+1)+","+klient+",TO_TIMESTAMP( '2019-03-02 14:53:20','YYYY-MM-DD HH24:MI:SS'),TO_TIMESTAMP( '2019-03-02 16:33:20','YYYY-MM-DD HH24:MI:SS'))"
            cur.execute(querry)
            Generator.saveToFileInserts(querry)
            ostatnieIdRejestr_wejsc_wyjsc=ostatnieIdRejestr_wejsc_wyjsc+1
            time.sleep(0.01)
            
        
        
        
        cur.execute('commit')
        print('Dodawanie wierszy do tabli Rejestr_wejsc_wyjsc zakonczono pomyslnie')
