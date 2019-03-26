#coding:utf-8

from base64 import b64decode
import boto3

def decrypt_text_by_kms(encrypted_text):
    return boto3.client('kms').decrypt(CiphertextBlob=b64decode(encrypted_text))['Plaintext'].decode('utf-8')

