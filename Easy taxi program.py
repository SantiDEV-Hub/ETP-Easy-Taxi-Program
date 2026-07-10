print(r"""
·····················
: _____ _____ ____  :
:| ____|_   _|  _ \ :
:|  _|   | | | |_) |:
:| |___  | | |  __/ :
:|_____| |_| |_|    :
·····················
""")


taxi = input("Welcome to the Easy Taxi Program! Please type how many passengers are coming with you (max 3): ")

if taxi in ["1", "2", "3"]:
    print(f"ok! a Sedan for {taxi}!")
    
  
    quality = input("What quality would you like in your taxi? Budget/Normal/Luxury? ").lower()
    
  
    if quality == "budget":
        print("Ok a Toyota Prius on your way!")
    elif quality == "normal":
        print("Ok a Volkswagen Passat on your way!")
    elif quality == "luxury":
        print("Ok a Mercedes-Benz S-Class on your way!")
    else:
        print("uhhh we will just put you whit normal.")

   
    where = input("Where you heading to? Mall/Work/Shuttle Station? ").lower()
    
    if where in ["mall", "work", "shuttle station"]:
        print("Ok your taxi should be there in 3 minutes thanks for using ETP!")
    else:
        print("Ok just tell the driver where you heading to")

else:
    print("Sorry we only have taxis up to 3 people")