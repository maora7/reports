import pyodbc
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-40ILBA5\\SQLEXPRESS;"
    "DATABASE=Spinframe;"
    "UID=maor;"
    "PWD=123456"
)
try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    delete_query = """
    DELETE FROM [Spinframe].[dbo].[MonitoringReportMailingRules]
    WHERE [Id] = ?
    """
    ids = [83]
    for id in ids:
        cursor.execute(delete_query, id)

    cursor.execute(delete_query, id)
    conn.commit()
    print("Data deleted successfully!")
    cursor.execute("SELECT TOP 10 * FROM [Spinframe].[dbo].[MonitoringReportMailingRules] ORDER BY Id DESC")
    rows = cursor.fetchall()
    print("Verifying the remaining data:")
    for row in rows:
        print(row)
        
except pyodbc.Error as ex:
    print("SQL Error:", ex)
except Exception as ex:
    print("Error:", ex)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
