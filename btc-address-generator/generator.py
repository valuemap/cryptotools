#import only neccessary functions
from bitcoin import random_key,privkey_to_address

#generate random key and assign it to the variable
private_key = random_key()

#use generated private key to generate BTC address and assign it to variable
address = privkey_to_address(private_key)

#print both private key and it's public address
print(private_key)
print(address)