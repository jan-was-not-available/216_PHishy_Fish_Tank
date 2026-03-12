import rsa as rsa

key = int(input("Enter the Decryption Key: " ))
mod_value = int(input("Enter the Modulus: " ))
encrypted_msg = input("What message would you like to decrypt (No brackets): ")

#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
print (rsa.decrypt(key,mod_value , msg))


# Line 1: "# start_monitoring.py"
# Line 2: "from fishtank import FishTankCLI"
# Line 3: "app = FishTankCLI()"
# Line 4: "app.main()"