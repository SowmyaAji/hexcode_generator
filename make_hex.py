from scraper import get_common_codes
import secrets
import hashlib
import sqlite3

def get_hex():
    return secrets.token_hex(4).upper() # use secrets to generate a secure hex token rather than just a random choice hex string. 
    
def validate_in_common(random_string: str) -> bool:
    common_codes = get_common_codes() # check if hex code is there in common magic hexcodes used in the software industry
    return any(random_string in code for code in common_codes)

def validate_no_repeats(random_string: str) -> bool:
    return len(set(random_string.split())) <= 2 # to avoid repeated chars in the hex code,allow at the max two characters that can repeat in the code

# def validate_no_sequences(random_string: str) -> bool:
    

def generate_hashed_string(random_string: str) -> str:
    return hashlib.sha256(random_string.encode('utf-8')).hexdigest()  # uses hashing to store the hex code generated and compares the hex with the ones in the db column
    
def validate_not_used(random_string: str, hashed_string:str, list_limit:int) -> str:
    #  store hex string in db
    conn = sqlite3.connect("hexcodes.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS hexcodes (id int PRIMARY KEY, hexcode_hash char(65) NOT NULL)")
    c.execute("SELECT hexcode_hash FROM hexcodes")
    results = c.fetchall()
    for row in results:
        print(row)
    if len(results) == list_limit: # if the first iteration of unique hexcodes are done drop the data base and restart the process of storing
        c.execute("DROP TABLE hexcodes")
        conn.commit()
        print("All valid hexcodes exhausted, restarting ...")
    else:
        if hashed_string not in results:
            c.execute("INSERT INTO hexcodes (hexcode_hash) VALUES (?)",(hashed_string, ))
            conn.commit()
            return random_string
        else:
            print("Hex code already used earlier")
        
def main():
    new_hex = get_hex()
    hashed_string = generate_hashed_string(new_hex)
    check_hex = validate_not_used(new_hex, hashed_string, 3)
    if check_hex :
        if not (validate_in_common(check_hex) and validate_no_repeats(check_hex)):
            print("New Hex code: ", check_hex)
        else:
            print("Error, hexcode is invalid.")

if __name__ == "__main__":
    main()
    