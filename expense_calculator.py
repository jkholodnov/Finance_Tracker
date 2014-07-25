import urllib2
import sys
from Queue import *
from threading import Thread
from bs4 import BeautifulSoup
import sqlite3 as lite
from sets import Set
from math import *
import matplotlib.pyplot as plt
import numpy as np

class ostream:
    def __init__(self, file):
        self.file = file
        
    def __lshift__(self, obj):
        self.file.write(str(obj));
        return self
cout = ostream(sys.stdout)
cerr = ostream(sys.stderr)
endl = '\n'


def controller():
    selection = 0
    while(selection != "4"):
        cout << "___________________________" << endl 
        cout << "| Please make a selection |" << endl 
        cout << "|_________________________|" << endl 
        cout << "|To input an expense: \t1 |" << endl 
        cout << "|To calculate expenses:\t2 |" << endl 
        cout << "|To reset the database:\t3 |" << endl
        cout << "|To exit this program: \t4 |" << endl
        cout << "|_________________________|" << endl 


        selection = raw_input("$:")
        
        if(selection=="1"):
            input_Expenses()
            

        if(selection=="2"):
            calculate_Expenses()
            

        if(selection=="3"):
            create_tables()


def calculate_Expenses():
    con = lite.connect('expenses.db')
    with con:

        cur = con.cursor()
        cur.execute("Select * from expenses")

        expenses = cur.fetchall()
    con.close()
    for expense in expenses:
        print expense

    
def create_tables():
    con = lite.connect('expenses.db')

    with con:
        
        cur = con.cursor()   

        cur.execute("DROP TABLE IF EXISTS expenses") 
        
        cur.execute("CREATE TABLE expenses(type TEXT, location TEXT, month TEXT, year int, cost INT, memo TEXT)")

    con.commit()
    con.close()

class purchase(object):
    def __init__(self,v,x,y,z,z1):
        self.type=v
        self.location = x
        self.date = y
        self.cost = z
        self.year = "undefined"
        self.fix_date()
        self.description = z1

    def fix_date(self):
        month = self.date[0:2]
        theyear = self.date[3:]
        self.year = theyear
        if(month=="01"):
            self.date = "January"
        if(month=="02"):
            self.date = "February"
        if(month=="03"):
            self.date = "March"
        if(month=="04"):
            self.date = "April"
        if(month=="05"):
            self.date = "May"
        if(month=="06"):
            self.date = "June"
        if(month=="07"):
            self.date = "July"
        if(month=="08"):
            self.date = "August"
        if(month=="09"):
            self.date = "September"
        if(month=="10"):
            self.date = "October"
        if(month=="11"):
            self.date = "November"
        if(month=="12"):
            self.date = "December"

    def update_DB(self):
        con = lite.connect('expenses.db')
        cur = con.cursor()

        with con:
            query = "'" + str(self.type) + "','" + str(self.location) + "','" + str(self.date) + "'," + str(self.year) + "," + str(self.cost) + ",'" + str(self.description) + "'"
            cur.execute("INSERT INTO expenses VALUES("+query.upper()+")")
    def print_info(self):
        cout << self.description << "\t" << self.type << '\t' << self.location << '\t' << self.date << '\t' << self.year << '\t' << self.cost << endl

def input_Expenses():
    inputted_expenses = []

    addMore = "1"
    while (addMore =="1"):
        
        thetype= raw_input("Type of Purchase:(options: Food, Gas, Drinks, Entertainment, Bills, Other):\t")
        thelocation= raw_input("Location of Purchase:(ex: Amazon, Starbucks, BP, Online):\t")
        thedate= raw_input("Date of Purchase:(ex: MM-YYYY):\t")
        thecost= raw_input("Cost of Purchase:(ex: 23.00):\t")
        memo= raw_input("Description of Purchase:(ex:Coffee, Rent):\t")
        currentPurchase = purchase(thetype,thelocation,thedate,thecost,memo)
        inputted_expenses.append(currentPurchase)

        addMore = raw_input("Would you like to add more purchases? (1 for yes):\t")
    
    print "Would you like to save these expenses?"
    
    for expense in inputted_expenses:
        expense.print_info()
    tocommit = raw_input("Y/N:\t")
    if(tocommit == "y") or (tocommit == "Y"):
        for expense in inputted_expenses:
            expense.update_DB()

if __name__ == '__main__':
    controller()

#TODO
#Get date
#Figure out month
#Set up recurring monthly payments