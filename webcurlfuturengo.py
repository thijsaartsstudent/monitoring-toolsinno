#stuurt een nslookup naar de future website, werkt alleen op linux
import os
import time
hostname = "future.ngo" #example
counter=0
import datetime

while True:
    # ik voer het nslookup commando 3 keer uit om zeker te weten dat hij goed wordt verbonden en of dat er een verschil is tussen de 3 keren.
    stream = os.popen("curl -s -w 'Testing Website Response Time for :%{url_effective}\n\nLookup Time:\t\t%{time_namelookup}\nConnect Time:\t\t%{time_connect}\nAppCon Time:\t\t%{time_appconnect}\nRedirect Time:\t\t%{time_redirect}\nPre-transfer Time:\t%{time_pretransfer}\nStart-transfer Time:\t%{time_starttransfer}\n\nTotal Time:\t\t%{time_total}\n' -o /dev/null future.ngo")
    output = stream.read()
    stream = os.popen(
        "curl -s -w 'Testing Website Response Time for :%{url_effective}\n\nLookup Time:\t\t%{time_namelookup}\nConnect Time:\t\t%{time_connect}\nAppCon Time:\t\t%{time_appconnect}\nRedirect Time:\t\t%{time_redirect}\nPre-transfer Time:\t%{time_pretransfer}\nStart-transfer Time:\t%{time_starttransfer}\n\nTotal Time:\t\t%{time_total}\n' -o /dev/null future.ngo")
    output2 = stream.read()
    stream = os.popen(
        "curl -s -w 'Testing Website Response Time for :%{url_effective}\n\nLookup Time:\t\t%{time_namelookup}\nConnect Time:\t\t%{time_connect}\nAppCon Time:\t\t%{time_appconnect}\nRedirect Time:\t\t%{time_redirect}\nPre-transfer Time:\t%{time_pretransfer}\nStart-transfer Time:\t%{time_starttransfer}\n\nTotal Time:\t\t%{time_total}\n' -o /dev/null future.ngo")
    output3 = stream.read()
    print(hostname)
    tijd=time.ctime()
    now = datetime.datetime.now()
    # dit voegt een datum toe aan het bestand zodat het meer overzichterlijker is.
    print(now.strftime("%Y-%m-%d"))
    namestring = now.strftime("%Y-%m-%d")+'-ngo-' + 'logfile.txt'
    f = open(namestring, "a")
    print(tijd)
    print(output)
    f.write(tijd+'\n'+ output+"\n"+output2+"\n"+output3+'\n')
    # ik heb hier een sleep aangemaatk van 10 seconden anders kun je geblokeerd worden door de website
    time.sleep(10)
