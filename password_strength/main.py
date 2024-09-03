# passord styrkesjekker
# input passord
# sjekker passord
# hvis den ikke er sterk nok så gir man tips
# tips: bruk tegn, nummer, bokstaver
import re

# fra KPR prosjektet
def load_words(word_list): # loads words into a list
    wordlist = list() 
    try:    
        with open(word_list, encoding="utf-8") as f: # specify encoding aswell
            for line in f:
                wordlist.append(line.strip('\n'))
        return wordlist
    except IOError:
        print("Error 1: Filen eksister ikke, vennligst prøv en annen fil")


def validate_password(password, word_list):
    if password in word_list:
        return "Passordet ditt er veldig vanlig, velg noe unikt!"
    
    if len(password) < 8:
        return "Passordet ditt er ikke langt nok, øk lengden!"

    if not re.search(r'[A-Z]', password):
        return "Du mangler store bokstaver, legg til noen store bokstaver!"
        
    if not re.search(r'[a-z]', password):
        return "Du mangler små bokstaver i passordet, legg til noen små bokstaver for å få ett sterkere passord!"
    
    if not re.search(r'\d', password):
        return "Du mangler tall i passordet, legg til noen tall så får du et sterkere passord!"
    
    if not re.search(r"[.,?£$?=&!@%-]", password): # dette er det jeg brukte for alle tegnene https://owasp.org/www-community/password-special-characters noen er eksludert
        return "Passordet mangler tegn, prøv ett av disse tegnene i passordet!\n. , ? £ $ ? = & ! @  % -"
    
    else:
        return "Passordet ditt er sterkt!"

def main():
    while True:
        print("Velkommmen til passord sjekker #1337")
        input_checker = str(input("Vil du sjekke passordet ditt?\nTast Y (Ja)\nHvis ikke blir du kastet ut av programmet.\n")).lower()
        
        if input_checker == "y":
            wordlist = load_words("./passwords.txt") # loads most common passwords into a list
            password = str(input("Skriv inn passordet ditt for å sjekke om det er et bra passord!\n"))
            print(validate_password(password, wordlist)) # takes in password and wordlist
        else:
            break


if __name__ == "__main__":
        main()