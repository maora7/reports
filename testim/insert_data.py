import pyodbc

# Define your connection string
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-40ILBA5\\SQLEXPRESS;"
    "DATABASE=Spinframe;"
    "UID=maor;"
    "PWD=123456;"
    "MultipleActiveResultSets=True;"
    "App=EntityFramework"
)

try:
    # Establish a connection to the database
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Define your insert query
    insert_query = """
    INSERT INTO [Spinframe].[dbo].[MonitoringReportMailingRules]
    ([BusinessId], [Name], [Email], [DailyRegCars], [SMSAlert], [MobileNumber], [CarNotification])
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    # Define the data to be inserted
    data = (217, 'maor test13 ', 'maora@spinframe.co.il', 1, 0, '1234567890', 0)

    # Execute the query with the data
    cursor.execute(insert_query, data)

    # Commit the transaction
    conn.commit()
    print("Data inserted successfully!")

    # Run a select query to verify the data
    select_query = "SELECT TOP 10 * FROM [Spinframe].[dbo].[MonitoringReportMailingRules] ORDER BY Id DESC"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Print the selected rows
    print("Verifying the inserted data:")
    for row in rows:
        print(row)

except pyodbc.Error as ex:
    print("SQL Error:", ex)
except Exception as ex:
    print("Error:", ex)
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
