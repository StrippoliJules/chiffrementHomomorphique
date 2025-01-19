# Projet de Calcul Homomorphique

Ce projet illustre un flux de travail complet de chiffrement, calcul homomorphique et déchiffrement en utilisant Python et la bibliothèque TenSEAL.

---

## Prérequis

- **Python 3.8+** installé.
- **TenSEAL** installé. Pour l'installer, exécutez la commande suivante :

```bash
pip install tenseal
```

---

## Fichiers

1. **`programme1_chiffrement.py`**
   - Chiffre les données et génère les fichiers suivants :
     - `context_prive.json`
     - `context_public.json`
     - `blocs1.json`

2. **`calcul.py`**
   - Lit les fichiers `context_public.json` et `blocs1.json`.
   - Effectue un calcul homomorphique.
   - Produit le fichier `blocs2.json`.

3. **`dechiffrement.py`**
   - Lit les fichiers `context_prive.json` et `blocs2.json`.
   - Déchiffre les données et affiche le résultat en clair.

---

## Utilisation

### 1. Sur la machine qui chiffre (Machine A)

Exécutez le script `programme1_chiffrement.py` :

```bash
python programme1_chiffrement.py
```

Cela générera les fichiers suivants :
- `context_prive.json` (garde le fichier **privé** sur cette machine).
- `context_public.json`
- `blocs1.json`

Envoyez les fichiers `context_public.json` et `blocs1.json` à la machine qui effectuera le calcul (Machine B).

### 2. Sur la machine qui calcule (Machine B)

Exécutez le script `calcul.py` :

```bash
python calcul.py
```

Cela produira le fichier :
- `blocs2.json`

Renvoyez le fichier `blocs2.json` à la machine qui déchiffre (Machine A).

### 3. Sur la machine qui déchiffre (Machine A)

Exécutez le script `dechiffrement.py` :

```bash
python dechiffrement.py
```

Le script lira les fichiers `context_prive.json` et `blocs2.json`, puis affichera le résultat déchiffré en clair.

---

## Notes

- Assurez-vous que les fichiers échangés entre les machines sont transmis de manière sécurisée.
- Ne partagez **jamais** le fichier `context_prive.json`, car il contient des informations sensibles nécessaires pour le déchiffrement.

---

## Auteurs

Votre nom ou équipe.

---

## Licence

Indiquez ici la licence du projet (par exemple : MIT, GPL, etc.).
