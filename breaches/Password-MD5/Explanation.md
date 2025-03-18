## Decouverte

### Scan avec DIRB

```
darkly git:(main) ✗ dirb http://10.13.248.133/ /usr/share/wordlists/dirb/common.txt

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Mon Mar 17 17:37:29 2025
URL_BASE: http://10.13.248.133/
WORDLIST_FILES: /usr/share/wordlists/dirb/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://10.13.248.133/ ----
==> DIRECTORY: http://10.13.248.133/admin/                                                         
==> DIRECTORY: http://10.13.248.133/audio/                                                         
==> DIRECTORY: http://10.13.248.133/css/                                                           
==> DIRECTORY: http://10.13.248.133/errors/                                                        
+ http://10.13.248.133/favicon.ico (CODE:200|SIZE:1406)                                            
==> DIRECTORY: http://10.13.248.133/fonts/                                                         
==> DIRECTORY: http://10.13.248.133/images/                                                        
==> DIRECTORY: http://10.13.248.133/includes/                                                      
+ http://10.13.248.133/index.php (CODE:200|SIZE:6892)                                              
==> DIRECTORY: http://10.13.248.133/js/                                                            
+ http://10.13.248.133/robots.txt (CODE:200|SIZE:53)                                               
==> DIRECTORY: http://10.13.248.133/whatever/                                                      
                                                                                                   
---- Entering directory: http://10.13.248.133/admin/ ----
==> DIRECTORY: http://10.13.248.133/admin/css/                                                     
==> DIRECTORY: http://10.13.248.133/admin/fonts/                                                   
+ http://10.13.248.133/admin/index.php (CODE:200|SIZE:1432)                                        
                                                                                                   
---- Entering directory: http://10.13.248.133/audio/ ----
                                                                                                   
---- Entering directory: http://10.13.248.133/css/ ----
==> DIRECTORY: http://10.13.248.133/css/images/                                                    
                                                                                                   
---- Entering directory: http://10.13.248.133/errors/ ----
                                                                                                   
---- Entering directory: http://10.13.248.133/fonts/ ----
                                                                                                   
---- Entering directory: http://10.13.248.133/images/ ----
                                                                                                   
---- Entering directory: http://10.13.248.133/includes/ ----
                                                                                                   
---- Entering directory: http://10.13.248.133/js/ ----
                                                                                                   
---- Entering directory: http://10.13.248.133/whatever/ ----
+ http://10.13.248.133/whatever/htpasswd (CODE:200|SIZE:38)                                        
                                                                                                   
---- Entering directory: http://10.13.248.133/admin/css/ ----
==> DIRECTORY: http://10.13.248.133/admin/css/images/                                              
                                                                                                   
---- Entering directory: http://10.13.248.133/admin/fonts/ ----
                                                                                                   
---- Entering directory: http://10.13.248.133/css/images/ ----
                                                                                                   
---- Entering directory: http://10.13.248.133/admin/css/images/ ----
                                                                                                   
-----------------
END_TIME: Mon Mar 17 17:37:42 2025
DOWNLOADED: 64568 - FOUND: 5
D: 64568 - FOUND: 5
```

### Recuperer le fichier
http://10.13.248.133/whatever/ dans ce path on peut telecharger un fichier contenant un mdp root de 128 bits soit 32 caracteres tres similaire aux hashe en MD5 

### Vulnerabilite 
Le protocole de hachage utilisé est MD5, mais il est vulnérable aux attaques par force brute ainsi qu'à l'utilisation de tables de hachage préconstruites (rainbow tables).

### Prevention 
Ne pas utiliser d'algorithme de hashage obsolete
