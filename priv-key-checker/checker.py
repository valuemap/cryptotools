#import only neccessary functions
from bitcoin import privkey_to_address
from blockcypher import get_address_overview, from_satoshis
#import re
from itertools import product

#replacements
#b6 gq g9 G6 Ll LI L1 O0 S5 VU Z2 #mind opposite direction
#a ci, d cl, g cj, m rn, A fi, W VV

#types of automatic modifications:
# - 1 char replacement (of any)
#replace_one_char(str,str,str)

#different solution https://stackoverflow.com/questions/52382444/replace-combinations-of-characters

#https://stackoverflow.com/questions/52382444/replace-combinations-of-characters
#https://stackoverflow.com/questions/14841652/string-replacement-combinations 
#https://stackoverflow.com/questions/44181772/python-character-replacement-combinations-with-a-list
#generates different combinations of the string (using options)
def filler(word):
    combos = [(c,) if c not in options else options[c] for c in word]
    return (''.join(o) for o in product(*combos))

options = {
    'b': ['b', '6',],
    'g': ["g", "q", "9", "6"],
    'L': ["L", "1", "i"],
    'O': ["O", "0"],
    'S': ["S", "5"],
    #'T': ["T", "7"],
    'V': ["V", "U"],
    'Z': ["Z", "2"]}


#priv key input and overwrites combinations to file
a = filler('5HpHagT65TZzG1PH3CSu63k8DbpvD8sSip4nEB3kEsreAnchuDf')
f = open('WordList.txt', 'w+')
lst = list(a)
#btw calling generator affects it and it won't return any more items
for item in lst:
    f.write(item+'\n')
f.close()

#other ideas
# - char replacement (of specific char)
# - move 1 char further or back (doesn't work for couple of first chars)
# - insert specific char or string somewhere or add at the end



def check_priv_key(priv_key):
    try:
        address = privkey_to_address(priv_key)
        print("try priv key {}".format(priv_key))
        print("generated public key {}".format(address))
        addr_overview = get_address_overview(address) #getting address data
        for key,value in addr_overview.items(): #getting info from address overview
            #check past transactions
            if key == 'final_n_tx': #check for any transactions in the past
                if value > 0: #if exist, then address has been used
                    print("Address has been used {0} times in the past".format(value))
                    print(priv_key)
                    print(address)
            #check balance
            if key == 'final_balance': #check for funds in the address
                if value > 0: #if any btc left on address, print details
                    print("Address has balance of {0}".format(from_satoshis(value,'btc')))
    except: 
        #this happens if string doesn't generate valid key
        return None

#read from the file with generated combinations and check if valid key            
filehandler = open("WordList.txt", "r") # open in read mode 'r'
content = filehandler.readlines()
content = [x.strip() for x in content]

for item in content:
    check_priv_key(item)
