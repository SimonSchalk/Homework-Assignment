# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 08:44:30 2020

@author: Simon
"""

"""
Author:         Simon Schalk S1910632012
Title:          Schaltjahr
Discription:    Ueberpuefung ob ein beliebiges Jahr ein Schaltjahr ist.
Last Change:    03.01.2020
"""

#Funktion zur Schaltjahr-Berechnung
def Schaltjahr(j):
        """j = int(input("Zu ueberpruefendes Jahr:  "))"""
        if j % 4 == 0:
                if j % 100 == 0:
                    
#Wenn Jahr durch 4 teilbar aber nicht durch 100 teilbar, dann Schaltjahr 
                        if j % 400 == 0:
                                print(str(j), " ist ein Schaltjahr!")
                                
#Wenn Jahr durch 100 teilbar aber nicht durch 400 teilbar, dann KEIN Schaltjahr  
                        else:
                                print(str(j), " ist KEIN Schaltjahr!")
#Gegenteilsfaelle fuer alle anderen Moeglichkeiten
                else:
                        print(str(j), " ist ein Schaltjahr!")
        else:
                print(str(j), " ist KEIN Schaltjahr!")


