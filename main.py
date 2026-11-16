import psycopg

#Establish a connection to the postgres database
conn = psycopg.connect(
        dbname = "hospital_data",
        user = "postgres",
        password = "SproutLeaf68#",
        host = "localhost",
        port = 5432
)

print("Connected to PostgresSQL!")

cursor = conn.cursor()


print("""===== Hospital Appointment Tracker =====
1. View Patients
2. View Doctors
3. View Appointments
4. Search Patients
5. Exit""")


def show_patients():
      cursor.execute('SELECT * FROM patients')
      patients = cursor.fetchall()    
      for row in patients:
          print(f"\nID: {row[0]}")
          print(f"Name: {row[1]} {row[2]}")
          print(f"Date of Birth: {row[3]}")

def show_doctors():
      cursor.execute('SELECT * FROM doctors')
      doctors = cursor.fetchall()    
      for row in doctors:
          print(f"\nID: {row[0]}")
          print(f"Name: {row[1]} {row[2]}")
          print(f"Specialty: {row[3]}")

def show_appointments():
      cursor.execute('SELECT * FROM appointments')
      appointments = cursor.fetchall()    
      for row in appointments:
          print(f"\nID: {row[0]}")
          print(f"Patient_id: {row[1]}")
          print(f"Doctor_id: {row[2]}")
          print(f"Date: {row[3]}")
          print(f"Reason: {row[4]}")

def search_patients():
        search = input('Enter patient name: ')
        cursor.execute('SELECT * FROM patients WHERE first_name ILIKE %s', (search,))
        patients = cursor.fetchall()
        for row in patients:
            print(f"ID: {row[0]}")
            print(f"Name: {row[1]} {row[2]}")
            print(f"Date of Birth: {row[3]}")

active = True
while active:
    user_input = input("Choose a number 1-5: ")
    if user_input == "1":
        show_patients()
    elif user_input == "2":
        show_doctors()
    elif user_input == "3":
        show_appointments()
    elif user_input == "4":
        search_patients()
    elif user_input == "5":
        active = False
    else:
        print('Invalid option. Please choose 1-5')
    
conn.close() # this closes the connection
