import math

def encode(n, alphabet):
  encoded = ""
  while n > 0:
    i = n % len(alphabet)
    encoded = alphabet[i] + encoded
    n = n // len(alphabet)
  return encoded[::-1] # Reverse because test cases reversed...

alpha = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
print(encode(15674, alpha))
print(encode(7026425611433322325, alpha))
print(encode(187621, alpha))
print(encode(237860461, alpha))
print(encode(2187521, alpha))
print(encode(18752, alpha))


  
