# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

#Define the SQL query variables
sql1 = """ SELECT employeeNumber,lastName FROM employees; """
sql2 = """ SELECT lastName,employeeNumber FROM employees; """
sql3 = """ SELECT 
            lastName,
            employeeNumber AS ID
            FROM employees;
        """
sql4 = """  SELECT *,
                CASE
                WHEN jobTitle = "President" OR 
                    jobTitle = "VP Sales" OR
                    jobTitle = "VP Marketing" THEN "Executive"
                ELSE "Not Executive"
                END AS role
            FROM employees;
        """
sql5 = """  SELECT length(lastName) AS name_length
            FROM employees;
        """

sql6 = """  SELECT substr(jobTitle,1,2) AS short_title
            FROM employees;
        """

sql7 = """  SELECT round(priceEach * quantityOrdered) AS total_price
            FROM orderDetails;
         """

sql8 = """  SELECT orderDate,
                strftime("%d", orderDate) AS day,
                strftime("%m", orderDate) AS month,
                strftime("%Y", orderDate) AS year
            FROM orders;
         """

# SELECT filtering to select employeeNumber and lastName from employees table
df_first_five = pd.read_sql(sql1,conn)


# SELECT filtering to select employeeNumber and lastName in reverse order from employees table
df_five_reverse = pd.read_sql(sql2,conn)


# Use SELECT with aliasing to rename the employee number column as 'ID' 
df_alias = pd.read_sql(sql3,conn)

#Use CASE to bin where the jobTitles of President, VP Sales, or VP Marketing have the 'role' of "Executive"
# The rest of the employees are supposed to be "Not Executive"
df_executive = pd.read_sql(sql4,conn)

# use SELECT and SQL built-in functions for string manipulation
# find the length of the last name for all employees, and return only this data as a new column called name_length
df_name_length = pd.read_sql(sql5,conn)

# use SELECT and SQL built-in functions for string manipulation 
# find the first two letters of each employees job title, and return only this data as a new column called short_title
df_short_title = pd.read_sql(sql6,conn)

# use SELECT to the return total amount for all orders, calculated as the sum of rounded total prices
# use pandas sum() to evaluate the sum of each column(total_price column) hence the total amount of all orders
sum_total_price = pd.read_sql(sql7, conn).sum()

# use SELECT to return the original orderDate column, and 3 other columns
# The 3 other columns should display the orderDate's day, month, and year respectiveley
df_day_month_year = pd.read_sql(sql8, conn)



#Test cases
# Add code below and run file to see data from employees table
""" print("---------------------Employee Data---------------------")
print(df_first_five) 
#print(df_five_reverse) 
#print(df_alias)
#print(df_executive)
#print(df_name_length)
#print(df_short_title)
print("-------------------End Employee Data-------------------") """

# Add the code below and run the file to see data from order details table
""" print("------------------Order Details Data------------------")
print(sum_total_price)
print("----------------End Order Details Data----------------") """

# Add the code below and run the file to see data from orders table
""" print("------------------Order Details Data------------------")
print(df_day_month_year)
print("----------------End Order Details Data----------------") """


# disconnect the database
conn.close()