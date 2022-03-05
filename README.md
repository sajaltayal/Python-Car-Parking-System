# Python-Car-Parking-System
CAR PARKING SYSTEM

This project demonstrates how to implement a Car Parking System using Python.

User needs to enter Information for the 1st time when it is starting the system and these are-
1.) Capacity for SUV cars
2.) Capacity for SEDAN cars
3.) Capacity for MINI cars or 2-Wheelers
4.) Amount for SUV
5.) Amount for SEDAN
6.) Amount for MINI or 2-Wheeler
7.) Entry Mode or Exit Mode

The Interface looks like:

<img width="407" alt="Screenshot 2022-03-05 at 5 54 50 PM" src="https://user-images.githubusercontent.com/73775153/156882842-e8fccb49-1523-4fde-bfa1-136fac219ff3.png">

Features:
  1.) Entry and Exit Mode support
  2.) Total Amount Collected to be shown in the Exit Mode when requested
  3.) Real Time Parking Capacity after every Entry or Exit
  4.) Support to shut down when required
  
ENTRY MODE:
  * When a car enters the parking, the operator need to feed in the type of car i.e. SUV,SEDAN,MINI or 2-Wheeler.
  * As the Entry is Successfull, considering that there is sufficient parking space available, the respective parking space capacity is reduced by 1.
  * Updated Remaining Capacity is shown

The Entry Mode Interface looks like:

<img width="221" alt="Screenshot 2022-03-05 at 5 52 36 PM" src="https://user-images.githubusercontent.com/73775153/156882768-6f3107f6-0132-4369-9c21-04196ea17317.png">




EXIT MODE:
  * When a car exits the parking, the operator need to feed in the type of car i.e. SUV,SEDAN,MINI or 2-Wheeler.
  * As the Exit is Successfull, considering that there is a car inside the parking i.e. gives a error message if there is no car in the parking but the operator is initiating the exit, the respective parking space capacity is increased by 1.
  * Updated Remaining Capacity is shown
  * Also, there is a feature in the EXIT MODE to see the total money collected since the starting of the software.

The Exit Mode Interface looks like:

<img width="221" alt="Screenshot 2022-03-05 at 5 53 12 PM" src="https://user-images.githubusercontent.com/73775153/156882794-7c048318-4dfe-4880-9abc-c4440665a11f.png">
