# Enkel Kalkulator


def addisjon(n1, n2):
    return n1 + n2
    
def subtraksjon(n1, n2):
    return n1 - n2

def multiplikasjon(n1, n2):
    return n1 * n2

def divisjon(n1, n2):
    return n1 / n2

def main():
    print("Velg en operasjon å utføre")
    print("1. Addisjon\n"\
    "2. Subtraksjon\n"\
    "3. Multiplikasjon\n"\
    "4. Divisjon\n")
    
    operasjon = int(input("velg et tall som tillhører operasjonen\n"))
    n1 = int(input("Vennligst gi det første tallet\n"))
    n2 = int(input("Vennligst oppgi det andre tallet\n"))
    
    match operasjon:
        case 1:
            print(addisjon(n1, n2))
        case 2:
            print(subtraksjon(n1, n2))
        case 3:
            print(multiplikasjon(n1, n2))
        case 4:
            print(divisjon(n1, n2))
        case _:
            print("Ugyldig operasjon vennligst prøv igjen senere.")

if __name__ == "__main__":
    main()        
            
    