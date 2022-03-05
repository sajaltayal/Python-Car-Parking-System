class ParkingSystem:
    def __init__(self, suv, sedan, mini,rs,suv_money,sedan_money,mini_money,total_amount):
        self.sp = [0,suv,sedan,mini]    #we have started the array with zero because the car type we are taking starts with 1
        self.rs=rs  #copy of array 
        self.suv_money=suv_money   #Charges for SUV
        self.sedan_money=sedan_money  #Charges for SEDAN
        self.mini_money=mini_money  #Charges for MINI / 2-WHEELER
        self.total_amount=total_amount  #total amount collected for today
        self.i=0  #threshold value to stop the system from taking further entries after the parking is full

    def addCar(self, carType):
        if(self.sp[carType] >0 ):
            self.sp[carType] -= 1  #decrease specific car space as car enter
            self.i=1
            print()
            print("ENTRY SUCCESSFULL")
            print()
            print("Capacity for SUV:",self.sp[1])
            print("Capacity for SEDAN:",self.sp[2])
            print("Capacity for MINI or 2-WHEELERS:",self.sp[3])
        else:
            self.i=0
            print("No parking Space left for such type of Car")     #shortage of space

    def removeCar(self, carType):
        if(self.sp[carType]>=0 and self.sp[carType]<self.rs[carType]):
            self.sp[carType] += 1  # increase specific car space as car exits
            self.i=1
            print()
            print("EXIT SUCCESSFULL")
            print()
            print("Capacity for SUV:",self.sp[1])
            print("Capacity for SEDAN:",self.sp[2])
            print("Capacity for MINI or 2-WHEELERS:",self.sp[3])

            if(carType==1):
                print("\nNet Amount =",suv_money)
                self.total_amount+=suv_money       #calculate amount for SUV
            elif(carType==2):
                print("\nNet Amount =",sedan_money)
                self.total_amount+=sedan_money       #calculate amount for SEDAN
            elif(carType==3):
                print("\nNet Anount =",mini_money)
                self.total_amount+=mini_money       #calculate amount for MINI / 2-Wheeler
            else:
                print("\nNet Amount = 0")
                self.total_amount+=0
        else:
            self.i=0
            print("Capacity Full")      #No cars left in the parking
            print()
            print("Capacity for SUV:",self.sp[1])
            print("Capacity for SEDAN:",self.sp[2])
            print("Capacity for MINI or 2-WHEELERS:",self.sp[3])
            print("\nNet Amount = 0")
            
        

b=int(input("Capacity for SUV cars like Innova:").strip())      #Capacity for SUV 
m=int(input("Capacity for SEDAN cars like Honda City:").strip())    #Capacity for SEDAN
s=int(input("Capacity for 2 WHEELER or MINI CARS like Alto, Nano:").strip())    #Capacity for MINI / 2 wheeler 
suv_money=int(input("Amount for SUV:").strip())    #Charges for SUV
sedan_money=int(input("Amount for SEDAN:").strip())  #Charges for SEDAN
mini_money=int(input("Amount for MINI or 2-WHEELER:").strip())  #Charges for MINI
print()

print("Starting the parking system")
total=b+m+s #total parking space available
ps=ParkingSystem(b,m,s,[0,b,m,s],bm,mm,sm,0)
ee=str(input("Entry/Exit:").upper())
car_number
i=1
while i<total:
    if(ee=="ENTRY"):
        print("\nENTRY MODE ON")
        t=int(input("\n1.) SUV\n2.) SEDAN\n3.) MINI or 2-WHEELERS\n4.) Switch Mode (Entry/Exit)\n5.) Exit ---> 5\n\nEnter the Car Type / Mode:").strip())
        if(t==1 or t==2 or t==3):
            ps.addCar(t)
            print("---------------------------------------------------------")
            if(ps.i==0):
                i=i
            else:
                i+=1
        elif(t==5):
            print("\n\n Ending........")
            break
        else:
            ee="EXIT"
            print("---------------------------------------------------------")
        
    else:
        print("\nEXIT MODE ON")
        t=int(input("\n1.) SUV\n2.) SEDAN\n3.) MINI or 2-WHEELERS\n4.) Switch Mode (Entry/Exit)\n5.) Total Amount\n6.) Exit\n\nEnter the Car Type / Mode:").strip())
        if(t == 1 or t== 2 or t == 3):
            ps.removeCar(t)
            print("---------------------------------------------------------")
            if(ps.i==0):
                i=i
            else:
                i-=1
        elif(t==5):
            print("---------------------------------------------------------")
            print("Total Amount Collected:",ps.total_amount)
            print("---------------------------------------------------------")
        elif(t==6):
            print("\n\n Ending........")
            break
        else:
            ee="ENTRY"
            print("---------------------------------------------------------")
        

        
