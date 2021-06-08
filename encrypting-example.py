# Example of how to use the Vigenere Square to encrypt a message.

import vigenere as vig

# This assumes that you and your friend both know the key phrase. Perhaps you
# talked about it in person. Now you want to use that key phrase in the
# Vigenere Square to encrypt a message.

# Start by setting the key phrase as it's done here.
key = "Goats are cool."

# Now create a new Vigenere Square using that key phrase in the constructor.
square = vig.VigenereSquare(key)

# Type in the message to encrypt.
message = "Mischievous gnomes let the sheep out."

# Encrypt the message using your square's encrypt method.
encrypted_message = square.encrypt(message)
# Print out the encrypted message.
print("Encrypted message:", encrypted_message)
