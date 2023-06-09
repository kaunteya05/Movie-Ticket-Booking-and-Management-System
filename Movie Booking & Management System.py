import mysql.connector
import random
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import from_db_cursor

mydb = mysql.connector.connect(host="localhost",user="root",password="root",port=3306,database="Customer")


def Database():
      mydb = mysql.connector.connect(host="localhost",user="root",password="root",port=3306,database="Customer")
      with mydb:
           mycursor=mydb.cursor(buffered=True)
           retrieve = "SELECT * FROM Details"
           mycursor.execute(retrieve)
           Table_Output = from_db_cursor(mycursor)
      print(Table_Output)
      Surety()


#Customer Function
def Customer():
    print("Select what you wish to do!\n"
          "1. Book Ticket\n"
          "2. View Your Order\n"
          "3. Exit")
    print(" ")
    z=int(input("Enter you choice: "))
    if z==1 :
        print(" ")
        WORK()
        print(" ")
    elif z==2 :
        print(" ")
        OrderSum()
    elif z==3:
        Main_Exit()
    else:
        print("Enter Correct Choice!")
        print(" ")
        Customer()


#Admin Function
def Admin():
        p=input("Enter Password: ")
        if p=="nox":
            print("Welcome!")
            print(" ")
            print("Choose one of the following: \n"
                  "1.View Database\n"
                  "2.View Sales\n"
                  "3.Analytics\n")
            L=int(input("Choose one: "))
            if L==1:
                Database()
            elif L==2:
                Sales_Menu()
            elif L==3:
                Graphs_Menu()
        else:
            print("Enter Correct Password!")
            Admin()


def Sales_Menu():
    print("How do you wish to see the Sales?")
    print("1.Moive Wise\n"
          "2.City Wise\n")
    CHOZ=int(input("Choose One: "))
    if CHOZ ==1:
        mydb = mysql.connector.connect(host="localhost",user="root",password="root",port=3306,database="Customer")
        mycursor = mydb.cursor(buffered=True)
        sql = "Select MOVIE, SUM(No_Of_Seats) AS 'Sales' from DETAILS group by MOVIE"
        mycursor.execute(sql)
        with mydb:
            Table_Output = from_db_cursor(mycursor)
        print(Table_Output)
        Surety()
            
    elif CHOZ ==2:
        mydb = mysql.connector.connect(host="localhost",user="root",password="root",port=3306,database="Customer")
        mycursor = mydb.cursor(buffered=True)
        sql = "Select City, SUM(No_Of_Seats) AS 'Sales' from DETAILS group by City"
        mycursor.execute(sql)
        with mydb:
            Table_Output = from_db_cursor(mycursor)
        print(Table_Output)

        Surety()

    else:
        print("Choose A Valid Option!")
        Sales_Menu()
    
#GRAPHS MENU FXN
def Graphs_Menu():
    print("1.Sales \n"
          "2.Popularity\n"
          "3.Movie Ratings")
    moz=int(input("Chose One: "))
    if moz==1:
        Sales_Graph()
    elif moz==2:
        Popularity_Graph()()
    elif moz==3:
        Movie_Rating()
    else:
        print("CHOOSE A VAILD OPTION!")
        Graphs_Menu()

#MAIN EXIT FRN
def Main_Exit():
    print("ARE YOU SURE YOU WANT TO EXIT?\n"
          "1. YES\n"
          "2. NO")
    CLOSE=int(input("Choose: "))
    if CLOSE== 1:
        print("Thank You For Using Our Program!")

    elif CLOSE== 2:
        print(" ")
        print("Welcome Back!")
        print(" ")
        main()

    else :
        print("Enter A Valid Choice!")
        Main_Exit()


    
#SURETY FXN
def Surety():
    print(" ")
    print("THANK YOU FOR USING OUR PROGRAM!\n"
          "WHAT DO YOU WISH TO DO?\n"
               "1. CONTINUE\n"
               "2. EXIT")
    print(" ")
    FIRM=int(input("SELECT WHAT YOU WISH TO DO: "))
    print(" ")

    if FIRM==1:
        main()

    elif FIRM ==2:
        print("Thank You For Booking With Us!")        

    else:
        print("ENTER A VALID CHOICE!")
        Surety()
        


