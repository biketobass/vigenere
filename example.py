# Example of how to use the Vigenere Square.

import vigenere as vig

# You and your friend both know the key phrase and you want to
# encrypt a message. Start by setting the key phrase as it is set here.
key = "Goats are cool."

# Now create a new Vigenere Square using that key phrase.
square = vig.VigenereSquare(key)

# Type in the message to encrypt.
message = "Mischievous gnomes let the sheep out."
# Print it out if you like.
print("Original message:", message)

# Encrypt the message using your square's encrypt method.
encrypted_message = square.encrypt(message)
# Print out the encrypted message.
print("Encrypted message:", encrypted_message)

# Your friend will want to decrypt the message. They will
# enter the key phrase as you did above and then
# decrypt the message using the square's decrypt method.
decrypted_message = square.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message)
