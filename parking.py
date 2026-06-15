import os
import platform
import mysql.connector

# ── DB CONNECTION ────────────────────────────────────────────────
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="a1234",
        port=3307,
        database="parking"
    )

mydb = get_connection()
mycursor = mydb.cursor()


# ── ADD PARKING RECORD ───────────────────────────────────────────
def Add_Record():
    L = []
    id1 = int(input("Enter the parking number : "))
    L.append(id1)
    pname1 = input("Enter the Parking Name: ")
    L.append(pname1)
    level1 = input("Enter level of parking : ")
    L.append(level1)
    freespace1 = input("Is there any freespace or not (YES/NO): ")
    L.append(freespace1)
    vehicleno1 = input("Enter the Vehicle Number : ")
    L.append(vehicleno1)
    nod1 = int(input("Enter total number of days for parking: "))
    L.append(nod1)

    Payment1 = nod1 * 20  # 20 per day
    L.append(Payment1)

    stud = tuple(L)
    sql = 'INSERT INTO parkmaster12 (pid, pnm, level, freespace, vehicleno, nod, payment) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql, stud)
    mydb.commit()
    print("Record added successfully. Payment: ₹", Payment1)


# ── VIEW PARKING RECORDS ─────────────────────────────────────────
def Rec_View():
    print("\nSelect the search criteria:")
    print("1. Parking Number")
    print("2. Parking Name")
    print("3. Level No")
    print("4. All")
    ch = int(input("Enter the choice: "))

    if ch == 1:
        s = int(input("Enter Parking no: "))
        rl = (s,)
        sql = "SELECT * FROM parkmaster12 WHERE pid=%s"
        mycursor.execute(sql, rl)
    elif ch == 2:
        s = input("Enter Parking Name: ")
        rl = (s,)
        sql = "SELECT * FROM parkmaster12 WHERE pnm=%s"
        mycursor.execute(sql, rl)
    elif ch == 3:
        s = input("Enter Level of Parking: ")
        rl = (s,)
        sql = "SELECT * FROM parkmaster12 WHERE level=%s"
        mycursor.execute(sql, rl)
    elif ch == 4:
        sql = "SELECT * FROM parkmaster12"
        mycursor.execute(sql)
    else:
        print("Invalid choice.")
        return

    res = mycursor.fetchall()
    print("\nDetails about Parking:")
    print("(ParkingID | Name | Level | FreeSpace | VehicleNo | Days | Payment)")
    print("-" * 65)
    for x in res:
        print(x)
    print("Task completed.")


# ── ADD VEHICLE DETAIL ───────────────────────────────────────────
def Vehicle_Detail():
    L = []
    vid1 = int(input("Enter Vehicle ID (matching Parking ID): "))
    L.append(vid1)
    vnm1 = input("Enter Vehicle Name/Model Name: ")
    L.append(vnm1)
    dateofpur1 = input("Enter purchase date (YYYY-MM-DD): ")
    L.append(dateofpur1)
    vdt = tuple(L)
    sql = "INSERT INTO vehicle (pid, vnm, dateofpur) VALUES (%s,%s,%s)"
    mycursor.execute(sql, vdt)
    mydb.commit()
    print("Vehicle record added successfully.")


# ── VIEW VEHICLE WITH JOIN ───────────────────────────────────────
def Vehicle_View():
    vid1 = int(input("Enter the vehicle ID to view details: "))
    sql = '''SELECT parkmaster12.pid, parkmaster12.pnm, parkmaster12.vehicleno,
                    vehicle.pid, vehicle.vnm
             FROM parkmaster12
             INNER JOIN vehicle ON parkmaster12.pid = vehicle.pid
             AND vehicle.pid = %s'''
    rl = (vid1,)
    mycursor.execute(sql, rl)
    res = mycursor.fetchall()
    print("\nParking+Vehicle Details:")
    print("(ParkingID | ParkingName | VehicleNo | VehicleID | VehicleModel)")
    print("-" * 65)
    for x in res:
        print(x)
    print("Task completed.")


# ── REMOVE VEHICLE ───────────────────────────────────────────────
def remove():
    vid1 = int(input("Enter the vehicle ID to delete: "))
    rl = (vid1,)
    sql = "DELETE FROM vehicle WHERE pid=%s"
    mycursor.execute(sql, rl)
    mydb.commit()
    print("Vehicle record removed.")


# ── MENU ─────────────────────────────────────────────────────────
def Menu():
    print("\n" + "=" * 40)
    print("     PARKING MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Parking Detail")
    print("2. View Parking Detail")
    print("3. Add Vehicle Detail")
    print("4. Remove Vehicle Record")
    print("5. View Vehicle Details (with Parking)")
    print("0. Exit")
    print("=" * 40)

    input_dt = int(input("Select an option: "))

    if input_dt == 1:
        Add_Record()
    elif input_dt == 2:
        Rec_View()
    elif input_dt == 3:
        Vehicle_Detail()
    elif input_dt == 4:
        remove()
    elif input_dt == 5:
        Vehicle_View()
    elif input_dt == 0:
        print("Goodbye.")
        exit()
    else:
        print("Invalid choice. Try again.")


# ── RUN LOOP ─────────────────────────────────────────────────────
def runAgain():
    Menu()
    runAgn = input('\nRun again? (Y/N): ')
    while runAgn.lower() == 'y':
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        Menu()
        runAgn = input('\nRun again? (Y/N): ')


if __name__ == "__main__":
    runAgain()