#POPULARITY GRAPH FXN
def Popularity_Graph():
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",port=3306,database="Customer")
    mycursor = mydb.cursor()
    mycursor.execute("Select SUM(No_Of_Seats),MOVIE from DETAILS group by MOVIE")
    result = mycursor.fetchall
    SUMM = []
    MOVIE = []
    for i in mycursor:
            MOVIE.append(i[0])
            SUMM.append(i[1])

    plt.bar(SUMM,MOVIE)
    plt.xlabel("City Names")
    plt.ylabel("Sales")
    plt.title("City Wise Popularity")
    plt.xticks(rotation = -45)
    print("CLICK THE GRAPH TO CONTINUE!")
    plt.waitforbuttonpress(0)
    plt.close()
    Surety()
    



#SALES GRAPH FXN
def Sales_Graph():
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",port=3306,database="Customer")
    mycursor = mydb.cursor()
    mycursor.execute("select City, Count(Order_ID) from Details Group by City")
    result = mycursor.fetchall
    City = []
    Order_ID = []
    for i in mycursor:
            City.append(i[0])
            Order_ID.append(i[1])
    plt.bar(City, Order_ID)
    plt.xlabel("City Names")
    plt.ylabel("Sales")
    plt.title("City Wise Sales Report")
    print("PRESS ANY BUTTON TO CONTINUE!")
    plt.waitforbuttonpress(0)
    plt.close()
    Surety()

def Movie_Rating():
    file=pd.read_csv("C:/Users/HP5CD/OneDrive/Documents/Movie Ticket Booking and Management System/Movie Rating.csv")
    file.plot(kind='bar',x='Movie',color=['yellow','red'],edgecolor='Green')
    plt.ylabel("Rating")
    plt.xlabel("Movies")
    print("PRESS ANY BUTTON TO CONTINUE!")
    plt.waitforbuttonpress(0)
    plt.close()
    Surety()

#ORRDER SUMMARY
def OrderSum():
    OID=int(input("Please Enter Your Order ID: "))
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",port=3306,database="Customer")
    mycursor = mydb.cursor(buffered=True)
    
    with mydb:
        ACC = [OID]
        retrieve = "SELECT * FROM Details where Order_ID=%s"
        mycursor.execute(retrieve,(ACC))
        table = from_db_cursor(mycursor) 
    print(table)

    print(" \n"
          "NOTE: PLEASE REMEMBER YOUR ORDER ID TO VIEW YOUR ORDER SUMMARY IN THE FUTURE!")
    Surety()


#CITIES FUNCTION
def Cities():
    Cit={'Cities':pd.Series(["Mumbai",
                         "Delhi-NCR",
                         "Jaipur",
                         "Bangalore",
                         "Hydrabad" ,
                         "Chandigarh"], index=[1,2,3,4,5,6])}
    Cities=pd.DataFrame(Cit)
    print(Cities)
    


