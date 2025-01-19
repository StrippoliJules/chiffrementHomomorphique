Prérequis
Python 3.8+ installé
TenSEAL installé :
bash
Copier
pip install tenseal
Fichiers
programme1_chiffrement.py

Chiffre les données et produit :
context_prive.json
context_public.json
blocs1.json
calcul.py

Lit context_public.json et blocs1.json,
Exécute un calcul homomorphique,
Produit blocs2.json
dechiffrement.py

Lit context_prive.json et blocs2.json,
Déchiffre et affiche le résultat en clair.
Utilisation
Sur la machine qui chiffre

bash
Copier
python chiffrement.py
Génère context_prive.json, context_public.json, blocs1.json.
Envoyer context_public.json + blocs1.json à la machine qui fait le calcul (Machine B).

Sur la machine qui calcule (Machine B)

bash
Copier
python calcul.py
Produit blocs2.json.
Renvoyer blocs2.json à Machine A.

Sur la machine qui déchiffre (Machine A)

bash
Copier
python dechiffrement.py
Affiche les résultats en clair.
