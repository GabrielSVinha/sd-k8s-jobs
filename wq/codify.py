#!/usr/bin/env python

import base64

class Encoder:
  """
  Simple encoder/decoder with passed key
  """
  def encode(self, key, value):
    """Return decoded value with the given key"""
    enc = []
    for i in range(len(value)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(value[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))
 
  def decode(self, key, value):
    """Return decoded value with the given key"""
    dec = []
    value = base64.urlsafe_b64decode(value)
    for i in range(len(value)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(value[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