#WORK Function
def WORK():
    Cities()

    ID=random.randint(151,2000)
    array1=np.array(["Liger (Hindi 2D)","Liger (Hindi 2D)","Liger (Hindi 2D)","Liger (Hindi 2D)","Liger (Hindi 2D)","Liger (Hindi 2D)"])
    array2=np.array(['Dragon Ball Super: Super Hero (English 2D)','Dragon Ball Super: Super Hero (English 2D)','Dragon Ball Super: Super Hero (English 2D)','Dragon Ball Super: Super Hero (English 2D)','Dragon Ball Super: Super Hero (English 2D)','Dragon Ball Super: Super Hero (English 2D)'])
    array3=np.array(['Laal Singh Chaddha (Hindi 2D)','Laal Singh Chaddha (Hindi 2D)','Laal Singh Chaddha (Hindi 2D)','Laal Singh Chaddha (Hindi 2D)','Laal Singh Chaddha (Hindi 2D)','Laal Singh Chaddha (Hindi 2D)'])
    array4=np.array(['Dobaaraa (Hindi 2D)','Dobaaraa (Hindi 2D)',"Karthikeya 2 (Hindi 2D)",'Dobaaraa (Hindi 2D)',"Karthikeya 2 (Hindi 2D)","Karthikeya 2 (Hindi 2D)"])
    array5=np.array(['Nope (English 2D)',"Kathikeya 2 (Hindi 2D)",'Nope (English 2D)',"Kathikeya 2 (Hindi 2D)",'Nope (English 2D)','Nope (English 2D)'])
    array6=np.array(['Bullet Train (English 2D)','Bullet Train (English 2D)',"Raksha Bandhan (Hindi 2D)","Nope (English 2D)",'Bullet Train (English 2D)','Bullet Train (English 2D)'])
    array7=np.array(['Top Gun:Maverick (English 2D)','Top Gun:Maverick (English 2D)',"Aanchhi (Hindi 2D)","Thiruchitrambalam (Tamil 2D)",'Top Gun:Maverick (English 2D)''Top Gun:Maverick (English 2D)'])
    Mavie=pd.DataFrame([array1,array2,array3,array4,array5,array6,array7],index=[1,2,3,4,5,6,7],columns=['Mumbai','Delhi-NCR','Jaipur','Bangalore','Hydrabad','Chandigarh'])

    city=int(input("Enter your city: "))
    if city==1: #Mumbai
        city_entry="Mumbai"
        print(Mavie.loc[:,'Mumbai'])
        print(" ")
        
    elif city==2: #Delhi-NCR
        city_entry="Delhi-NCR"
        print(print(Mavie.loc[:,'Delhi-NCR']))
        print(" ")
        
    elif city==3: #Jaipur
        city_entry="Jaipur"
        print(Mavie.loc[:,'Jaipur'])
        print(" ")
        
    elif city==4: #Bangalore
        city_entry="Bangalore"
        print(Mavie.loc[:,'Bangalore'])
        print(" ")
        
    elif city==5: #Hyderabad
        city_entry="Hyderabad"
        print(Mavie.loc[:,'Hyderabad'])
        print(" ")
        
    elif city==6: #Chandigarh
        city_entry="Chandigarh"
        print(Mavie.loc[:,'Chandigarh'])
        print(" ")
    else:
        print(" ")
        print("ENTER A VALID NUMBER!")
        print(" ")
        print("PLEASE CHOOSE AGAIN!")
        WORK()
        
    
    mov=int(input("Please enter the your movie number: "))
    print(" ")
#Mumbai
    if city==1 and mov==1:
        movie_entry="Liger (Hindi 2D)"
        print("1.Maison PVR:Library Hall,Jio World Drive    2.INOX:Atria Mall    3.Cinepolis:Nexus Seawoods")
    elif city==1 and mov==2:
        movie_entry="Dragon Ball Super: Super Hero (English 2D)"
        print("1.Maison PVR:Library Hall,Jio World Drive    2.INOX:Atria Mall    3.Cinepolis:Nexus Seawoods")
    elif city==1 and mov==3:
        movie_entry="Laal Singh Chaddha (Hindi 2D)"
        print("1.Maison PVR:Library Hall,Jio World Drive    2.INOX:Atria Mall    3.Cinepolis:Nexus Seawoods")
    elif city==1 and mov==4:
        movie_entry="Dobaaraa (Hindi 2D)"
        print("1.Maison PVR:Library Hall,Jio World Drive    2.INOX:Atria Mall    3.Cinepolis:Nexus Seawoods")
    elif city==1 and mov==5:
        movie_entry="Nope (English 2D)"
        print("1.Maison PVR:Library Hall,Jio World Drive    2.INOX:Atria Mall    3.Cinepolis:Nexus Seawoods")
    elif city==1 and mov==6:
        movie_entry="Bullet Train (English 2D)"
        print("1.Maison PVR:Library Hall,Jio World Drive    2.INOX:Atria Mall    3.Cinepolis:Nexus Seawoods")
    elif city==1 and mov==7:
        movie_entry="Top Gun:Maverick (English 2D)"
        print("1.Maison PVR:Library Hall,Jio World Drive    2.INOX:Atria Mall    3.Cinepolis:Nexus Seawoods")
