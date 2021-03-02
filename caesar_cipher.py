def shift_num(x, y, z, shift):
  return (x - y + shift) % (z-y+1) + y

def caesar_cipher(source = str, shift = str) -> str:
  r = str()
  for i in range(len(source)):
    c = ord(source[i])
    if 65 <= c <= 90: r += chr(shift_num(c, 65, 90, shift))
    elif 97 <= c <= 122: r += chr(shift_num(c, 97, 122, shift))
    else: r += source[i]

  return r

print(caesar_cipher("Hello World!", 1))