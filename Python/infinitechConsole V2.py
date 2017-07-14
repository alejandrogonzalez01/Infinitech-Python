import gspread
from oauth2client.service_account import ServiceAccountCredentials

### Interactive client with Google API ###
scope = ['https://spreadsheets.google.com/feeds']
json_file = 'client_secret.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
client = gspread.authorize(creds)

### Connect and Download data from Google SpreadSheet ###
print 'Connecting to Google SpreadSheets'
sheet = client.open('customerlist').sheet1
data = sheet.get_all_values()

### Sheet Fields ###


dateList = []
custNumberList = []
restNameList = []
custGenderList = []
timeList = []
custNameList = []
statusList = []

dateCategory = 0
custNumberCategory = 1
restNameCategory = 2
custGenderCategory = 3
timeCategory = 4
custNameCategory = 5
statusCategory = 6

unwantedIndexes = []



def parseData():
    
    print 'Parsing Data'
    
    def filler(L, C):
        for row in data:
            L.append(row[C])

    ## Filling all lists with corresponding data ##
    filler(dateList, dateCategory)
    filler(custNumberList, custNumberCategory)
    filler(restNameList, restNameCategory)
    filler(custGenderList, custGenderCategory)
    filler(timeList, timeCategory)
    filler(custNameList, custNameCategory)
    filler(statusList, statusCategory)

    ## Get unwanted line indexes
    counter = 0
    for item in restNameList:
        if 'Total' in item:
            unwantedIndexes.append(counter)
            counter += 1
        else:
            counter += 1
    print 'Finished Parsing'

def list_restaurants():

    ## Creates list without repeating names and sorts ##
    mem = []
    for item in restNameList:
        if item not in mem and 'Total' not in item:
            mem.append(item)
    mem.sort()

    ## Prints all names ##
    for item in mem:
        print item



############TEST###########
mem = []        
        

def list_by_status(S):
    ## Remove unwanted lines ##
    global mem
    counter = 0
    while counter < len(data):
        if counter in unwantedIndexes:
            counter += 1
        else:
            mem.append(data[counter])
            counter += 1

    for item in mem:
        if S in item:
            print item


    

    
if __name__ == '__main__':
    parseData()
    list_by_status('ORDERED')
    