#Delhi-NCR
    elif city==2 and mov==1:
        movie_entry="Liger (Hindi 2D)"
        print("1.PVR:Ambience    2.INOX:Sapphire 90 Mall    3.Cinepolis:Grand Venice Mall")
    elif city==2 and mov==2:
        movie_entry="Dragon Ball Super: Super Hero (English 2D)"
        print("1.PVR:Ambience    2.INOX:Sapphire 90 Mall    3.Cinepolis:Grand Venice Mall")
    elif city==2 and mov==3:
        movie_entry="Laal Singh Chaddha (Hindi 2D)"
        print("1.PVR:Ambience    2.INOX:Sapphire 90 Mall    3.Cinepolis:Grand Venice Mall")
    elif city==2 and mov==4:
        movie_entry="Dobaaraa (Hindi 2D)"
        print("1.PVR:Ambience    2.INOX:Sapphire 90 Mall    3.Cinepolis:Grand Venice Mall")
    elif city==2 and mov==5:
        movie_entry="Karthikeya 2 (Hindi 2D)"
        print("1.PVR:Ambience    2.INOX:Sapphire 90 Mall    3.Cinepolis:Grand Venice Mall")
    elif city==2 and mov==6:
        movie_entry="Bullet Train (English 2D)"
        print("1.PVR:Ambience    2.INOX:Sapphire 90 Mall    3.Cinepolis:Grand Venice Mall")
    elif city==2 and mov==7:
        movie_entry="Top Gun:Maverick (English 2D)"
        print("1.PVR:Ambience    2.INOX:Sapphire 90 Mall    3.Cinepolis:Grand Venice Mall")
#Jaipur
    elif city==3 and mov==1:
        movie_entry="Liger (Hindi 2D)"
        print("1.Miraj Cinemas:Entertainment Paradise    2.INOX:Elements Mall    3.Cinepolis:World Trade Park")
    elif city==3 and mov==2:
        movie_entry="Dragon Ball Super: Super Hero (English 2D)"
        print("1.Miraj Cinemas:Entertainment Paradise    2.INOX:Elements Mall    3.Cinepolis:World Trade Park")
    elif city==3 and mov==3:
        movie_entry="Laal Singh Chaddha (Hindi 2D)"
        print("1.Miraj Cinemas:Entertainment Paradise    2.INOX:Elements Mall    3.Cinepolis:World Trade Park")
    elif city==3 and mov==4:
        movie_entry="Karthikeya 2 (Hindi 2D)"
        print("1.Miraj Cinemas:Entertainment Paradise    2.INOX:Elements Mall    3.Cinepolis:World Trade Park")
    elif city==3 and mov==5:
        movie_entry="Nope (English 2D)"
        print("1.Miraj Cinemas:Entertainment Paradise    2.INOX:Elements Mall    3.Cinepolis:World Trade Park")
    elif city==3 and mov==6:
        movie_entry="Raksha Bandhan (Hindi 2D)"
        print("1.Miraj Cinemas:Entertainment Paradise    2.INOX:Elements Mall    3.Cinepolis:World Trade Park")
    elif city==3 and mov==7:
        movie_entry="Aanchhi (Hindi 2D)"
        print("1.Miraj Cinemas:Entertainment Paradise    2.INOX:Elements Mall    3.Cinepolis:World Trade Park")
#Bangalore
    elif city==4 and mov==1:
        movie_entry="Liger (Hindi 2D)"
        print("1.PVR:Gold VR Bengaluru    2.INOX:Garuda Mall    3.Cinepolis:Orion East Mall")
    elif city==4 and mov==2:
        movie_entry="Dragon Ball Super: Super Hero (English 2D)"
        print("1.PVR:Gold VR Bengaluru    2.INOX:Garuda Mall    3.Cinepolis:Orion East Mall")
    elif city==4 and mov==3:
        movie_entry="Laal Singh Chaddha (Hindi 2D)"
        print("1.PVR:Gold VR Bengaluru    2.INOX:Garuda Mall    3.Cinepolis:Orion East Mall")
    elif city==4 and mov==4:
        movie_entry="Dobaaraa (Hindi 2D)"
        print("1.PVR:Gold VR Bengaluru    2.INOX:Garuda Mall    3.Cinepolis:Orion East Mall")
    elif city==4 and mov==5:
        movie_entry="Karthikeya 2 (Hindi 2D)"
        print("1.PVR:Gold VR Bengaluru    2.INOX:Garuda Mall    3.Cinepolis:Orion East Mall")
    elif city==4 and mov==6:
        movie_entry="Nope (English 2D)"
        print("1.PVR:Gold VR Bengaluru    2.INOX:Garuda Mall    3.Cinepolis:Orion East Mall")
    elif city==4 and mov==7:
        movie_entry="Thiruchitrambalam (Tamil 2D)"
        print("1.PVR:Gold VR Bengaluru    2.INOX:Garuda Mall    3.Cinepolis:Orion East Mall")
