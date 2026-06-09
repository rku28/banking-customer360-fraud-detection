#This file generates the fake data set needed for the project

import pandas as pd 
import random
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()

os.makedirs("data",exist_ok=True)

#---------------------
#Customers Fake Data
#---------------------


customers=[] 

#creating list and appending , because we need multiple records

for i in range(1,1001):
    customers.append({
    #We use dictionaries because each dictionary represents one row of data, and later Pandas can easily convert a list of dictionaries into a table.    
    "customer_id": i,
    "name":fake.name(),
    "age":random.randint(18,80),
    "city":fake.city()
    })


customers_df= pd.DataFrame(customers)

customers_df.to_csv(
    "data/customers.csv",
    index=False
    )

#-----------------------
#Accounts Fake Data
#-----------------------

accounts = []

for i in range(1,2001):
    accounts.append({
        "account_id":i,
        "customer_id":random.randint(1,1000),
        "account_type":random.choice(["SAVINGS","CHEQUING"]),
        "balance":random.randint(100,50000)
    })


accounts_df = pd.DataFrame(accounts)

accounts_df.to_csv(
    "data/accounts.csv",
    index=False
    )


#----------------------------
#Transactions Fake Data
#----------------------------


transactions = []

for i in range(1,50001):
    date= datetime.now() - timedelta(days = random.randint(0,365))
    transactions.append({
        "transaction_id" :i,
        "transaction_type" : random.choice(["Debit","Credit"]),
        "account_id" : random.randint(1,2000),
        "amount" : round(random.uniform(5,20000),2),
        "Location" : fake.city(),
        "timestamp" : date
    })

transactions_df = pd.DataFrame(transactions)

transactions_df.to_csv(
    "data/transactions.csv",
    index=False
)

#---------------------------
#Login Event
#---------------------------

logins=[]

for i in range(1,1000):
    date = datetime.now() - timedelta(days=random.randint(0,365))
    logins.append({
        "customer_id":random.randint(1,1000),
        "device":random.choice(["Mobile","Desktop"]),
        "login_status": random.choice(["Success","Failed"]),
        "timestamp": date
    })


logins_df = pd.DataFrame(logins)

logins_df.to_csv(
    "data/logins.csv",
    index=False
)

print("Done")

