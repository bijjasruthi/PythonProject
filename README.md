# 👉 Expense Tracker

*A Python-based finance tracking tool to log, manage, and visualize income and expenses.*



---

## 🚀 Project Overview
The **Personal Finance Tracker** is a Python-based application that allows users to **log financial transactions, organize them into categories, retrieve transaction summaries, and visualize income and expenses over time**. The data is stored in a **CSV file**, making it easy to integrate with Excel or Google Sheets.

This project is designed to help you practice **Python, Pandas, CSV file handling, and Matplotlib for data visualization**.

---

## ✨ Key Features
✅ **Log Transactions**: Add income and expenses with details like date, amount, category, and description.  
✅ **Retrieve Transactions**: View financial records within a given date range.  
✅ **Summarize Finances**: Get total **income, expenses, and net savings**.  
✅ **Data Visualization**: Generate a graph of **income vs. expenses** over time.  
✅ **Persistent Storage**: Saves all data in a `CSV` file for easy retrieval.  
✅ **User-Friendly CLI Interface**: Simple command-line prompts to interact with the tool.  

---

## 📂 Project Structure
```bash
Personal-Finance-Tracker/
│── finance_data.csv        # CSV file storing transaction data
│── main.py                 # Main program file
│── data_entry.py           # Handles user input validation
│── README.md               # Project documentation
│── requirements.txt        # Required dependencies
```

---

## 🛠 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/Personal-Finance-Tracker.git
cd Personal-Finance-Tracker
```

### **2️⃣ Create a Virtual Environment (Optional)**
```sh
python3 -m venv env
source env/bin/activate   # MacOS/Linux
env\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```sh
python main.py
```

---

## 📊 How It Works
### **Adding a Transaction**
```sh
Enter the date of the transaction (DD-MM-YYYY) or press Enter for today's date: 07-03-2024
Enter the amount: 325.76
Enter the category (I for Income, E for Expense): I
Enter a description: Salary
```
✔ **Transaction added successfully!**

### **Viewing Transactions & Summary**
```sh
Enter start date (DD-MM-YYYY): 01-07-2024
Enter end date (DD-MM-YYYY): 30-07-2024
```
📊 **Output:**
```
Date         Amount    Category   Description
07-07-2024   300.00    Income     Freelance Work
15-07-2024   120.00    Expense    Groceries
27-07-2024   500.00    Income     Salary

Summary:
Total Income: $800.00
Total Expenses: $120.00
Net Savings: $680.00
```

### **Generating a Graph**
```sh
Do you want to see a plot? (Y/N): Y
```
A **line chart** is displayed showing income and expense trends over time.

---

## 🔍 Future Improvements
🔹 **Database Integration**: Use SQLite or PostgreSQL instead of CSV.  
🔹 **Graphical User Interface (GUI)**: Build a **Tkinter** or **Flask-based** interface.  
🔹 **Expense Categories**: Allow custom categories instead of just `Income` and `Expense`.  
🔹 **Monthly/Yearly Summaries**: Aggregate transactions by month or year.  

---

## 👨‍💻 Contributing
Contributions are welcome! Feel free to **fork** this repository, improve it, and submit a **pull request**.

### **Steps to Contribute**
1. **Fork the repository** 🍴  
2. **Clone the forked repo**:  
   ```sh
   git clone https://github.com/bijjasruthi/PythonProject
   ```
3. **Create a new branch**:  
   ```sh
   git checkout -b feature-branch
   ```
4. **Make your changes and commit**:  
   ```sh
   git commit -m "Added new feature"
   ```
5. **Push changes and create a pull request** 🎉  

---

## 🐝 License
This project is licensed under the **MIT License** - you are free to use, modify, and distribute it.

---

## ⭐ Support the Project
If you found this project helpful, **give it a ⭐ on GitHub!**

📬 **Follow me on GitHub for more projects!**  
🔗 [GitHub Profile](https://github.com/bijjasruthi)