#Hyderabad
    elif city==5 and mov==1:
        movie_entry="Liger (Hindi 2D)"
        print("1.PVR: Central Mall    2.INOX:Sattva Necklace    3.Cinepolis:Mantra Mall")
    elif city==5 and mov==2:
        movie_entry="Dragon Ball Super: Super Hero (English 2D)"
        print("1.PVR: Central Mall    2.INOX:Sattva Necklace    3.Cinepolis:Mantra Mall")
    elif city==5 and mov==3:
        movie_entry="Laal Singh Chaddha (Hindi 2D)"
        print("1.PVR: Central Mall    2.INOX:Sattva Necklace    3.Cinepolis:Mantra Mall")
    elif city==5 and mov==4:
        movie_entry="Karthikeya 2 (Hindi 2D)"
        print("1.PVR: Central Mall    2.INOX:Sattva Necklace    3.Cinepolis:Mantra Mall")
    elif city==5 and mov==5:
        movie_entry="Nope (English 2D)"
        print("1.PVR: Central Mall    2.INOX:Sattva Necklace    3.Cinepolis:Mantra Mall")
    elif city==5 and mov==6:
        movie_entry="Bullet Train (English 2D)"
        print("1.PVR: Central Mall    2.INOX:Sattva Necklace    3.Cinepolis:Mantra Mall")
    elif city==5 and mov==7:
        movie_entry="Top Gun:Maverick (English 2D)"
        print("1.PVR: Central Mall    2.INOX:Sattva Necklace    3.Cinepolis:Mantra Mall")
#Chandigarh
    elif city==6 and mov==1:
        movie_entry="Liger (Hindi 2D)"
        print("1.PVR:Elante    2.INOX:Dhillon Plaza    3.Cinepolis:Bestech Square")
    elif city==6 and mov==2:
        movie_entry="Dragon Ball Super: Super Hero (English 2D)"
        print("1.PVR:Elante    2.INOX:Dhillon Plaza    3.Cinepolis:Bestech Square")
    elif city==6 and mov==3:
        movie_entry="Laal Singh Chaddha (Hindi 2D)"
        print("1.PVR:Elante    2.INOX:Dhillon Plaza    3.Cinepolis:Bestech Square")
    elif city==6 and mov==4:
        movie_entry="Karthikeya 2 (Hindi 2D)"
        print("1.PVR:Elante    2.INOX:Dhillon Plaza    3.Cinepolis:Bestech Square")
    elif city==6 and mov==5:
        movie_entry="Nope (English 2D)"
        print("1.PVR:Elante    2.INOX:Dhillon Plaza    3.Cinepolis:Bestech Square")
    elif city==6 and mov==6:
        movie_entry="Bullet Train (English 2D)"
        print("1.PVR:Elante    2.INOX:Dhillon Plaza    3.Cinepolis:Bestech Square")
    elif city==6 and mov==7:
        movie_entry="Top Gun:Maverick (English 2D)"
        print("1.PVR:Elante    2.INOX:Dhillon Plaza    3.Cinepolis:Bestech Square")
    else:
        print("Enter A valid number!")
        print(' ')
        print("PLEASE CHOOSE AGAIN!")
        WORK()

    print(" ")
    venue=int(input("Enter venue: "))
    print(" ")

