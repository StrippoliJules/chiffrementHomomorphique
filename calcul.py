import tenseal as ts
import json
import base64

def programme2_calcul(context_public_file='context_public.json',
                      input_ciphertext='blocs1.json',
                      output_ciphertext='blocs2.json'):
    
    with open(context_public_file, 'r') as f:
        serialized_public_b64 = json.load(f)
    serialized_public = base64.b64decode(serialized_public_b64)
    context_public = ts.context_from(serialized_public)

    with open(input_ciphertext, 'r') as f:
        ciphertext_b64 = json.load(f)
    ciphertext_bytes = base64.b64decode(ciphertext_b64)
    vecteur_chiffre = ts.ckks_vector_from(context_public, ciphertext_bytes)

    vecteur_chiffre += 5
    vecteur_chiffre *= 2

    new_ciphertext_bytes = vecteur_chiffre.serialize()
    new_ciphertext_b64 = base64.b64encode(new_ciphertext_bytes).decode('utf-8')

    with open(output_ciphertext, 'w') as f:
        json.dump(new_ciphertext_b64, f)

    print(f"Nouveau ciphertext => {output_ciphertext}")

if __name__ == "__main__":
    programme2_calcul()
