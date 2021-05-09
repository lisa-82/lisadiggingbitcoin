from hashlib import sha256

import time

TOTALNUMBEROFGUESSESJOKER = 3828883559

def jokersrediculouscypher(enterstring):
    return sha256(enterstring.encode("ascii")).hexdigest()

def diggingforbitcoin(hereablocknumberdummy
, inprivitywithjoker, youroldjokerbitcoin, openingzeroofbitcoin):
    starting_stringofbeginning = '0' * openingzeroofbitcoin

    for yourluckyguess in range(TOTALNUMBEROFGUESSESJOKER):
        enterstring = str(hereablocknumberdummy) + inprivitywithjoker + youroldjokerbitcoin + str(yourluckyguess)
        yourcurrentbitcoinhash = jokersrediculouscypher(enterstring)
        if yourcurrentbitcoinhash.startswith(starting_stringofbeginning):
            print(f"Dang, joker, here's your just reward with the lucky guess value:{yourluckyguess}")
            return yourcurrentbitcoinhash

    raise BaseException(f"Just couldn't do it brah. I tried {TOTALNUMBEROFGUESSESJOKER} guesses.")

if __name__=='__main__':
    inprivitywithjoker='''
    Alice->Howard Hughes->20,
    Jokerundastairs->Jay Sebring->45,
    Lisbeth Salander->Lisa Rowe-3
    '''
    
    numberofzerosinfrontofhash = 3 
    
    thisiswhereyourdiggingbeginsjoker = time.time()
    
    print("dig joker")
    
    yourcurrentbitcoinhash = diggingforbitcoin(5,inprivitywithjoker,'000db0dc6cee89fddd2ac434a2be028410c782adc97144e2993c4d6be0b2edf2', numberofzerosinfrontofhash)
    
    total_time = str((time.time() - thisiswhereyourdiggingbeginsjoker))
    
    print(f"stop digging joker: {total_time} seconds")
    
    print(yourcurrentbitcoinhash)