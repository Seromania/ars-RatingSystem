# -*- coding: cp1252 -*-
import StringIO
import codecs
from arsapi import SeroARSAPI

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

        dataapi = SeroARSAPI(id)
        
        Staatsname = dataapi.getData("Statesname")
        Staatseinkommen = dataapi.getData("Total state income")
        Staatsschulden = dataapi.getData("National debt")
        Neuverschuldung= dataapi.getData("New indebtedness")
        Zinszahlungen = dataapi.getData("Payment of interest")
        Beliebtheit = dataapi.getData("Popularity-Regent")
        Weltruf = dataapi.getData("Int. reputation-Regent")
        Einfluss = dataapi.getData("Influence-Regent")
        Wahlen = dataapi.getData("Elections-Regent")
        BIP = dataapi.getData("Gross domestic product")
        Wirtschaft = dataapi.getData("Economy growth")
        Staatenklasse = dataapi.getData("Staatenklasse")

                
            
        Rf = (float(Beliebtheit) + float(Einfluss)) * (float(Wahlen.split("%")[0]) / 100)

        #print("       Staatsname: %s" % Staatsname)
        #print("    Staatenklasse: %s" % Staatenklasse)
        #print("               Rf: %s" % Rf)
        #print("              BIP: %s" % BIP)
        #print(" vorj. Wirtschaft: %s" % Wirtschaft)
        #print("  Staatseinkommen: %s" % Staatseinkommen)
        #print("   Staatsschulden: %s" % Staatsschulden)
        #print("  Neuverschuldung: %s" % Neuverschuldung)
        #print("    Zinszahlungen: %s" % Zinszahlungen)
        
        if float(Weltruf) < 0:
            Wruf = -float(Rf);
        if float(Weltruf) >= 0:
            Wruf = Weltruf     
        #print("             Wruf: %s" % Wruf)

        STf = float(Rf) + float(Wruf)

        if float(STf) > 1:
            STf = float(STf) - (int(STf) - 1)
        if float(STf) < 0:
            STf = 0
        #print("             STf: %s\n" % STf)

        X1 = float(Staatsschulden) / float(BIP) * 100
        X2 = float(Neuverschuldung) / float(BIP) * 100
        X3 = float(Zinszahlungen) / float(Staatseinkommen) * 100
        

        #print("X1: %s || X2: %s || X3: %s" % (X1, X2, X3))

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


        #print("            X4: %s" % X4)
     
        #print("X1: %s || X2: %s || X3: %s || X4: %s" % (X1, X2, X3, X4))

        RatingPunkte = X1 + X2 + X3 + X4 + STf
        #print("\n   Ratingpunkte: %s" % RatingPunkte)
        if str(Staatenklasse) == "Supermacht" or str(Staatenklasse) == "Industriemacht":
            RatingPunkte += 3
        elif str(Staatenklasse) == "Rohstoffmacht":
            RatingPunkte += 1
        elif str(Staatenklasse) == "postkommunistisch" or str(Staatenklasse) == "fundamentalistisch" or str(Staatenklasse) == "Entwicklungsland":
            RatingPunkte -= 1
        #print("   Ratingpunkte: %s" % RatingPunkte)

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

        #print("     Vorzeichen: %s" % Vorzeichen)
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
        #print("         Rating: %s%s" % (Rating,Vorzeichen))

        file = codecs.open('rating.csv', 'a+', 'iso-8859-15')
        file.write("%s;%s%s\n" % (Staatsname, Rating, Vorzeichen))
        file.close()
        

        
if __name__ == "__main__":
    SR = SerosRating()
    SR.getCountryIDs("states.txt")
    SR.GetCountryRates()
    
