# dit script kijkt naar de katalon output bestanden en kijkt naar het tijd verschil tussen somige instructies en zet alle informatie in een grafiek

import datetime
import time
import re
import statistics
import glob, os
import matplotlib.pyplot as plt
from pathlib import Path

#bestand te openen
f = open('stdout-6.log', "r")
bestand = f.read()
#print(bestand)
#split alle values om er een lijst van te maken
bestandlist=bestand.split('2020')
#de eerste tijd te selecteren zodat ik weet wanneer de monitoring begon
timevalue=bestand[12:20]
eerstetijd= datetime.datetime.strptime(timevalue, '%H:%M:%S')
#print(timevalue)
plugtijd=[]
plugval=[]
logintijd=[]
loginvalue=[]
timeval = datetime.datetime.strptime(timevalue, '%H:%M:%S')
#print(type(timeval))
#print(bestandlist)
datum=bestand[1:11]#zodat ik weet wanneer de monitoring begon
tijd=bestand[12:20] #de eerste tijd te selecteren zodat ik weet wanneer de monitoring begon
print(datum+':'+tijd)
datum=datum+':'+tijd

#print(datum,'dit is de datum')
#print(bestand)
for x in bestandlist[1:-1]:
    #selecteerd de datum
    timevalue2=x[7:15]
    #print('dit is de timevalue:',timevalue2)
    #print(x)
    #veranderd de tijd in een leesbare datum
    timeval2 = datetime.datetime.strptime(timevalue2, '%H:%M:%S')
    #print(timevalue)
    time_delta1 = (timeval2 - timeval) #berekent het tijd verschil tussen de tijd van deze iterarition en de vorige
    #print(time_delta1)
    total_seconds = time_delta1.total_seconds()# de tijd tussen de twee values in seconde
    #print(total_seconds)
    #print(total_seconds)
    timeval=timeval2
    timeval3=str(timevalue2)
    timeval4=timeval3.strip(' ')
    #print(timeval4)
    #print(timeval4)

    #deze twee regels zetten alle informatie in een list om in een grafiek te stoppen, ik heb specifiek deze informatie gekozen want het was de meest representatief van het laden van de website
    if "[MESSAGE][PASSED] - Navigate to 'https://dev.future.ngo/wp-admin/plugins.php' successfully" in x:
        plugtijd.append(timeval4)
        plugval.append(float(total_seconds))
    if "[MESSAGE][PASSED] - Object: 'Object Repository/Page_Login  Toekomstfonds/input_Onthoud mij_wp-submit' is clicked on" in x:
        logintijd.append(timeval4)
        loginvalue.append(float(total_seconds))
    #deze regels kijkt of er een proces was dat langer dan 8 seconden duurde er print het process
    if total_seconds>8:

        print('waarschuwing')
        print('dit stuk duurt te lang')
        x2=x.strip('\n')
        print(x2)
        time_delta2 = (timeval2 - eerstetijd)
        total_seconds2=time_delta2.total_seconds()
        minuten=total_seconds2/60
        print('het duurde',total_seconds, 'en kwam',minuten,'minuten na dat het script begon')


#dit gedeelte hieronder is om grafieken te maken
#print(len(loginvalue))
#print(len(logintijd))
#print(logintijd)
strlengte = len(logintijd)
lengforgraph = 0.89 * float(strlengte)
lengforgraph= round(lengforgraph)
#print('dit is de lengte', lengforgraph)
if lengforgraph>655.36:
    lengforgraph=655.35


fig = plt.figure(figsize=(lengforgraph, 10), dpi=80)
# line 1 points
x1 = logintijd
y1 = loginvalue
# plotting the line 1 points
plt.plot(x1, y1, label='logintijd')

# naming the x axis
plt.xlabel('tijd')
# naming the y axis
plt.ylabel('tijd om in te loggen')
# giving a title to my graph
plt.title('dev.future.ngo inlogtijd')

# show a legend on the plot
plt.legend()

# function to show the plot

from matplotlib.pyplot import figure
plt.show()
#print('dit is de twee length for grep')
fig.set_size_inches(lengforgraph, 10)
datum=datum.replace(':','-')
fig.savefig("C:/Users/jackl/PycharmProjects/untitled/testmap/charts2/"+str(datum)+'logintijd' + 'chart.png', dpi=100)

#tweede keer voor de andere value

#print(loginvalue)
#print(plugval)
strlengte = len(plugtijd)
lengforgraph = 0.89 * float(strlengte)
lengforgraph= round(lengforgraph)
#print('dit is de lengte', lengforgraph)
if lengforgraph>655.36:
    lengforgraph=655.35


fig = plt.figure(figsize=(lengforgraph, 10), dpi=80)
# line 1 points
x1 = plugtijd
y1 = plugval
# plotting the line 1 points
plt.plot(x1, y1, label='plugintijd')

# naming the x axis
plt.xlabel('tijd')
# naming the y axis
plt.ylabel('tijd om in te loggen')
# giving a title to my graph
plt.title('dev.future.ngo plugintijd')

# show a legend on the plot
plt.legend()

# function to show the plot

from matplotlib.pyplot import figure
plt.show()
#print('dit is de twee length for grep')
fig.set_size_inches(lengforgraph, 10)
#print(datum)
datum=datum.replace(':','-')
fig.savefig("C:/Users/jackl/PycharmProjects/untitled/testmap/charts2/"+str(datum)+'plugintijd' + 'chart.png', dpi=100)

