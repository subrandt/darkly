# Vulnérabilité: Contenu caché

## Découverte

### Scan DIRB
Nous avons utilisé DIRB pour scanner le serveur cible et découvrir plusieurs dossiers accessibles:
```
darkly git:(main) ✗ dirb http://10.13.248.133/ /usr/share/wordlists/dirb/common.txt
```

Le scan a révélé:
- Plusieurs répertoires standard (/admin/, /css/, /js/, etc.)
- Un fichier robots.txt contenant une référence à un dossier `.hidden/`
- Un fichier potentiellement sensible: `/whatever/htpasswd`

### Exploitation
En explorant le fichier `robots.txt`, nous avons trouvé le chemin vers `.hidden/` qui contenait de nombreux sous-dossiers avec des noms cryptiques.

Pour trouver le flag, nous avons:
1. Parcouru tous les dossiers avec un script de scraping
2. Comparé la longueur des réponses pour identifier le contenu pertinent

## Protection
Pour corriger cette vulnérabilité:
- Ne pas stocker de fichiers sensibles dans des répertoires accessibles publiquement
- Déplacer tout contenu sensible vers le backend
- Configurer correctement les contrôles d'accès