#dit script is er om de log files te paken uit de twee webcurl scripts en ze dan veranderen in een grafiek.
import re
import statistics
import glob, os
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path


test=[]#dit heeft de tijd en alle values
test2=[]
test3=[]#dit zijn de values van alle lookups
firstvalue=[]
average=[]
tijdvanlookup=[]

def lookuptimedef(values):
    for getallen in values:
        try:
            lku=[]
            for m in re.finditer('Lookup Time', x[1]):
                #print('ll found', m.start(), m.end())
                lku.append(m.start())
            lkutime1=lku[0]
            lkutime2=lku[1]
            lkutime3=lku[2]
            #print(getallen)
            #print(getallen[93:101])
            #print(lkutime1)
            #lookuptime1 = float(getallen[82:90])
            lookuptime1 = float(getallen[lkutime1+14:lkutime1+22])
            #print('dit is de lookuptime',lookuptime1)
            lookuptime2 = float(getallen[lkutime2+14:lkutime2+22])
            lookuptime3 = float(getallen[lkutime3+14:lkutime3+22])
            #print(getallen[377:385])
            #lookuptime2 = float(getallen[310:318])
            #print(getallen[661:669])
            #lookuptime3 = float(getallen[538:546])
            test2 = [lookuptime1, lookuptime2, lookuptime3]
            test.append(getallen[3:11])
            test.append(test2)
            #test3.append(getallen[3:11])
            #firstvalue.append(lookuptime1)
            #average.append(statistics.mean(test2))
        except:
            print("error")
    return test

def totaltimedef(values):
    for getallen in values:
        try:
            lku = []
            for m in re.finditer('Total Time', x[1]):
                #print('ll found', m.start(), m.end())
                lku.append(m.start())
            tttime1 = lku[0]
            tttime2 = lku[1]
            tttime3 = lku[2]
            # print(getallen)
            # print(getallen[93:101])
            # print(lkutime1)
            # lookuptime1 = float(getallen[82:90])
            tttime1 = float(getallen[tttime1 + 14:tttime1 + 23])
            tttime2 = float(getallen[tttime2 + 14:tttime2 + 23])
            tttime3 = float(getallen[tttime3 + 14:tttime3 + 23])
            #print(tttime1)
            #print(getallen)
            #print(getallen[93:101])
            #totaltime1 = float(getallen[82:90])
            #print(getallen[377:385])
            #totaltime2 = float(getallen[310:318])
            #print(getallen[661:669])
            #totaltime3 = float(getallen[538:546])
            test2 = [tttime1, tttime2, tttime3]
            test.append(getallen[3:11])
            test.append(test2)
            #test3.append(getallen[3:11])
            #firstvalue.append(totaltime1)
            #average.append(statistics.mean(test2))
        except:
            print("error")
    return test


def lookupgraph(first, averg, tijdlo,yval1,yval2,ylabel,titel,typegraph,naamvanwebsite):
    # print(test3)
    # print(len(first))
    # print(len(averg))
    # print(len(tijdlo))
    # print(first)
    strlengte = len(tijdlo)
    lengforgraph = 0.89 * float(strlengte)
    lengforgraph= round(lengforgraph)
    print('dit is de lengte', lengforgraph)
    if lengforgraph>655.36:
        lengforgraph=655.35

    #dit is vooral voor het verkorten van de tijd value, als het elke 10 minuten is is er weinig punt om de seconden te laten zien
    lijst3=[]
    for y in tijdlo:
        x = datetime.strptime(y, '%H:%M:%S')
        #print(type(x))
        #print(x)
        lijst3.append(x)

    #print(lijst3)

    time_delta1 = (lijst3[-2] - lijst3[-3])
    #print(time_delta1)
    total_seconds = time_delta1.total_seconds()
    #print(total_seconds)
    minutes = total_seconds / 60

    #dit is om tijd te verkorten, als er om de 10 minuten een scan wordt gedaan is er geen punt
    if minutes > 10:
        #print('tijd verschil is te groot het wordt verkort')
        niewetijdlijst = []
        for i in tijdlo:
            niewetijdlijst.append(i[0:-3])
        #print(tijdlo)
        #print(niewetijdlijst)
        tijdlo=niewetijdlijst

    fig = plt.figure(figsize=(lengforgraph, 10), dpi=80)
    # line 1 points
    x1 = tijdlo
    y1 = first
    # plotting the line 1 points
    plt.plot(x1, y1, label=yval1)

    # line 2 points
    x2 = tijdlo
    y2 = averg
    # plotting the line 2 points
    plt.plot(x2, y2, label=yval2)

    # naming the x axis
    plt.xlabel('tijd')
    # naming the y axis
    plt.ylabel(ylabel)
    # giving a title to my graph
    plt.title(titel+naamvanwebsite)

    # show a legend on the plot
    plt.legend()

    # function to show the plot

    from matplotlib.pyplot import figure
    #plt.show()
    #print('dit is de twee length for grep')
    fig.set_size_inches(lengforgraph, 10)
    fig.savefig("C:/Users/jackl/PycharmProjects/untitled/testmap/charts/"+datum+typegraph + 'chart.png', dpi=100)



