#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:16:45 2023

@author: finnkruger
"""

class CaesarCipher:
    def __init__(self, shift):
        # create arrays for encryption and decryption
        encrypt_arr = [None]*26
        decrypt_arr = [None]*26
        
        # populate arrays
        for i in range(26):
            encrypt_arr[i] = chr((i + shift) % 26 + ord('A'))
            decrypt_arr[i] = chr((i - shift) % 26 + ord('A'))
            
        # convert arrays to strings
        self._forward = ''.join(encrypt_arr)
        self._backward = ''.join(decrypt_arr)

    def transform(self, original, code):
        # convert message to list of characters
        msg = list(original)
        for i in range(len(msg)):
            # check if character is uppercase
            if msg[i].isupper():
                # convert character to index and replace with code
                j = ord(msg[i]) - ord('A')
                msg[i] = code[j]
        # convert list of characters back to string
        return ''.join(msg)
    
if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE S."
    
    # encrypt message
    coded = cipher.transform(message, cipher._forward)
    print("Secret:", coded)
    
    # decrypt message
    answer = cipher.transform(coded, cipher._backward)
    print("Message:", answer)