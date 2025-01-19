import tenseal as ts
import json
import base64

def programme1_chiffrement(donnees):
    context_prive = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[60, 40, 40, 60]
    )
    context_prive.global_scale = 2**40

    context_prive.generate_galois_keys()
    context_prive.generate_relin_keys()

    context_public = context_prive.copy()
    context_public.make_context_public()
    vecteur_chiffre = ts.ckks_vector(context_prive, donnees)

    serialized_prive = context_prive.serialize(
        save_secret_key=True,      
        save_public_key=True,
        save_galois_keys=True,
        save_relin_keys=True
    )
    serialized_public = context_public.serialize(
        save_public_key=True,
        save_galois_keys=True,
        save_relin_keys=True
    )
    serialized_ciphertext = vecteur_chiffre.serialize()
    serialized_prive_b64 = base64.b64encode(serialized_prive).decode('utf-8')
    serialized_public_b64 = base64.b64encode(serialized_public).decode('utf-8')
    serialized_ciphertext_b64 = base64.b64encode(serialized_ciphertext).decode('utf-8')

    with open('context_prive.json', 'w') as f:
        json.dump(serialized_prive_b64, f)
    with open('context_public.json', 'w') as f:
        json.dump(serialized_public_b64, f)
    with open('blocs1.json', 'w') as f:
        json.dump(serialized_ciphertext_b64, f)

    print("[Programme#1] context_prive.json")
    print("[Programme#1] context_public.json")
    print("[Programme#1] blocs1.json")

if __name__ == "__main__":
    donnees = [10.5, 20.3, 30.7]
    programme1_chiffrement(donnees)
