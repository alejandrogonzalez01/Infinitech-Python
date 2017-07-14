import gspread
from oauth2client.service_account import ServiceAccountCredentials

### Interactive client with Google API ###
scope = ['https://spreadsheets.google.com/feeds']
json_file = 'client_secret.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
client = gspread.authorize(creds)

### Sheet structure ###
print 'Connecting to Google SpreadSheets'
sheet = client.open('customerlist').sheet1

dateCat = 1
phoneCat = 2
restCat = 3
genderCat = 4
timeCat = 5
customerCat = 6
statusCat = 7

dateList = []
phoneList = []
restList = []
genderList = []
timeList = []
customerList = []
statusList = []

size = 0;

def analyze():
    # print 'Analyzing Spreadsheet'
    # Access global variables
    global dateCat
    global phoneCat
    global restCat
    global genderCat
    global timeCat
    global customerCat
    global statusCat
    
    global dateList
    global phoneList
    global restList
    global genderList
    global timeList
    global customerList
    global statusList
    
    global size

    # Get sheet size using phone_number category    
    size = 0
    l = sheet.col_values(phoneCat)
    while l[size] is not '':
        size += 1

    def filler(L, C):
        
        #Used for Pretty Printing
        categoryNames = ['Dates', 'Phone Numbers', 'Restaurant Names', 'Genders', 'Order Times',
                 'Customer Names', 'Status']
        rowCounter = 1
        print 'Analyzing  ' + categoryNames[C - 1]
        while rowCounter <= size:
            L.append(sheet.cell(rowCounter, C).value)
            rowCounter += 1
        
    filler(dateList, dateCat)
    filler(phoneList, phoneCat)
    filler(restList, restCat)
    filler(genderList, genderCat)
    filler(timeList, timeCat)
    filler(customerList, customerCat)
    filler(statusList, statusCat)

def list_restaurants():
        
    # Creates list so names don't repeat.
    global restList
    mem = [] 
    counter = 0
    while counter < size:
        name = restList[counter]
        if name not in mem and "Total" not in name:
            print name
            mem.append(name)
            counter += 1

        else:
            counter += 1
            
    # Sorts Alphabetically 
    mem.sort()

    # Displays names  
    counter = 1
    for item in mem:
        print str(counter) + ') ' + item
        counter += 1

    print ''

def list_by_status(S):
    # Only 4 status available. ORDERED, DEAD, CALLED, 'BLANK'
    # Prints daterest name, name, 
    global dateList
    global phoneList
    global restList
    global timeList
    global customerList
    global statusList
    global size
    indexes = []

    counter = 1
    for item in statusList:
        if item == S:
            print counter
            indexes.append(counter)
            counter += 1
            
        else:
            counter += 1


    for index in indexes:
        i = index
        date = dateList[i - 1]
        phone = phoneList[i - 1]
        rest = restList[i - 1]
        time = timeList[i - 1]

        print str(date) + '  ***  ' + str(time) + '  ***  ' + str(phone) + '  ***  ' + rest




    



    
if __name__ == '__main__':   
    
    analyze()
    # Menu for console use
    while True:
        
        print '1) Update Data (Download and Reparse)'
        print '2) List by Force Order status'
        print '3) List all Restaurants in Database'
        option = int(raw_input(':'))

        # Update Data
        if option == 1:
            analyze()
        # List by Status
        elif option == 2:
            print '1) Ordered (has used the app or webpage)'
            print '2) Dead (no orders from restaurant in a while)'
            print '3) Called (ordered through restaurant)'
            print '4) Pending (hasn\'t ordered through app or webpage)'
            print '5) Go Back'
            option2 = int(raw_input(':'))

            catOptions = ['ORDERED', 'DEAD', 'CALLED', 'PENDING']
            if option2 < 5:
                list_by_status(catOptions[option2 - 1])
            else:
                break

        elif option == 3:
            list_restaurants()
        else:
            print 'That is not a valid option'
            



