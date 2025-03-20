# XSS dans le Formulaire de Feedback

> ⚠️ **ATTENTION:** Le flag ne fonctionne pas, ci-dessous recap d'une attaque XSS sur des champs de formulaires.

## Découverte
Nous avons découvert une vulnérabilité XSS (Cross-Site Scripting) sur la page de feedback du site web.
http://10.13.248.97/index.php?page=feedback

## Vulnérabilité
Faille de type **"Stored XSS"** combinant:
1. Contournement de la validation de longueur côté client
2. Absence d'échappement des caractères spéciaux HTML

## Exploitation
1. Identification du formulaire avec limitation côté client:
   ```html
   <input name="txtName" type="text" size="30" maxlength="10">
   ```

2. Contournement de la limitation en modifiant l'attribut `maxlength` via les outils développeur

3. Injection de code JavaScript dans le champ "Name":
   ```
   <script>alert(1)</script>
   ```

4. Soumission du formulaire et exécution du script injecté

5. Obtention du flag:
   ```
   THE FLAG IS : 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E
   ```

## Mécanisme technique
1. La validation côté client est insuffisante et facilement contournable
2. L'application stocke les entrées utilisateur sans filtrage
3. Les entrées sont affichées directement dans le HTML sans échappement
4. Le navigateur interprète et exécute le code JavaScript injecté

## Prévention
- Valider les entrées côté serveur (longueur ET contenu)
- Échapper systématiquement les caractères spéciaux HTML
- Utiliser des en-têtes Content-Security-Policy
- Implémenter une liste blanche des caractères autorisés