import pandas as pand
import csv
from datetime import datetime

class CSV:
    CSV_FILE= "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]


    @classmethod
    def initialize_csv(cls):
        try:
            pand.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pand.DataFrame(columns= cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False )
    @classmethod 
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open (cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)

        print("Entry addeed Successfully")
CSV.initialize_csv()
CSV.add_entry("07/03/2024", 325.76, "Income", "Salary" )
        