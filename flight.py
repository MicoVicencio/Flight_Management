import sys

class Flight():
    def __init__(self,
                 name = None,
                 email = None,
                 age = None,
                 f_id = None,
                 air_seats = None,
                 d_areas = None,
                 total_price = 0,
                 taytay_des = None,
                 binangonan_des = None,
                 angono_des = None,
                 person_count = 1,
                 taytay_books = [],
                 binangonan_books = [],
                 angono_books = [],
                 chosen = None,
                 seat = None,
                 clas= None,
                 date=None,
                 time = None
                 ):
        # Initialize the Flight class with various attributes
        self.time = time  # Time of the flight
        self.date = date  # Date of the flight
        self.clas = clas  # Class of the flight (VIP or Regular)
        self.seat = seat  # Seat number
        self.chosen = chosen  # Chosen flight details
        self.taytay_books = taytay_books  # Bookings for Taytay
        self.binangonan_books = binangonan_books  # Bookings for Binangonan
        self.angono_books = angono_books  # Bookings for Angono
        self.person_count = person_count  # Count of persons
        self.name = name  # Passenger's name
        self.email = email  # Passenger's email
        self.age = age  # Passenger's age
        self.f_id = f_id  # Flight ID
        self.air_seats = air_seats  # Available seats
        self.d_areas = d_areas  # Departure areas
        self.total_price = total_price  # Total price of the booking
        self.taytay_des = taytay_des  # Taytay flight destinations
        self.binangonan_des = binangonan_des  # Binangonan flight destinations
        self.angono_des = angono_des  # Angono flight destinations
        self.d_areas = ["Taytay", "Angono", "Binangonan"]  # List of departure areas
        # Flight destinations and details for Taytay, Binangonan, and Angono
        self.taytay_des = [
            {
                "Destination":"Boracay",
                "Flight Hour":"5hrs",
                "Ticket Price": 400,
                "Available Seats":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            },
            {
                "Destination":"Davao",
                "Flight Hour":"5hrs",
                "Ticket Price": 400,
                "Available Seats":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            },
            {
                "Destination":"Siargao",
                "Flight Hour":"5hrs",
                "Ticket Price": 400,
                "Available Seats":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            }
        ]
        self.binangonan_des = [
            {
                "Destination":"Bohol",
                "Flight Hour":"5hrs",
                "Ticket Price": 500,
                "Available Seats":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            },
            {
                "Destination":"Cebu",
                "Flight Hour":"5hrs",
                "Ticket Price": 500,
                "Available Seats":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            },
            {
                "Destination":"Dumagete",
                "Flight Hour":"5hrs",
                "Ticket Price": 500,
                "Available Seats":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            }
        ]
        self.angono_des = [
            {
                "Destination":"Camiguin",
                "Flight Hour":"5hrs",
                "Ticket Price": 600,
                "Available Seats":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            },
            {
                "Destination":"Zamboanga",
                "Flight Hour":"5hrs",
                "Ticket Price": 600,
                "Available Seats":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            },
            {
                "Destination":"Cagayan",
                "Flight Hour":"5hrs",
                "Ticket Price": 600,
                "Available Seats":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            }
        ]
    def menu(self):
        # Display the main menu and handle user choices
        print()
        print("Welcome to Rizal Airlines")
        print("Functionalities:")
        print("1.View Availabe Fligts")
        print("2.Book a Flight")
        print("3.View Booked Flights")
        print("4.Exit the program")
        choose = input("Enter your choice:1-4:")
        if choose == '1':
            self.view_flights()
        elif choose == '2':
            self.book()
        elif choose == '3':
            self.view_books()
        elif choose == '4':
            sys.exit()
        else:
            print("Invalid Choice! Try again.")
            self.menu()
            
    def book(self):
         # Book a flight for the user
        self.total_price = 0
        self.person_count += 1
        print("Booking Function")
        self.name = input("Enter Name:")
        self.age = input("Enter Age:")
        self.email = input("Enter Email:")
        self.date = input("Enter Date of Flight:(dd/mm/yy)")
        print("Available Time: 9am,1pm & 5pm")
        self.time = input("Enter your time prefer(9,1,5):")
        self.f_id = "QWE12"+str(self.person_count)
        print("Available Departure Areas:")
        n = 1
        for _ in self.d_areas:
            print(f"{n}.{_}")
            n += 1
        choice = input("Choose where do you want to go:(1-3):")
        if choice == '1':
            self.total_price += 400
            self.taytay()
            des = int(input("Choose your destination:(1-3):"))
            if des >= 1 and des <=3:
                self.chosen = self.taytay_des[des - 1]
                self.print_destination()
                while True:
                  self.seat = int(input("Which seat do you want to seat?(1-20):"))
                  if self.seat in self.chosen["Available Seats"]:
                      self.chosen["Available Seats"].remove(self.seat)
                      break
                  else:
                      print("The seat was already Booked. Try Again!")
                ask = input("Do you want to avail VIP experience?(y-n):")
                if ask == 'y':
                    self.chosen["Class"] = "VIP"
                    self.total_price += 300
                else:
                    self.chosen["Class"] = "Regular"
                self.chosen["f_id"] = self.f_id
                self.chosen["Date"] = self.date
                if self.time == '9':
                    self.chosen["Time"] = "9am-2pm"
                elif self.time == "1":
                    self.chosen["Time"] = "1pm-6pm"
                elif self.time == "5":
                    self.chosen["Time"] = "5pm-10pm"
                self.chosen["Total Price"] = self.total_price
                print(self.chosen)
                self.book_adder("Taytay")
        elif choice == '2':
            self.angono()
            self.total_price += 400
            des = int(input("Choose your destination:(1-3):"))
            if des >= 1 and des <=3:
                self.chosen = self.angono_des[des - 1]
                self.print_destination()
                while True:
                  self.seat = int(input("Which seat do you want to seat?(1-20):"))
                  if self.seat in self.chosen["Available Seats"]:
                      self.chosen["Available Seats"].remove(self.seat)
                      break
                  else:
                      print("The seat was already Booked. Try Again!")
                ask = input("Do you want to avail VIP experience?(y-n):")
                if ask == 'y':
                    self.chosen["Class"] = "VIP"
                    self.total_price += 300
                else:
                    self.chosen["Class"] = "Regular"
                self.chosen["f_id"] = self.f_id
                self.chosen["Date"] = self.date
                if self.time == '9':
                    self.chosen["Time"] = "9am-2pm"
                elif self.time == "1":
                    self.chosen["Time"] = "1pm-6pm"
                elif self.time == "5":
                    self.chosen["Time"] = "5pm-10pm"
                self.chosen["Total Price"] = self.total_price
                self.book_adder("Angono")
        elif choice == '3':
            self.binangonan()
            self.total_price += 400
            des = int(input("Choose your destination:(1-3):"))
            if des >= 1 and des <=3:
                self.chosen = self.binangonan_des[des - 1]
                self.print_destination()
                while True:
                  self.seat = int(input("Which seat do you want to seat?(1-20):"))
                  if self.seat in self.chosen["Available Seats"]:
                      self.chosen["Available Seats"].remove(self.seat)
                      break
                  else:
                      print("The seat was already Booked. Try Again!")
                ask = input("Do you want to avail VIP experience?(y-n):")
                if ask == 'y':
                    self.chosen["Class"] = "VIP"
                    self.total_price += 300
                else:
                    self.chosen["Class"] = "Regular"
                self.chosen["f_id"] = self.f_id
                self.chosen["Date"] = self.date
                if self.time == '9':
                    self.chosen["Time"] = "9am-2pm"
                elif self.time == "1":
                    self.chosen["Time"] = "1pm-6pm"
                elif self.time == "5":
                    self.chosen["Time"] = "5pm-10pm"
                self.chosen["Total Price"] = self.total_price
                
                self.book_adder("Binangonan")
                
        self.menu()
            
    
    def print_destination(self):
        # Print details of the chosen destination
        print()
        print(f"Destination:{self.chosen['Destination']}")
        print(f"Flight Hour:{self.chosen['Flight Hour']}")
        print(f"Ticket Price:{self.chosen['Ticket Price']}")
        print(f"Available Seats:{self.chosen['Available Seats']}")       
            
    def book_adder(self,departure):
         # Add booking details to the respective destination
        if departure == "Taytay":
            items = {
                "Name":self.name,
                "Age":self.age,
                "Email":self.email,
                "F_ID":self.chosen["f_id"],
                "Date":self.chosen["Date"],
                "Flight Duration":self.chosen["Time"],
                "Destination":self.chosen["Destination"],
                "Flight Hour":self.chosen["Flight Hour"],
                "Ticket Price":self.chosen["Ticket Price"],
                "Seat Number":self.seat,
                "Class":self.chosen["Class"],
                "Total Price":self.chosen["Total Price"]   
            } 
            self.taytay_books.append(items)
            
        if departure == "Angono":
            items = {
                "Name":self.name,
                "Age":self.age,
                "Email":self.email,
                "F_ID":self.chosen["f_id"],
                "Date":self.chosen["Date"],
                "Flight Duration":self.chosen["Time"],
                "Destination":self.chosen["Destination"],
                "Flight Hour":self.chosen["Flight Hour"],
                "Ticket Price":self.chosen["Ticket Price"],
                "Seat Number":self.seat,
                "Class":self.chosen["Class"],
                "Total Price":self.chosen["Total Price"]   
            } 
            self.angono_books.append(items)
            
        if departure == "Binangonan":
            items = {
                "Name":self.name,
                "Age":self.age,
                "Email":self.email,
                "F_ID":self.chosen["f_id"],
                "Date":self.chosen["Date"],
                "Flight Duration":self.chosen["Time"],
                "Destination":self.chosen["Destination"],
                "Flight Hour":self.chosen["Flight Hour"],
                "Ticket Price":self.chosen["Ticket Price"],
                "Seat Number":self.seat,
                "Class":self.chosen["Class"],
                "Total Price":self.chosen["Total Price"]   
            } 
            self.binangonan_books.append(items)       
            
            
    def view_flights(self):
        # Display available flights based on user's choice of departure area
        print("Available Departure Areas:")
        n = 1
        for _ in self.d_areas:
            print(f"{n}.{_}")
            n += 1
        choice = input("Which Departure Area do you want to see the available flights?")
        if choice == '1':
            self.taytay()
        elif choice == '2':
            self.angono()
        elif choice == '3':
            self.binangonan()
        self.menu()   
             
    def view_books(self):
        # View booked flights based on user's choice of departure area
        print("Categories:")
        n = 1
        for _ in self.d_areas:
            print(f"{n}.{_}")
            n += 1
        ask = input("Enter choice:(1-3):")   
        if ask == '1':
            n = 1
            for items in self.taytay_books:
                print()
                print(f"#{n}")
                print(f"Name:{items['Name']}")
                print(f"Age:{items['Age']}")
                print(f"Email:{items['Email']}")
                print(f"F_ID:{items['F_ID']}")
                print(f"Date:{items['Date']}")
                print(f"Flight Duration:{items['Flight Duration']}")
                print(f"Destination:{items['Destination']}")
                print(f"Flight Hour:{items['Flight Hour']}")
                print(f"Ticket Price:{items['Ticket Price']}")
                print(f"Seat Number:{items['Seat Number']}")
                print(f"Class:{items['Class']}")
                print(f"Total Price:{items['Total Price']}")
                print()
                n+=1
        elif ask == '2':
             n = 1
             for items in self.angono_books:
                print()
                print(f"#{n}")
                print(f"Name:{items['Name']}")
                print(f"Age:{items['Age']}")
                print(f"Email:{items['Email']}")
                print(f"F_ID:{items['F_ID']}")
                print(f"Date:{items['Date']}")
                print(f"Flight Duration:{items['Flight Duration']}")
                print(f"Destination:{items['Destination']}")
                print(f"Flight Hour:{items['Flight Hour']}")
                print(f"Ticket Price:{items['Ticket Price']}")
                print(f"Seat Number:{items['Seat Number']}")
                print(f"Class:{items['Class']}")
                print(f"Total Price:{items['Total Price']}")
                n+= 1
                print()
        elif ask == '3':
             n = 1
             for items in self.binangonan_books:
                print()
                print(f"#{n}")
                print(f"Name:{items['Name']}")
                print(f"Age:{items['Age']}")
                print(f"Email:{items['Email']}")
                print(f"F_ID:{items['F_ID']}")
                print(f"Date:{items['Date']}")
                print(f"Flight Duration:{items['Flight Duration']}")
                print(f"Destination:{items['Destination']}")
                print(f"Flight Hour:{items['Flight Hour']}")
                print(f"Ticket Price:{items['Ticket Price']}")
                print(f"Seat Number:{items['Seat Number']}")
                print(f"Class:{items['Class']}")
                print(f"Total Price:{items['Total Price']}")
                print()
                n+=1
        self.menu()
        
        
        
    def taytay(self):
        # Display available flights for Taytay
        print("Taytay Available Flights:")
        for item in self.taytay_des:
            print()
            print(f"Destination:{item['Destination']}")
            print(f"Flight Hour:{item['Flight Hour']}")
            print(f"Ticket Price:{item['Ticket Price']}")
            print(f"Available Seats:{item['Available Seats']}")
            
    def angono(self):
         # Display available flights for Angono
        print("Angono Available Flights:")
        for item in self.angono_des:
            print()
            print(f"Destination:{item['Destination']}")
            print(f"Flight Hour:{item['Flight Hour']}")
            print(f"Ticket Price:{item['Ticket Price']}")
            print(f"Available Seats:{item['Available Seats']}")

    def binangonan(self):
        # Display available flights for Binangonan
        print("Binangonan Available Flights:")
        for item in self.binangonan_des:
            print()
            print(f"Destination:{item['Destination']}")
            print(f"Flight Hour:{item['Flight Hour']}")
            print(f"Ticket Price:{item['Ticket Price']}")
            print(f"Available Seats:{item['Available Seats']}")
            
            
flight = Flight()
flight.menu()