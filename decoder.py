import wget
import os
import hashlib


def search_hash(hash_query, file):
    match = 0
    with open(file) as f:
        for line in f:
            psw = line.rstrip()
            hash_psw = hashlib.sha256(psw.encode('UTF8')).hexdigest()

            if hash_query == hash_psw:
                match = 1
                print("Match! It is {} !".format(psw))
    if match == 0:
        print("No match. Try using a different wordlist.")

def main(url, hash_query):

    print("Getting rockyou weak password list...")
    response = wget.download(url, "rockyou.txt")
    print("\n")

    search_hash(hash_query ,"rockyou.txt")

    os.remove("rockyou.txt")


if __name__ == "__main__":

    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou-75.txt"
    hash_query = input("Please input a SHA-256 hash. If you want the default test run, press ENTER: ")

    if hash_query == "":
        hash_query = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
    main(url, hash_query) 
