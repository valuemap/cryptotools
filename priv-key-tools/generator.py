#import only neccessary functions
from bitcoin import random_key,privkey_to_address

#generate random key and assign it to the variable
#private_key = random_key()

#check string as private key
#private_key = int("0x1", 16) #first private key
private_key = int("0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140", 16) #last private key

#use generated private key to generate BTC address and assign it to variable
address = privkey_to_address(private_key)

#print both private key and it's public address
print(private_key)
print(address)