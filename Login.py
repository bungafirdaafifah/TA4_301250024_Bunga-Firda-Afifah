data_username = "admin"
data_password = "python"

total_percobaan = 0
for i in range(3):    
    username = str(input("Username: "))
    password = str(input("Password: "))

    if data_username == username and data_password == password:
        print("Berhasil masuk, username password benar")
        break
    
    if data_username != username or data_password != password:
        total_percobaan += 1
        if total_percobaan == 3:
            print("Maksimal percobaan 3 kali")
        else:
            print("Login gagal sebanyak", total_percobaan, "kali")
        continue