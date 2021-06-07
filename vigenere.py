import pandas as pd

# You guessed it. This is the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Helper method to shift a list or in this case an alphabet by one.
def shift_list(a_list) :
    copy = a_list.copy()
    front = copy.pop(0)
    copy.append(front)
    return copy


# Next up create a dictionary that has the index position of each letter of the alphabet
# but shifted over one.
letter_index = {}
shifted = shift_list(alphabet)
for i in range(len(shifted)) :
    letter_index[shifted[i]] = i


# Create Vigenere Square
vig_square = pd.DataFrame(columns = alphabet)
shifted_alphabet = shift_list(alphabet)
for i in range(len(alphabet)) :
    vig_square.loc[i] = shifted_alphabet
    shifted_alphabet = shift_list(shifted_alphabet)

# With that done we can write the encryption and decryption methods

def encrypt(message, key) :
    # Make sure the message and key are lower case
    # and remove any spaces
    lc_message = clean_str(message)
    lc_key = clean_str(key)

    # Repeat the keyword over the length of the message
    long_key = fill_out_key(lc_message, lc_key)

    # Now actually do the encrypting
    enc = ""
    for i in range(len(lc_message)) :
        letter = lc_message[i]
        key_letter = long_key[i]
        # Look up what the ciphertext should be
        # Get the index of the key_letter
        key_index = letter_index[key_letter]
        cipher_letter = vig_square.loc[key_index, letter]
        enc += cipher_letter

    return enc.upper()

# Helper method that makes a string lowercase and removes all spaces.
# Ideally, this would remove all non-alphabetical characters.
# I should really change this to use regular expressions. That's on
# the to do list.
def clean_str(message) :
    # Make sure the message is lower case
    lc_message = message.lower()
    # Get rid of any spaces in both
    lc_message = lc_message.replace(" ", "")
    lc_message = lc_message.replace(".", "")
    lc_message = lc_message.replace(",", "")
    lc_message = lc_message.replace("?", "")
    lc_message = lc_message.replace("!", "")
    lc_message = lc_message.replace("'", "")
    lc_message = lc_message.replace('"', "")
    lc_message = lc_message.replace("-", "")

    return lc_message

# Another helper method
def fill_out_key(message, key) :
    long_key = ""
    i = 0
    for letter in message :
        long_key += key[i%len(key)]
        i += 1

    return long_key

def decrypt(enc_message, key) :
    lc_enc_message = clean_str(enc_message)
    lc_key = clean_str(key)
    long_key = fill_out_key(lc_enc_message, lc_key)
    decrypted = ""
    for i in range(len(lc_enc_message)) :
        cipher_letter = lc_enc_message[i]
        key_letter = long_key[i]
        key_index = letter_index[key_letter]
        shifted_alpha = vig_square.loc[key_index]
        decrypted += shifted_alpha[shifted_alpha == cipher_letter].index[0]

    return decrypted


def main() :
    message = "This is a test to try out this Vigenere Square method of encryption. I'm glad it works. Aren't you?"
    key = "unoriginal key phrase"
    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)
    print("Original message: ", message)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)

main()
