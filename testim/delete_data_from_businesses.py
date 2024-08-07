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

    # Define your delete query
    delete_query = """
    DELETE FROM [Spinframe].[dbo].[Businesses]
    WHERE [id] = ?
    """

    # Define the data for the delete operation
    id = 331
    # Execute the query with the data
    cursor.execute(delete_query, id)

    # Commit the transaction
    conn.commit()
    print("Data deleted successfully!")

    # Run a select query to verify the remaining data
    select_query = "SELECT TOP 10 * FROM [Spinframe].[dbo].[Businesses] ORDER BY Id DESC"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Print the selected rows
    print("Verifying the remaining data:")
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