#Mumbai

    if city==1 and mov==1 and venue==1:
        venue_entry="Maison PVR:Library Hall,Jio World Drive"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==1 and venue==2:
        venue_entry="INOX:Atria Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==1 and venue==3:
        venue_entry="Cinepolis:Nexus Seawoods"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==2 and venue==1:
        venue_entry="Maison PVR:Library Hall,Jio World Drive"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==2 and venue==2:
        venue_entry="INOX:Atria Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==2 and venue==3:
        venue_entry="Cinepolis:Nexus Seawoods"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==3 and venue==1:
        venue_entry="Maison PVR:Library Hall,Jio World Drive"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==3 and venue==2:
        venue_entry="INOX:Atria Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==3 and venue==3:
        venue_entry="Cinepolis:Nexus Seawoods"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==4 and venue==1:
        venue_entry="Maison PVR:Library Hall,Jio World Drive"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==4 and venue==2:
        venue_entry="INOX:Atria Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==4 and venue==3:
        venue_entry="Cinepolis:Nexus Seawoods"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==5 and venue==1:
        venue_entry="Maison PVR:Library Hall,Jio World Drive"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==5 and venue==2:
        venue_entry="INOX:Atria Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==5 and venue==3:
        venue_entry="Cinepolis:Nexus Seawoods"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==6 and venue==1:
        venue_entry="Maison PVR:Library Hall,Jio World Drive"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==6 and venue==2:
        venue_entry="INOX:Atria Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==6 and venue==3:
        venue_entry="Cinepolis:Nexus Seawoods"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==7 and venue==1:
        venue_entry="Maison PVR:Library Hall,Jio World Drive"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==7 and venue==2:
        venue_entry="INOX:Atria Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==1 and mov==7 and venue==3:
        venue_entry="Cinepolis:Nexus Seawoods"
        print("1. 3:30 pm           2. 9:00 pm")

    #Delhi-NCR

    elif city==2 and mov==1 and venue==1:
        venue_entry="PVR:Ambience"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==1 and venue==2:
        venue_entry="INOX:Sapphire 90 Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==1 and venue==3:
        venue_entry="Cinepolis:Grand Venice Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==2 and venue==1:
        venue_entry="PVR:Ambience"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==2 and venue==2:
        venue_entry="INOX:Sapphire 90 Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==2 and venue==3:
        venue_entry="Cinepolis:Grand Venice Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==3 and venue==1:
        venue_entry="PVR:Ambience"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==3 and venue==2:
        venue_entry="INOX:Sapphire 90 Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==3 and venue==3:
        venue_entry="Cinepolis:Grand Venice Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==4 and venue==1:
        venue_entry="PVR:Ambience"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==4 and venue==2:
        venue_entry="INOX:Sapphire 90 Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==4 and venue==3:
        venue_entry="Cinepolis:Grand Venice Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==5 and venue==1:
        venue_entry="PVR:Ambience"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==5 and venue==2:
        venue_entry="INOX:Sapphire 90 Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==5 and venue==3:
        venue_entry="Cinepolis:Grand Venice Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==6 and venue==1:
        venue_entry="PVR:Ambience"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==6 and venue==2:
        venue_entry="INOX:Sapphire 90 Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==6 and venue==3:
        venue_entry="Cinepolis:Grand Venice Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==7 and venue==1:
        venue_entry="PVR:Ambience"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==7 and venue==2:
        venue_entry="INOX:Sapphire 90 Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==2 and mov==7 and venue==3:
        venue_entry="Cinepolis:Grand Venice Mall"
        print("1. 3:30 pm           2. 9:00 pm")

    #Jaipur

    elif city==3 and mov==1 and venue==1:
        venue_entry="Miraj Cinemas:Entertainment Paradise"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==1 and venue==2:
        venue_entry="INOX:Elements Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==1 and venue==3:
        venue_entry="Cinepolis:World Trade Park"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==2 and venue==1:
        venue_entry="Miraj Cinemas:Entertainment Paradise"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==2 and venue==2:
        venue_entry="INOX:Elements Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==2 and venue==3:
        venue_entry="Cinepolis:World Trade Park"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==3 and venue==1:
        venue_entry="Miraj Cinemas:Entertainment Paradise"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==3 and venue==2:
        venue_entry="INOX:Elements Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==3 and venue==3:
        venue_entry="Cinepolis:World Trade Park"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==4 and venue==1:
        venue_entry="Miraj Cinemas:Entertainment Paradise"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==4 and venue==2:
        venue_entry="INOX:Elements Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==4 and venue==3:
        venue_entry="Cinepolis:World Trade Park"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==5 and venue==1:
        venue_entry="Miraj Cinemas:Entertainment Paradise"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==5 and venue==2:
        venue_entry="INOX:Elements Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==5 and venue==3:
        venue_entry="Cinepolis:World Trade Park"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==6 and venue==1:
        venue_entry="Miraj Cinemas:Entertainment Paradise"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==6 and venue==2:
        venue_entry="INOX:Elements Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==6 and venue==3:
        venue_entry="Cinepolis:World Trade Park"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==7 and venue==1:
        venue_entry="Miraj Cinemas:Entertainment Paradise"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==7 and venue==2:
        venue_entry="INOX:Elements Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==3 and mov==7 and venue==3:
        venue_entry="Cinepolis:World Trade Park"
        print("1. 3:30 pm           2. 9:00 pm")

    #Bangalore

    elif city==4 and mov==1 and venue==1:
        venue_entry="PVR:Gold VR"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==1 and venue==2:
        venue_entry="INOX:Garuda Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==1 and venue==3:
        venue_entry="Cinepolis:Orion East Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==2 and venue==1:
        venue_entry="PVR:Gold VR"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==2 and venue==2:
        venue_entry="INOX:Garuda Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==2 and venue==3:
        venue_entry="Cinepolis:Orion East Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==3 and venue==1:
        venue_entry="PVR:Gold VR"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==3 and venue==2:
        venue_entry="INOX:Garuda Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==3 and venue==3:
        venue_entry="Cinepolis:Orion East Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==4 and venue==1:
        venue_entry="PVR:Gold VR"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==4 and venue==2:
        venue_entry="INOX:Garuda Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==4 and venue==3:
        venue_entry="Cinepolis:Orion East Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==5 and venue==1:
        venue_entry="PVR:Gold VR"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==5 and venue==2:
        venue_entry="INOX:Garuda Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==5 and venue==3:
        venue_entry="Cinepolis:Orion East Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==6 and venue==1:
        venue_entry="PVR:Gold VR"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==6 and venue==2:
        venue_entry="INOX:Garuda Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==6 and venue==3:
        venue_entry="Cinepolis:Orion East Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==7 and venue==1:
        venue_entry="PVR:Gold VR"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==7 and venue==2:
        venue_entry="INOX:Garuda Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==4 and mov==7 and venue==3:
        venue_entry="Cinepolis:Orion East Mall"
        print("1. 3:30 pm           2. 9:00 pm")

    #Hyderabad

    elif city==5 and mov==1 and venue==1:
        venue_entry="PVR:Central Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==1 and venue==2:
        venue_entry="INOX:Sattva Necklace"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==1 and venue==3:
        venue_entry="Cinepolis:Mantra Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==2 and venue==1:
        venue_entry="PVR:Central Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==2 and venue==2:
        venue_entry="INOX:Sattva Necklace"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==2 and venue==3:
        venue_entry="Cinepolis:Mantra Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==3 and venue==1:
        venue_entry="PVR:Central Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==3 and venue==2:
        venue_entry="INOX:Sattva Necklace"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==3 and venue==3:
        venue_entry="Cinepolis:Mantra Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==4 and venue==1:
        venue_entry="PVR:Central Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==4 and venue==2:
        venue_entry="INOX:Sattva Necklace"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==4 and venue==3:
        venue_entry="Cinepolis:Mantra Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==5 and venue==1:
        venue_entry="PVR:Central Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==5 and venue==2:
        venue_entry="INOX:Sattva Necklace"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==5 and venue==3:
        venue_entry="Cinepolis:Mantra Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==6 and venue==1:
        venue_entry="PVR:Central Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==6 and venue==2:
        venue_entry="INOX:Sattva Necklace"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==6 and venue==3:
        venue_entry="Cinepolis:Mantra Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==7 and venue==1:
        venue_entry="PVR:Central Mall"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==7 and venue==2:
        venue_entry="INOX:Sattva Necklace"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==5 and mov==7 and venue==3:
        venue_entry="Cinepolis:Mantra Mall"
        print("1. 3:30 pm           2. 9:00 pm")

    #Chandigarh

    elif city==6 and mov==1 and venue==1:
        venue_entry="PVR:Elante"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==1 and venue==2:
        venue_entry="INOX:Dhillon Plaza"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==1 and venue==3:
        venue_entry="Cinepolis:Bestech Square"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==2 and venue==1:
        venue_entry="PVR:Elante"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==2 and venue==2:
        venue_entry="INOX:Dhillon Plaza"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==2 and venue==3:
        venue_entry="Cinepolis:Bestech Square"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==3 and venue==1:
        venue_entry="PVR:Elante"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==3 and venue==2:
        venue_entry="INOX:Dhillon Plaza"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==3 and venue==3:
        venue_entry="Cinepolis:Bestech Square"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==4 and venue==1:
        venue_entry="PVR:Elante"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==4 and venue==2:
        venue_entry="INOX:Dhillon Plaza"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==4 and venue==3:
        venue_entry="Cinepolis:Bestech Square"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==5 and venue==1:
        venue_entry="PVR:Elante"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==5 and venue==2:
        venue_entry="INOX:Dhillon Plaza"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==5 and venue==3:
        venue_entry="Cinepolis:Bestech Square"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==6 and venue==1:
        venue_entry="PVR:Elante"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==6 and venue==2:
        venue_entry="INOX:Dhillon Plaza"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==6 and venue==3:
        venue_entry="Cinepolis:Bestech Square"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==7 and venue==1:
        venue_entry="PVR:Elante"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==7 and venue==2:
        venue_entry="INOX:Dhillon Plaza"
        print("1. 3:30 pm           2. 9:00 pm")
    elif city==6 and mov==7 and venue==3:
        venue_entry="Cinepolis:Bestech Square"
        print("1. 3:30 pm           2. 9:00 pm")
    else:
        print(" ")
        print("Enter A valid number!")
        print(" ")
        print("PLEASE CHOOSE AGAIN!")
        WORK()
        print(" ")

