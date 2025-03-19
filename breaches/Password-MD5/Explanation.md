# Vulnérabilité: Exposition de hash MD5

## Découverte

### Scan DIRB
Un scan DIRB a révélé plusieurs répertoires du serveur, notamment:
```
==> DIRECTORY: http://10.13.248.133/admin/
==> DIRECTORY: http://10.13.248.133/whatever/
+ http://10.13.248.133/whatever/htpasswd (CODE:200|SIZE:38)
```

### Exploitation
Dans le chemin `http://10.13.248.133/whatever/`, nous avons découvert un fichier `htpasswd` téléchargeable contenant un mot de passe root hashé en MD5 (32 caractères).

### Vulnérabilité 
Le hash MD5 utilisé est vulnérable à:
- Attaques par force brute
- Recherches dans des tables rainbow préexistantes

## Protection
- Utiliser des algorithmes de hachage modernes
- Ne pas exposer de fichiers de mots de passe, même hashés
- Stocker les informations sensibles dans le backend