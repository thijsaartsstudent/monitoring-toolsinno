#dit bestand voert een script uit dat kijk naar de speed score van een website en maakt er een csv bestand van
#omdat het gebruikt maakt van nslookup via linux shell werkt het alleen op linux
import requests
import datetime
import time
import os
import time

counter=0
import datetime
#veel van dit script komt van deze tutorail https://medium.com/@benjburkholder/python-automating-google-pagespeed-insights-api-for-seo-a0d1ba2f3a8b ik heb zelf wat aanpassingen gemaakt
# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started

# JSON paths: https://developers.google.com/speed/docs/insights/v4/reference/pagespeedapi/runpagespeed

# Populate 'pagespeed.txt' file with URLs to query against API.
while True:
    with open('pagespeed.txt') as pagespeedurls: # het pagespeed bestand zet je alle websites in die je wilt testen
        now = datetime.datetime.now()
        download_dir = 'pagespeed-results.csv'
        file = open(now.strftime("%Y-%m-%d")+download_dir, 'a')
        content = pagespeedurls.readlines()
        content = [line.rstrip('\n') for line in content]
        #columnTitleRow = "URL, First Contentful Paint, First Interactive, Time,lookuptime,totaltime\n"
        #file.write(columnTitleRow)

        # This is the google pagespeed api url structure, using for loop to insert each url in .txt file
        for line in content:
            # If no "strategy" parameter is included, the query by default returns desktop data.
            x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}&strategy=mobile'
            print(f'Requesting {x}...')
            r = requests.get(x)
            final = r.json()

            try:
                urlid = final['id']
                split = urlid.split('?') # This splits the absolute url from the api key parameter
                urlid = split[0] # This reassigns urlid to the absolute url
                ID = f'URL ~ {urlid}'
                ID2 = str(urlid)
                urlfcp = final['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
                FCP = f'First Contentful Paint ~ {str(urlfcp)}'
                FCP2 = str(urlfcp)
                urlfi = final['lighthouseResult']['audits']['interactive']['displayValue']
                FI = f'First Interactive ~ {str(urlfi)}'
                FI2 = str(urlfi)
                hostname = "dev.future.ngo"
                crlcommand="curl -s -w 'Testing Website Response Time for :%{url_effective}\n\nLookup Time:\t\t%{time_namelookup}\nConnect Time:\t\t%{time_connect}\nAppCon Time:\t\t%{time_appconnect}\nRedirect Time:\t\t%{time_redirect}\nPre-transfer Time:\t%{time_pretransfer}\nStart-transfer Time:\t%{time_starttransfer}\n\nTotal Time:\t\t%{time_total}\n' -o /dev/null " +hostname
                print(crlcommand)
                stream = os.popen(crlcommand)
                output = stream.read()
                output2= output.split(':')
                #print(output)
                #print(output2[2][2:10])
                #print(output2[-1][2:10])
                #ik heb lookuptime bij dit script gestopt want het leek me nuttige informatie
                lookuptime=output2[2][2:10]
                # totaltime heeft te maken met nslookup
                totaltime=output2[-1][2:10]

            except KeyError:
                print(f'<KeyError> One or more keys not found {line}.')

            try:
                tijd = time.ctime()
                row = f'{ID2},{FCP2},{FI2},{tijd},{lookuptime},{totaltime}\n'
                file.write(row)
            except NameError:
                print(f'<NameError> Failing because of KeyError {line}.')
                file.write(f'<KeyError> & <NameError> Failing because of nonexistant Key ~ {line}.' + '\n')

            try:
                print(ID)
                print(FCP)
                print(FI)
            except NameError:
                print(f'<NameError> Failing because of KeyError {line}.')

        file.close()
        #ik heb hier een sleep aangemaatk van 10 seconden anders kun je geblokeerd worden door de website
        time.sleep(10)
