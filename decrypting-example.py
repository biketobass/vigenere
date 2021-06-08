# Example of how to use the Vigenere Square to decrypt a message you've
# been given.

import vigenere as vig

# You and your friend both know the key phrase.
# Your friend gives you an encrypted message that you want to decrypt.

# Set the key phrase.
key = "Goats are cool."

# Now create a new Vigenere Square using that key phrase.
square = vig.VigenereSquare(key)

# Enter the encrypted message in quotes because it's a string.
encrypted_message = "SWSVZIVZQIGRTCMXKLVXVVSDNSEIGUK"

# Now decrypt the message using the square's decrypt method.
decrypted_message = square.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message)
