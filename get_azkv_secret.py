#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import argparse
import os
import subprocess
from azure.identity import CertificateCredential
from azure.keyvault.secrets import SecretClient



usage="""
#===============================================#
#   ___     _                      ___          #
#  / _ \ __| |__  ___ _ _ _ _  ___| _ \_ _ ___  #
# | (_) (_-< '_ \/ _ \ '_| ' \/ -_)  _/ '_/ _ \ #
#  \___//__/_.__/\___/_| |_||_\___|_| |_| \___/ #
#-----------------------------------------------#
#      If you can't beat 'em, tech 'em!         #
#===============================================#
    COMMAND:
        get_azkv_secret.py v1.0 ( https://osbornepro.com/ )

    SYNTAX:
        get_azkv_secret.py [-h] -s -v -t -c -f

    DESCRIPTION:
        get_azkv_secret.py is a tool created to retrieve a Secret value from
        the Azure Key Vault using a Service Princial account and Certificate to
        authenticate

    USAGE:
        get_azkv_secret.py [-h] [-s SECRET]
                                [-v VAULTNAME] [-t TENANTID]
                                [-c CLIENTID] [-f FILE]

    OPTIONS:
        -h : Displays the help information for the command.
        -s : Define the Secret Name value from Azure
        -v : Define the name of the Azure Key Vault holding the secret
        -t : Define the Tenant ID the Azure Key Vault is in
        -c : Define the AppID/Client ID containing the ServicePrincipal the certificate is associated with
        -f : Define the path to the certificate file used for authentication
              NOTE: This is in Base64 formatted containing the public cert followed by its private key

    EXAMPLES:
        get_azkv_secret.py -s 'ITEmailPassword' -v 'KeyVaultSMTP' -t 'x0xxx10-00x0-0x01-0xxx-x0x0x01xx100' -c '084bbd99-f63a-4d21-87c2-9fa1815e48b7' -f '/etc/pki/tls/certs/azure-auth.pem'
        # This example gets the secret value stored in the KeyVaultSMTP vault, secret name ITEmailPassword for the specified Tenant using the SPN of the specified AppID/ClientID using the defined certificate file

"""

def ensure_venv():
    """Ensure the script is running inside a virtual environment."""
    if sys.prefix == sys.base_prefix:
        print("[!] Not running inside a virtual environment.")
        venv_path = os.path.join(os.path.dirname(__file__), ".venv")
        print(f"[*] Creating virtual environment at {venv_path} ...")
        subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
        print("[*] Installing dependencies...")
        subprocess.run([f"{venv_path}/bin/pip", "install", "-q",
                        "azure-identity>=1.10.0", "azure-keyvault-secrets>=4.6.0"], check=True)
        print("[+] Virtual environment setup complete.")
        print(f"[*] Re-run this script using: source {venv_path}/bin/activate && python {__file__}")
        sys.exit(0)


def get_secret(secret_name, vault_name, tenant_id, client_id, cert_path):
    """Retrieve secret value from Azure Key Vault."""
    kv_uri = f"https://{vault_name}.vault.azure.net"
    try:
        credential = CertificateCredential(tenant_id, client_id, cert_path, send_certificate_chain=True)
        client = SecretClient(vault_url=kv_uri, credential=credential)
        secret = client.get_secret(secret_name)
        return secret.value
    except Exception as e:
        print(f"[x] Error retrieving secret: {e}")
        sys.exit(1)


def main():
    ensure_venv()

    parser = argparse.ArgumentParser(description="Retrieve a secret value from the Azure Key Vault")
    parser.add_argument("-s", "--secret", required=True, help="Azure Secret Name to retrieve")
    parser.add_argument("-v", "--vaultname", required=True, help="Azure Key Vault Name")
    parser.add_argument("-t", "--tenantid", required=True, help="Azure Tenant ID")
    parser.add_argument("-c", "--clientid", required=True, help="Azure Client ID")
    parser.add_argument("-f", "--filepath", required=True, help="Path to certificate (Base64 PEM format)")
    args = parser.parse_args()

    secret_value = get_secret(args.secret, args.vaultname, args.tenantid, args.clientid, args.filepath)
    print(secret_value)


if __name__ == "__main__":
    main()
