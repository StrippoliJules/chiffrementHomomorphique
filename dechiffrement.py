import tenseal as ts
import json
import base64

def programme3_dechiffrement(context_prive_file='context_prive.json',
                             input_ciphertext='blocs2.json'):
    """
    Programme #3 : 
     - Charge le contexte privé (avec la secret_key)
     - Lit blocs2 (résultat chiffré)
     - Déchiffre et affiche Blocs3
    """
    # 1) Charger le contexte privé
    with open(context_prive_file, 'r') as f:
        serialized_prive_b64 = json.load(f)
    serialized_prive = base64.b64decode(serialized_prive_b64)
    context_prive = ts.context_from(serialized_prive)

    # 2) Charger le ciphertext blocs2
    with open(input_ciphertext, 'r') as f:
        ciphertext_b64 = json.load(f)
    ciphertext_bytes = base64.b64decode(ciphertext_b64)
    vecteur_chiffre = ts.ckks_vector_from(context_prive, ciphertext_bytes)

    # 3) Déchiffrer
    blocs3 = vecteur_chiffre.decrypt()
    print(f"[Programme#3] Résultat déchiffré (Blocs3) = {blocs3}")

    return blocs3

# --------------- BONUS : Comparaison avec Blocs4 ---------------
def calcul_en_clair(donnees):
    """ Reproduit la même transformation que Programme#2 => (x+5)*2 """
    return [(x + 5)*2 for x in donnees]

if __name__ == "__main__":
    # On suppose qu'on connaît la donnée initiale (Machine A la connaît)
    donnees_initiales = [10.5, 20.3, 30.7]

    # 1) Récupérer Blocs2 => Déchiffrer => Blocs3
    blocs3 = programme3_dechiffrement()

    # 2) Calculer en clair => Blocs4
    blocs4 = calcul_en_clair(donnees_initiales)
    print(f"[Programme#3] Résultat en clair (Blocs4) = {blocs4}")

    # 3) Comparer Blocs3 et Blocs4
    print("\n[Programme#3] Comparaison Blocs3 vs Blocs4 :")
    for i, (val3, val4) in enumerate(zip(blocs3, blocs4)):
        print(f"  - Elément {i}: Blocs3 = {val3:.6f}, Blocs4 = {val4:.6f} (Diff={abs(val3-val4):.6e})")
