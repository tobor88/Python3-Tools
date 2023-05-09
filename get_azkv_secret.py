#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------------------------------
# Below are the steps I suggest carrying out in order to set this up and utilzie this command
#mkdir -P /root/scripts/.virtual
#cd /root/scripts/.virtual
#python3 -m venv get_azkv_secret
#source /root/scripts/.virtual/get_azkv_secret/bin/activate
#echo argparse >> /root/scripts/.virtual/requirements.txt
#echo azure-common==1.1.28 >> /root/scripts/.virtual/requirements.txt
#echo azure-identity==1.10.0 >> /root/scripts/.virtual/requirements.txt
#echo azure-core==1.24.2 >> /root/scripts/.virtual/requirements.txt
#echo azure-keyvault==1.1.0 >> /root/scripts/.virtual/requirements.txt
#echo azure-keyvault-certificates==4.6.0 >> /root/scripts/.virtual/requirements.txt
#echo azure-keyvault-keys==4.7.0 >> /root/scripts/.virtual/requirements.txt
#echo azure-keyvault-secrets==4.6.0 >> /root/scripts/.virtual/requirements.txt
#echo azure-mgmt-compute==27.2.0 >> /root/scripts/.virtual/requirements.txt
#echo azure-mgmt-core==1.3.2 >> /root/scripts/.virtual/requirements.txt
#echo azure-mgmt-resource==21.1.0 >> /root/scripts/.virtual/requirements.txt
#echo azure-mgmt-storage==20.0.0 >> /root/scripts/.virtual/requirements.txt
#echo azure-storage-blob==12.13.1 >> /root/scripts/.virtual/requirements.txt
#pip3 install -r /root/scripts/.virtual/requirements.txt
#find /root/scripts/.virtual -type d -exec umask 077 {} \;
#chmod o-rwx -R /root/scripts/.virtual
#chmod g-rwx -R /root/scripts/.virtual
#---------------------------------------------------------------------------------------------------
import sys
import argparse
from azure.keyvault import KeyVaultClient
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

argumentList = sys.argv[1:]
options = "svtcf:"
long_options = ["secret","vaultname","tenantid","clientid","filepath"]
parser = argparse.ArgumentParser(description="Retrieve a secret value from the Azure Key Vault")
parser.add_argument("-s", "--secret", help = "Enter the Azure Secret Name you wish to retrieve the value of", required=True)
parser.add_argument("-v", "--vaultname", help = "Enter the Azure Key Vault Name containing the secret you wish to retrieve the value of", required=True)
parser.add_argument("-t", "--tenantid", help = "Enter the Azure Tenant ID the secret is in", required=True)
parser.add_argument("-c", "--clientid", help = "Enter the Azure Client ID for the SPN", required=True)
parser.add_argument("-f", "--filepath", help = "Enter the path to the certificate file used for authentication (It needs Base64 formatting with public cert followed by the private key)", required=True)
args = parser.parse_args()
KVUri = str("https://{}.vault.azure.net".format(args.vaultname))
credential = CertificateCredential(
        args.tenantid, args.clientid, args.filepath, send_certificate_chain=True
)


# Connecting to Azure Key Vault
client = KeyVaultClient(credential)
client = SecretClient(vault_url=KVUri, credential=credential)


# Retrieving secret
try:
        retrieved_secret = client.get_secret(args.secret)
        print(retrieved_secret.value)
except:
        print("[x] Unable to retrieve Secret Name {} from Key Vault {} in the specified Azure Tenant".format(args.secret, args.vaultname))
        sys.exit(1)
