def encrypt(text,s):
  result=""

  for i in range(len(text)):
       char= text[i]

       if (char.isupper()):
        result += chr((ord(char) + s-65) % 26 +65)

       else:
        result += chr((ord(char) + s-97) % 26 +97)

  return result


text = input("Enter original text:")
s = int(input("shifts:"))
print("Encrypted text:" + encrypt(text,s))


def decrypt(cipher,s):
  result1 = "";

  for j in range(len(cipher)):
       char= cipher[j]

       if(char.isupper()):
        result1 += chr((ord(char) - s-65) % 26 +65)

       else:
        result1 += chr((ord(char) - s-97) % 26 +97)

  return result1

cipher = encrypt(text,s)
print("Decrypted text:" + decrypt(cipher,s))