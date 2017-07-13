import gspread
from oauth2client.service_account import ServiceAccountCredentials

### Interactive client with Google API ###
scope = ['https://spreadsheets.google.com/feeds']
json_file = 'client_secret.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
client = gspread.authorize(creds)

### Sheet structure ###
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
        counter = 1
        while counter  <= size:
            L.append(sheet.cell(counter, C).value)
            counter += 1
        
    filler(dateList, dateCat)
    filler(phoneList, phoneCat)
    filler(restList, restCat)
    filler(genderList, genderCat)
    filler(timeList, timeCat)
    filler(customerList, customerCat)
    filler(statusList, statusCat)




   
if __name__ == '__main__':   
    analyze()

    counter = 1
    for item in dateList:
        print str(counter) + ") " + item
        counter += 1