#TIME INPUT

    print(" ")
    TIME=int(input("Choose your Show Timing: "))
    print(" ")
    
#IMAGE POP UP

    if TIME==1:
        time_entry="3:30 pm"
        NOZ=int(input("Please Enter total No. of Seats you Wish to Buy: "))
        img = cv2.imread("C:\\Users\\HP5CD\\OneDrive\\Documents\\Movie Ticket Booking and Management System\\LAY.png", 0)
        cv2.imshow('LAY',img)
        cv2.waitKey(0)
        cv2.destroyWindow('LAY')
        SAT=input("Refer to the image for Selection\n"
                  "Seperate Multiple Seats Using a Comma\n"
                  "For Example: L34,L35\n"
                  "Enter your Seat Number :")
#IMAGE POP UP        
        
    elif TIME==2:
        time_entry="9:00 pm"
        NOZ=int(input("Please Enter total No. of Seats you Wish to Buy: "))
        img = cv2.imread("C:\\Users\\HP5CD\\OneDrive\\Documents\\Movie Ticket Booking and Management System\\LAY.png", 0)
        cv2.imshow('LAY',img)
        cv2.waitKey(0)
        cv2.destroyWindow('LAY')
        SAT=input("Refer to the image for Selection\n"
                  "Seperate Multiple Seats Using a Comma\n"
                  "For Example: L34,L35\n"
                  "Enter your Seat Number :")
        
        

    else:
        print("Enter A valid number!")
        print(" ")
        print("PLEASE CHOOSE AGAIN!")
        WORK()

    print(" ")
    CustName=input("Please enter your Full Name: ")
    print(" ")
    Mobile=int(input("Please Enter your Mobile Number: "))

