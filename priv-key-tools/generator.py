#import only neccessary functions
from bitcoin import random_key,privkey_to_address
from blockcypher import get_latest_block_height, get_total_balance, get_address_overview, from_satoshis

#int("0x1", 16) #first private key
#int("0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140", 16) #last private key

for i in range(35):
    #print(hex(i)) #show iterator in hex to reflect priv key format
    priv_key = i #generate priv_key from int anyway
    address = privkey_to_address(priv_key)
    addr_overview = get_address_overview(address) #getting address data
    #[print(key, value) for key, value in addr_overview.items()] #this would show dict with address info
    for key,value in addr_overview.items(): #getting info from address overview
        if key == 'final_balance': #check for funds in the address
            if value > 0: #if any btc left on address, print details
                print(priv_key)
                print(address)
                print(from_satoshis(value,'btc'))
