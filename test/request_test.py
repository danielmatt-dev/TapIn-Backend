import base64
import hashlib
import os
import urllib

import requests
from dotenv import load_dotenv

load_dotenv()

# Replace with your actual client ID and secret
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = "https://oauth.pstmn.io/v1/callback"
auth_url = "http://localhost:8000/o/authorize/"
token_url = "http://localhost:8000/o/token/"


# === FUNCIONES PKCE ===

def generate_code_verifier():
    return base64.urlsafe_b64encode(os.urandom(40)).decode('utf-8').rstrip('=')


def generate_code_challenge(verifier):
    digest = hashlib.sha256(verifier.encode('utf-8')).digest()
    return base64.urlsafe_b64encode(digest).decode('utf-8').rstrip('=')


# === PASO 1: Generar URL para login ===
def generar_url_authorization(code_challenge):
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
    }
    url = f"{auth_url}?{urllib.parse.urlencode(params)}"
    return url


# === PASO 2: Pedir Access Token ===
def pedir_access_token(authorization_code, code_verifier):
    data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret,  # Quita esta línea si tu servidor no requiere client_secret
        "code_verifier": code_verifier,
    }

    response = requests.post(token_url, data=data)

    if response.status_code == 200:
        token_data = response.json()
        print("\n✅ ACCESS TOKEN OBTENIDO:")
        print(token_data)
    else:
        print("\n❌ ERROR al pedir token:")
        print(f"Status Code: {response.status_code}")
        print(response.text)


# === MAIN ===
if __name__ == "__main__":
    print("\n🔵 Generando code_verifier y code_challenge (PKCE)...")
    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge(code_verifier)

    url = generar_url_authorization(code_challenge)

    print("\n🔵 Abre esta URL en tu navegador para iniciar sesión:")
    print(url)

    authorization_code = input("\nPega aquí el authorization_code que recibiste en el callback: ").strip()

    pedir_access_token(authorization_code, code_verifier)