#dit is om alle bestanden te vinden in de folder
os.chdir("C:/Users/jackl/PycharmProjects/untitled/testmap/logfiles")

pathlist = Path('C:/Users/jackl/PycharmProjects/untitled/testmap/logfiles').glob('**/*.txt')
for path in pathlist:
     # because path is object not string
     path_in_str = str(path)
     file=path_in_str
     datum=path_in_str[57:71]
     f = open(file, "r")
     bestand = f.read()

     x = bestand.split(' Oct ')
     x.pop(0)
     imagelist = []
     pathlist2 = Path('C:/Users/jackl/PycharmProjects/untitled/testmap/charts').glob('**/*.png')
     for path2 in pathlist2:
         path_in_str = str(path2)
         #print(path_in_str)
         image=path_in_str[55:69]
         imagelist.append(image[0:14])

     if datum in imagelist:
        print('dit bestand is er al')
        continue
     print(path)
     test = []  # dit heeft de tijd en alle values
     test2 = []
     test3 = []  # dit zijn de values van alle lookups
     firstvalue = []
     average = []
     tijdvanlookup = []
     counter = 2

     forpos = x[1].find('for :')
     endposition = x[1].find('Lookup Time', forpos)
     print(forpos)
     print(endposition)
     print(x)
     websitename=x[1][forpos + 5:endposition - 2]
     print(websitename)
     lookuplist = lookuptimedef(x)

     for y in lookuplist:

        if counter % 2 == 0:
            tijdvanlookup.append(y)
        if counter % 2 == 1:
            firstvalue.append(y[0])
            average.append(statistics.mean(y))
            #print(y)

        counter += 1

     lookupgraph(firstvalue,average,tijdvanlookup,'first lookuptime','avg lookup time','lookuptime','lookuptime van','lookuptime',websitename)
     #deze volgende regels is voor total time
     test = []  # dit heeft de tijd en alle values
     test2 = []
     test3 = []  # dit zijn de values van alle lookups
     firstvalue = []
     average = []
     tijdvanlookup = []
     counter = 2
     totallist = totaltimedef(x)
     tijdvantotaltime=[]


     for y in totallist:

        if counter % 2 == 0:
            tijdvantotaltime.append(y)
        if counter % 2 == 1:
            firstvalue.append(y[0])
            average.append(statistics.mean(y))
            #print(y)

        counter += 1

    #print(firstvalue)
    ##print(average)
    #print(tijdvantotaltime)
    #print(len(firstvalue))
    #print(len(average))
    #print(len(tijdvantotaltime))


     lookupgraph(firstvalue, average, tijdvantotaltime, 'first totaltime', 'avg totaltime time', 'totaltime','totaltime van ', 'totaltime',websitename)

#f = open("C:/Users/jackl/PycharmProjects/untitled/testmap/logfiles/2020-10-12logfile.txt", "r")
#print(f.read())
#bestand=f.read()
#datum=bestand[:10]
#x=bestand.split(' Oct ')
#print(x)
#print(x[1])



#lookuptime1=float(x[1][82:90])
#lookuptime2=float(x[1][310:318])
#lookuptime3=float(x[1][538:546])
#test=[]#dit heeft de tijd en alle values
#test2=[]
#test3=[]#dit zijn de values van alle lookups
#firstvalue=[]
#average=[]
#tijdvanlookup=[]

#deze loop is voor berekenen van de first lookup time



#test3.append(getallen[3:11])
#firstvalue.append(lookuptime1)
#average.append(statistics.mean(test2))
# print(test)
#print(lookuplist)

