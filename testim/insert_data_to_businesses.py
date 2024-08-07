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
    INSERT INTO [Spinframe].[dbo].[Businesses]
    ([name], [assignedToBusiness], [address], [phone], [type], [cretatedOn], [modifiedOn], [logoPath], [FTP_address], [FTP_username], [FTP_password], [ip_cameras], [website], [comments], [businessCode], [CameraSystem], [NVR_Address], [IsPort])
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    # 218
    data = (
        "maorallrs1", 218, None, None, "Agency", "2019-08-20 13:05:34.000", None, None, None, None, None, None, None, None, None, "Pro", None, 0
    )

    # Execute the query with the data
    cursor.execute(insert_query, data)

    # Commit the transaction
    conn.commit()
    print("Data inserted successfully!")

    # Run a select query to verify the data
    select_query = "SELECT TOP 10 * FROM [Spinframe].[dbo].[Businesses] ORDER BY Id DESC"
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
