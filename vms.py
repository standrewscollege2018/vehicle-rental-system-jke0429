###################################
###################################
###########    VMS     ############
###################################
###################################
# Program that runs a vehicle management system.

# Set vehicle as a class
class Vehicle:
    def __init__(self,make,model,licence,seats,price):
        self._make = make
        self._model = model
        self._licence = licence 
        self._seats = seats
        self._available = True
        self._renter = ""
        self._rentdate = ""
        self._price = price
        carlist.append(self)

    def _displaycars(self):
        print("======================")
        print("Make: {}".format(self._make))
        print("Model: {}".format(self._model))
        print("Licence: {}".format(self._licence))
        print("Seats: {}".format(self._seats))
        print("Price: ${} per day".format(self._price))
        if self._available == True:
            print("Available for Rental")
        else:
            print("Currently Unavailable, Rented by: {}".format(self._renter))
            print("Available by: {}".format(self._rentdate))
    

# Set up a list to store cars
carlist = []
# Create Default Cars
Vehicle("Porsche", "911 Carrera","JQE024", 4, 690)
Vehicle("Tesla", "Roadster", "B00M", 2, 500)
Vehicle("Tesla", "Model S", "S3XY", 7, 200)
Vehicle("Tesla", "Model 3", "JAI048", 5, 200)
Vehicle("Tesla", "Model X", "T3SL4", 5, 200)
Vehicle("Tesla", "Model Y", "SH00K", 7, 250)

# Set up a search function for cars by model
def model_search():
    while True:
        carmodel = input("Enter a Model of Car: ")
        model_count = 0
        for n in carlist:
            if carmodel in n._model and n._available == True:
                model_count += 1
                n._displaycars()
        print("{} Cars Matching model '{}'".format(model_count, carmodel))
        break

# Set up a search function for cars by license
def licence_search():
    while True:
        carlicence = input("Enter a licence of Car: ")
        licence_count = 0
        for n in carlist:
            if carlicence in n._licence and n._available == True:
                licence_count += 1
                n._displaycars()
        print("{} Cars Matching Licence'{}'".format(licence_count, carlicence))
        break

# Set up a search function for cars by license
def seats_search():
    while True:
        carseats= input("Enter a seat amount: ")
        seats_count = 0
        for n in carlist:
            if carseats in n._seats and n._available == True:
                seats_count += 1
                n._displaycars()
        print("{} Cars Matching seat amount '{}'".format(seats_count, carseats))
        break

# Set up a search function for cars by maximum price
def price_search():
    while True:
        carprice=int(input("Enter Maximum Price: "))
        price_count = 0
        for n in carlist:
            if carprice > n._price and n._available == True:
                price_count += 1
                n._displaycars()
        print("{} Cars under price: '${}'".format(price_count, carprice))
        break

# Set up a search function for cars by maximum price
def make_search():
    while True:
        carmake = input("Enter Car Make: ")
        make_count = 0
        for n in carlist:
            if carmake in n._make and n._available == True:
                make_count += 1
                n._displaycars()
        print("{} Cars with Make '{}'".format(make_count, carmake))
        break
def interact():
    while True:
        print("Welcome To the Vehicle Rental Company!")
        choice = int(input("To search vehicles by Make, Press 1. Model, Press 2. Licence, Press 3. Price, Press 4. Seats, Press 5. To Hire your chosen Car, Press 6. To Return your car, Press 7. To Exit, Press 8"))
        if choice == 1:
            make_search()
        if choice == 2:
            model_search()
        if choice == 3:
            licence_search()
        if choice == 4:
            price_search()
        if choice == 5:
            seats_search()
        if choice == 6:
            selection = input("Please type the License Plate no. of the car you would like to book:")
            for n in carlist:
                if selection in n._licence and n._available == True:
                    n._renter = input("Please Input your Name:")
                    print("Please input the dates you intend to hire the car until:")
                    day = input("Day (number):")
                    month = input("Month (number) :")
                    n._rentdate = (day + "/" + month + "/18")
                    n._available = False
                    print("Car Hired until {}".format(n._rentdate))
                    n._displaycars()
        if choice == 7:
            returncar = input("Please type the License Plate no. of the car you would like to return:")
            for n in carlist:
                if returncar in n._licence and n._available == False:
                    print('Thank you for doing business with us!')
                    n._available = True
                    n._displaycars()
        if choice == 8:
            break

interact()