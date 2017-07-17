import gspread
import datetime as cal
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



    
    counter = 0
    while counter < len(data):
        if counter in unwantedIndexes:
            counter += 1
        elif counter not in unwantedIndexes and data[counter] not in mem:
            mem.append(data[counter])
            counter += 1

    for item in mem:
        if S in item:
            print item

def menu():
    firstMenu = True
    secondMenu = True

    while firstMenu is True:
        print ''
        print '1) List all Restaurants'
        print '2) List by Status'
        print '3) Add Call Data'

        choice= int(raw_input(":"))
        if choice == 1:
            list_restaurants()
        elif choice == 2:
            while secondMenu is True:
                print ''
                print '1) Ordered'
                print '2) Pending'
                print '3) Dead'
                print '4) Called'
                
                choice2 = int(raw_input(":"))
                lazy_me = [1,2,3,4]

                if choice2 not in lazy_me:
                    print 'Invalid option'
                elif choice2 in lazy_me:
                    choicesStatus = ['ORDERED', 'PENDING', 'DEAD', 'CALLED']
                    list_by_status(choicesStatus[choice2 - 1])
                else:
                    menu()

        elif choice == 3:
            add_call()
        else:
            print 'That option is invalid'


def add_call():
    ##### TEST #####
    date = '7/17/2017'

    
    print 'Input data'
    insert = raw_input(":")
    input_data = insert.split(',')
    input_data.insert(0, date)
    input_data.append('PENDING')
    sheet.insert_row(input_data, len(data) + 1)
    

    
if __name__ == '__main__':
    parseData()
    menu()

        

def list_by_status(S):
    ## Remove unwanted lines ##
    mem = []

    
    counter = 0
    while counter < len(data):
        if counter in unwantedIndexes:
            counter += 1
        elif counter not in unwantedIndexes and data[counter] not in mem:
            mem.append(data[counter])
            counter += 1

    for item in mem:
        if S in item:
            print item

def menu():
    firstMenu = True
    secondMenu = True

    while firstMenu is True:
        print ''
        print '1) List all Restaurants'
        print '2) List by Status'
        print '3) Add Call Data'

        choice= int(raw_input(":"))
        if choice == 1:
            list_restaurants()
        elif choice == 2:
            while secondMenu is True:
                print ''
                print '1) Ordered'
                print '2) Pending'
                print '3) Dead'
                print '4) Called'
                
                choice2 = int(raw_input(":"))
                lazy_me = [1,2,3,4]

                if choice2 not in lazy_me:
                    print 'Invalid option'
                elif choice2 in lazy_me:
                    choicesStatus = ['ORDERED', 'PENDING', 'DEAD', 'CALLED']
                    list_by_status(choicesStatus[choice2 - 1])
                else:
                    menu()

        elif choice == 3:
            add_call()
        else:
            print 'That option is invalid'


def add_call():
    ##### TEST #####
    date = '7/17/2017'

    
    print 'Input data'
    insert = raw_input(":")
    input_data = insert.split(',')
    input_data.insert(0, date)
    input_data.append('PENDING')
    sheet.insert_row(input_data, len(data) + 1)
    

    
if __name__ == '__main__':
    parseData()
    menu()
