# -*- coding: cp1252 -*-
import urllib2
import StringIO
import lxml.html as lh
import codecs

class SerosRating(object):
    """SerosRating for Ars-Regendi"""

    def __init__(self):
        self.Staaten = []
        self.FoundData = 0
        self.currentStID = 0
        
    def getCountryIDs(self,Filename):
        #reads the IDs of the countrys in Filename
        stateobj = open(Filename, "r")
        for line in stateobj:
            #print line.rstrip()
            self.Staaten.append(line.rstrip())
        stateobj.close()

    def GetCountryRates(self):
        #Just a test, will delete it later
        for stateid in self.Staaten:
            #print ("http://de.ars-regendi.com/state/%s/show.html" % stateid)
            self.getHTML(stateid)
        print ("==================================================")
    
    def getHTML(self, id):
        #Get the Data of a Country
        print ("====NEW STATE====")
        print ("Current State: %s \n" % id)

        response = urllib2.urlopen("http://de.ars-regendi.com/state/%s/haushalt.html" % id)
        line = ""
        content = response.read()
        tree = lh.fromstring(content)
        for key, status in zip(*[iter(tree.xpath('//td/text()'))]*2):
            if status.split(" ")[0] == "Durchschnittsstaat":
               #print("Key: %s || Status: %s " % (key, status))
               Staatsname = key
            if key == "Gesamtes Staatseinkommen":
                #print("Key: %s || Status: %s " % (key, status.replace('.','').replace(',','.')))
                Staatseinkommen = status.split()[0].replace('.','').replace(',','.')
            if key == "Staatsschulden":
                #print("Key: %s || Status: %s " % (key, status.replace('.','').replace(',','.')))
                Staatsschulden = status.split()[0].replace('.','').replace(',','.')
            if key == "Neuverschuldung":
               # print("Key: %s || Status: %s " % (key, status.replace('.','').replace(',','.')))
                Neuverschuldung= status.split()[0].replace('.','').replace(',','.')
            if key == "Zinszahlungen":
                #print("Key: %s || Status: %s " % (key, status.replace('.','').replace(',','.')))
                Zinszahlungen = status.split()[0].replace('.','').replace(',','.')
        
        response = urllib2.urlopen("http://de.ars-regendi.com/state/%s/regent.html" % id)
        line = ""
        content = response.read()
        tree = lh.fromstring(content)
        for key, status in zip(*[iter(tree.xpath('//td/text()'))]*2):
            if key == "Beliebtheit":
                #print("Key: %s || Status: %s " % (key, status))
                Beliebtheit = status
            if key == "Weltruf":
                print("Key: %s || Status: %s " % (key, status))
                Weltruf = status
            if key == "Einfluss":
                #print("Key: %s || Status: %s " % (key, status))
                Einfluss = status
            if key == "Wahlen":
                #print("Key: %s || Status: %s " % (key, status.split("/")[1]))
                Wahlen = status.split("/")[1]

        response = urllib2.urlopen("http://de.ars-regendi.com/state/%s/detail6.html" % id)
        line = ""
        content = response.read()
        tree = lh.fromstring(content)
        for key, status in zip(*[iter(tree.xpath('//td/text()'))]*2):
            if key == "Bruttoinlandsprodukt":
                #print("Key: %s || Status: %s " % (key, status.split()[-3].replace('.','').replace(',','.')))
                BIP = status.split()[-3].replace('.','').replace(',','.')
            if key == "Wirtschaft Vorjahr":
                #print("Key: %s || Status: %s " % (key, status.split()[-2].replace('.','').replace(',','.')))
                Wirtschaft = status.split()[-2].replace('.','').replace(',','.')
            
        response = urllib2.urlopen("http://de.ars-regendi.com/state/%s/show.html" % id)
        line = ""
        content = response.read()
        tree = lh.fromstring(content)
                
        for key in zip(*[iter(tree.xpath('//p/text()'))]*1):
            #print("Key: %s" % key)
            tempstr = str(key)
            if tempstr.find("eingestufte") != -1:
                #print("key: %s" % tempstr)
                staatbesch = tempstr.split()
                #print(staatenklasse)
                count = 0
                for i in staatbesch:
                    if i == "eingestufte":
                        #print("Gefunden: %s" % count)
                        #print("Staatenklasse: %s" % staatenklasse[count-1])
                        Staatenklasse = staatbesch[count-1]
                    else:
                        count += 1
                
            
        Rf = (float(Beliebtheit) + float(Einfluss)) * (float(Wahlen.split("%")[0]) / 100)

        print("       Staatsname: %s" % Staatsname)
        print("    Staatenklasse: %s" % Staatenklasse)
        print("               Rf: %s" % Rf)
        print("              BIP: %s" % BIP)
        print(" vorj. Wirtschaft: %s" % Wirtschaft)
        print("  Staatseinkommen: %s" % Staatseinkommen)
        print("   Staatsschulden: %s" % Staatsschulden)
        print("  Neuverschuldung: %s" % Neuverschuldung)
        print("    Zinszahlungen: %s" % Zinszahlungen)
        
        if float(Weltruf) < 0:
            Wruf = -float(Rf);
        if float(Weltruf) >= 0:
            Wruf = Weltruf     
        print("             Wruf: %s" % Wruf)

        STf = float(Rf) + float(Wruf)

        if float(STf) > 1:
            STf = float(STf) - (int(STf) - 1)
        if float(STf) < 0:
            STf = 0
        print("             STf: %s\n" % STf)

        X1 = float(Staatsschulden) / float(BIP) * 100
        X2 = float(Neuverschuldung) / float(BIP) * 100
        X3 = float(Zinszahlungen) / float(Staatseinkommen) * 100
        

        print("X1: %s || X2: %s || X3: %s" % (X1, X2, X3))

        if X1 < -150:
            X1 = 0
        elif X1 < -100 and X1 > -150:
            X1 = 1
        elif X1 < -80 and X1 > -100:
            X1 = 2
        elif X1 < -50 and X1 > -80:
            X1 = 3
        elif X1 < -30 and X1 > -50:
            X1 = 4
        elif X1 > -30:
            X1 = 5

        if X2 < -6:
            X2 = 0
        elif X2 < -3:
            X2 = 1
        elif X2 < 0:
            X2 = 2
        elif X2 > 0:
            X2 = 3

        if X3 < -10:
            X3 = 0
        elif X3 < -8:
            X3 = 1
        elif X3 < -6:
            X3 = 2
        elif X3 < -3:
            X3 = 3
        elif X3 < 0:
            X3 = 4;
        elif X3 > 0:
            X3 = 5; 


        ##Staatenklassenabhaengig
        _Supermacht = 2.0
        _Industriemacht = 2.2
        _Rohstoffmacht = 1.9
        _Schwellenland = 2.5
        _Industrieland = 1.9
        _Postkommunistisch = 2.3
        _Fundamentalistisch = 2.6
        _Entwicklungsland = 1.3

        if str(Staatenklasse) == "Supermacht":
            if float(Wirtschaft) >= _Supermacht:
                X4 = 2
            elif float(Wirtschaft) > 0 and float(Wirtschaft) < _Supermacht:
                X4 = 1
            elif float(Wirtschaft) == 0:
                X4 = 0
            elif float(Wirtschaft) < 0:
                X4 = -1
            
        elif str(Staatenklasse) == "Industriemacht":
            if float(Wirtschaft) >= _Industriemacht:
                X4 = 2
            elif float(Wirtschaft) > 0 and float(Wirtschaft) < _Industriemacht:
                X4 = 1
            elif float(Wirtschaft) == 0:
                X4 = 0
            elif float(Wirtschaft) < 0:
                X4 = -1
                
        elif str(Staatenklasse) == "Rohstoffmacht":
            if float(Wirtschaft) >= _Rohstoffmacht:
                X4 = 2
            elif float(Wirtschaft) > 0 and float(Wirtschaft) < _Rohstoffmacht:
                X4 = 1
            elif float(Wirtschaft) == 0:
                X4 = 0
            elif float(Wirtschaft) < 0:
                X4 = -1
                
        elif str(Staatenklasse) == "Schwellenland":
            if float(Wirtschaft) >= _Schwellenland:
                X4 = 2
            elif float(Wirtschaft) > 0 and float(Wirtschaft) < _Schwellenland:
                X4 = 1
            elif float(Wirtschaft) == 0:
                X4 = 0
            elif float(Wirtschaft) < 0:
                X4 = -1

        elif str(Staatenklasse) == "Industrieland":
            if float(Wirtschaft) >= _Industrieland:
                X4 = 2
            elif float(Wirtschaft) > 0 and float(Wirtschaft) < _Industrieland:
                X4 = 1
            elif float(Wirtschaft) == 0:
                X4 = 0
            elif float(Wirtschaft) < 0:
                X4 = -1

                
        elif str(Staatenklasse) == "postkommunistisch":
            if float(Wirtschaft) >= _Postkommunistisch:
                X4 = 2
            elif float(Wirtschaft) > 0 and float(Wirtschaft) < _Postkommunistisch:
                X4 = 1
            elif float(Wirtschaft) == 0:
                X4 = 0
            elif float(Wirtschaft) < 0:
                X4 = -1
                
        elif str(Staatenklasse) == "fundamentalistisch":
            if float(Wirtschaft) >= _Fundamentalistisch:
                X4 = 2
            elif float(Wirtschaft) > 0 and float(Wirtschaft) < _Fundamentalistisch:
                X4 = 1
            elif float(Wirtschaft) == 0:
                X4 = 0
            elif float(Wirtschaft) < 0:
                X4 = -1
                
        elif str(Staatenklasse) == "Entwicklungsland":
            if float(Wirtschaft) >= _Entwicklungsland:
                X4 = 2
            elif float(Wirtschaft) > 0 and float(Wirtschaft) < _Entwicklungsland:
                X4 = 1
            elif float(Wirtschaft) == 0:
                X4 = 0
            elif float(Wirtschaft) < 0:
                X4 = -1


        print("            X4: %s" % X4)
     
        print("X1: %s || X2: %s || X3: %s || X4: %s" % (X1, X2, X3, X4))

        RatingPunkte = X1 + X2 + X3 + X4 + STf
        print("\n   Ratingpunkte: %s" % RatingPunkte)
        if str(Staatenklasse) == "Supermacht" or str(Staatenklasse) == "Industriemacht":
            RatingPunkte += 3
        elif str(Staatenklasse) == "Rohstoffmacht":
            RatingPunkte += 1
        elif str(Staatenklasse) == "postkommunistisch" or str(Staatenklasse) == "fundamentalistisch" or str(Staatenklasse) == "Entwicklungsland":
            RatingPunkte -= 1
        print("   Ratingpunkte: %s" % RatingPunkte)

        Vorzeichenliste = []
        Vorzeichenliste.append(X1)
        Vorzeichenliste.append(X2)
        Vorzeichenliste.append(X3)
        Vorzeichenliste.append(X4)
        Vorzeichenliste.sort()

        Vorzeichen = ""
        if (int(Vorzeichenliste[3]) - int(Vorzeichenliste[2])) >= 2:
            Vorzeichen = "+"
        if (int(Vorzeichenliste[1]) - int(Vorzeichenliste[0])) >= 2:
            if Vorzeichen == "+":
                Vorzeichen = ""
            else:
                Vorzeichen = "-"

        print("     Vorzeichen: %s" % Vorzeichen)
        """
        Rating Tabelle:
        AAA: 15 - 16
         AA: 13 - 15
          A: 11 - 13
        BBB: 09 - 11
         BB: 08 - 19
          B: 06 - 08
        CCC: 04 - 06
         CC: 02 - 04
          C: 01 - 02
          D:  0
        """
        
        Rating = "NR"
        if int(RatingPunkte) >= 15:
            Rating = "AAA"
        elif int(RatingPunkte) >= 13 and int(RatingPunkte) < 15:
            Rating = "AA"
        elif int(RatingPunkte) >= 11 and int(RatingPunkte) < 13:
            Rating = "A"
        elif int(RatingPunkte) >= 9 and int(RatingPunkte) < 11:
            Rating = "BBB"
        elif int(RatingPunkte) >= 8 and int(RatingPunkte) < 9:
            Rating = "BB"
        elif int(RatingPunkte) >= 6 and int(RatingPunkte) < 8:
            Rating = "B"
        elif int(RatingPunkte) >= 4 and int(RatingPunkte) < 6:
            Rating = "CCC"
        elif int(RatingPunkte) >= 2 and int(RatingPunkte) < 4:
            Rating = "CC"
        elif int(RatingPunkte) >= 1 and int(RatingPunkte) < 2:
            Rating = "C"
        elif int(RatingPunkte) < 1:
            Rating = "D"
        if Rating == "AAA" or Rating == "D":
            Vorzeichen = ""
        print("         Rating: %s%s" % (Rating,Vorzeichen))

        file = codecs.open('rating.csv', 'a+', 'iso-8859-15')
        file.write("%s;%s%s\n" % (Staatsname, Rating, Vorzeichen))
        file.close()
        

        
if __name__ == "__main__":
    SR = SerosRating()
    SR.getCountryIDs("states.txt")
    SR.GetCountryRates()
    #SR.getHTML(137078)