#SQL ENTRY COMMIT
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",port=3306,database="Customer")
    mycursor = mydb.cursor()
    sql = "INSERT INTO Details (Order_ID, Name, Contact_Number, City, Movie, Venue, Show_Time, Seat_Number, No_of_Seats) VALUES (%s, %s, %s,%s, %s, %s,%s,%s,%s)"
    val = (ID,CustName , Mobile, city_entry, movie_entry,venue_entry,time_entry, SAT,NOZ)
    mycursor.execute(sql, val)
    mydb.commit()

    with mydb:
        ODD = [ID]
        retrieve = "SELECT * FROM Details where Order_ID=%s"
        mycursor.execute(retrieve,(ODD))
        Table_Output = from_db_cursor(mycursor) 
    print(" ")
    print("Your Order Summary is a follows:")
    print(Table_Output)

    print(" \n"
          "NOTE: PLEASE REMEMBER YOUR ORDER ID TO VIEW YOUR ORDER SUMMARY IN THE FUTURE!\n"
          " \n"
          "Thank You! For Booking a ticket with Us!\n")
    print(" ")
    Surety()
               
        
        

#MAIN Function
def main():
    print("Available Users:")
    print("1. Customer")
    print("2. Administrator")
    print("3. Exit")
    print(" ")
    access=int(input("Choose : "))
    if access==1:
        print(" ")
        Customer()
    elif access==2:
        print(" ")
        Admin()
    elif access==3:
        Main_Exit()
    else:
        print(" ")
        print("Enter Correct Choice!")
        main()

main()
