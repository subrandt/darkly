# Vulnérabilité: Manipulation de formulaire côté client

## Découverte

En inspectant le code source de la page de réinitialisation de mot de passe, nous avons identifié un champ email caché avec une valeur prédéfinie.

```html
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```

### Exploitation

1. Nous avons utilisé l'inspecteur d'éléments du navigateur pour modifier la valeur du champ caché:
   - Valeur originale: `webmaster@borntosec.com`
   - Modifiée en: `test@exemple.com`

2. En soumettant le formulaire modifié, le système a traité la demande de réinitialisation avec notre email au lieu de celui de l'administrateur.

3. Cela nous a permis de recevoir un lien de réinitialisation pour un compte privilégié.

## Protection

- Ne jamais faire confiance aux données côté client
- Vérifier l'identité de l'utilisateur côté serveur
- Implémenter une validation serveur des adresses email autorisées
- Éviter de coder en dur des valeurs sensibles dans le HTML