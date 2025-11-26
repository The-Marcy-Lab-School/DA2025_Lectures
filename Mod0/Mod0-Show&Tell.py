# Load the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

#import csv file
df = pd.read_csv('cybersecurity_attacks.csv')


df['timestamp'] = pd.to_datetime(df['Timestamp'])

#Extracting the month from the timestamp column
df['month'] = pd.to_datetime(df['timestamp']).dt.month
#print(df['month])

#Converting the number of the month to the name of the month
name_month = []

#Counting total attacks per month
JanCounter = 0
FebCounter = 0
MarCounter = 0
AprCounter = 0
MayCounter = 0
JunCounter = 0
JulCounter = 0
AugCounter = 0
SepCounter = 0
OctCounter = 0
NovCounter = 0
DecCounter = 0

for month in df['month']:
    if month == 1:
        month = "January"
        name_month.append(month)
        JanCounter += 1
    elif month == 2:
        month = "February"
        name_month.append(month)
        FebCounter += 1
    elif month == 3:
        month = "March"
        name_month.append(month)
        MarCounter += 1
    elif month == 4:
        month = "April"
        name_month.append(month)
        AprCounter += 1
    elif month == 5:
        month = "May"
        name_month.append(month)
        MayCounter += 1
    elif month == 6:
        month = "June"
        name_month.append(month)
        JunCounter += 1
    elif month == 7:
        month = "July"
        name_month.append(month)
        JulCounter += 1
    elif month == 8:
        month = "August"
        name_month.append(month)
        AugCounter += 1
    elif month == 9:
        month = "September"
        name_month.append(month)
        SepCounter += 1
    elif month == 10:
        month = "October"
        name_month.append(month)
        OctCounter += 1
    elif month == 11:
        month = "November"
        name_month.append(month)
        NovCounter += 1
    elif month == 12:
        month = "December"
        name_month.append(month)
        DecCounter += 1


#Counting total attacks per category
malware   = [e for e in df["Attack Type"] if e == "Malware"]
ddos      = [e for e in df["Attack Type"] if e == "DDoS"]
intrusion = [e for e in df["Attack Type"] if e == "Intrusion"]

#print(len(malware)) #13307
#print(len(ddos)) #13428 
#print(len(intrusion)) #13265

#Discovered zip which allows to consider two parameters together
JanMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 1]
totalJanMalwareCount = len(JanMalwareCount)

FebMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 2]
totalFebMalwareCount = len(FebMalwareCount)

MarMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 3]
totalMarMalwareCount = len(MarMalwareCount)

AprMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 4]
totalAprMalwareCount = len(AprMalwareCount)

MayMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 5]
totalMayMalwareCount = len(MayMalwareCount)

JunMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 6]
totalJunMalwareCount = len(JunMalwareCount)

JulMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 7]
totalJulMalwareCount = len(JulMalwareCount)

AugMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 8]
totalAugMalwareCount = len(AugMalwareCount)

SepMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 9]
totalSepMalwareCount = len(SepMalwareCount)

OctMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 10]
totalOctMalwareCount = len(OctMalwareCount)

NovMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 11]
totalNovMalwareCount = len(NovMalwareCount)

DecMalwareCount = [e for e, month in zip(df["Attack Type"], df["month"]) if e == "Malware" and month == 12]
totalDecMalwareCount = len(DecMalwareCount)


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
total_attacks = [JanCounter, FebCounter, MarCounter, AprCounter, MayCounter, JunCounter, JulCounter, AugCounter, SepCounter, OctCounter, NovCounter, DecCounter]
malware_attacks = [totalJanMalwareCount, totalFebMalwareCount, totalMarMalwareCount, totalAprMalwareCount, totalMayMalwareCount, totalJunMalwareCount, totalJulMalwareCount, totalAugMalwareCount, totalSepMalwareCount, totalOctMalwareCount, totalNovMalwareCount, totalDecMalwareCount]


#Another example of for loops to print the output
print("Month\tTotal Attacks\tMalware Attacks")
for i in range(len(months)):
    print(f"{months[i]}.\t{total_attacks[i]}\t\t{malware_attacks[i]}")






