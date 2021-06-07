import pandas as pd
import re

class VigenereSquare :

    # Initialize a square with the keyword or phrase
    def __init__(self, key_phrase):
        self.key = self.clean_str(key_phrase)
        # The object needs to know the alphabet.
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        # The object will have a dictionary that holds the index position of
        # each letter of the alphabet but shifted over one. We're doing this
        # because the 0th row of the Vigenere Square is the alphabet shifted by one,
        # in other words b,c,d,...z,a. The next is c,d,e,...z,a,b. The last (or row
        # 25) is the alphabet in normal order. Having the dictionary, will enable
        # us to access each row by it's index.
        # Start with an empty dictionary.
        self.letter_index = {}
        # Shift the alphabet by 1.
        shifted = self.shift_list(self.alphabet)
        # Fill in the dictionary.
        for i in range(len(shifted)) :
            self.letter_index[shifted[i]] = i

        # It's time to make the square.
        # We're going to represent it as a pandas DataFrame with the columns
        # being the regular alphabet.
        self.vig_square = pd.DataFrame(columns = self.alphabet)
        # Each row is the alphabet from the previous row shifted over by one.
        # The 0th row is the normal alphabet shifted once.
        # So start with that.
        shifted_alphabet = self.shift_list(self.alphabet)
        for i in range(len(self.alphabet)) :
            # Set the current row to be the shifted alphabet.
            self.vig_square.loc[i] = shifted_alphabet
            # Shift again. Rinse and repeat
            shifted_alphabet = self.shift_list(shifted_alphabet)

    # Helper method to shift a list or in this case an alphabet by one.
    def shift_list(self, a_list) :
        copy = a_list.copy()
        front = copy.pop(0)
        copy.append(front)
        return copy

    # We need two more helper methods.

    # Helper method that makes a string lowercase and removes all spaces.
    # Ideally, this would remove all non-alphabetical characters.
    # I should really change this to use regular expressions. That's on
    # the to do list.
    def clean_str(self, str_to_clean) :
        # Make sure the message is lower case
        clean_str = str_to_clean.lower()
        # Get rid of any spaces, and non-alphabetical letters.
        clean_str = re.sub('[^a-z]', "", clean_str)
        return clean_str

    # Another helper method that repeats the key letter by letter
    # until it's the same length as the message.
    def fill_out_key(self, message) :
        long_key = ""
        for i in range(len(message)) :
            long_key += self.key[i%len(self.key)]
            i += 1

        return long_key



    # Now that the initialization and helper methods are done, we can write the
    # encryption and decryption methods.

    def encrypt(self, message) :
        # Make sure the message is lowercase and free of spaces, and
        # non-alphabetical characters.
        clean_message = self.clean_str(message)

        # Repeat the keyword over the length of the message
        long_key = self.fill_out_key(clean_message)

        # Now actually do the encrypting
        enc = ""
        for i in range(len(clean_message)) :
            # Get the letter from the message and the letter
            # from the key phrase that corresponds to it.
            letter = clean_message[i]
            key_letter = long_key[i]
            # Look up what the ciphertext should be
            # Get the index of the key_letter
            key_index = self.letter_index[key_letter]
            # Get the cipher text from the square. The row is the key_index.
            # The column name is the letter from the original message.
            cipher_letter = self.vig_square.loc[key_index, letter]
            enc += cipher_letter

        # And return the cipher text as all caps because that's convention.
        return enc.upper()


    # Take an encrypted message and decrypt it.
    def decrypt(self, enc_message) :
        clean_enc_message = self.clean_str(enc_message)
        long_key = self.fill_out_key(clean_enc_message)
        # Let's do some decrypting.
        decrypted = ""
        for i in range(len(clean_enc_message)) :
            # Get the current encrypted letter.
            cipher_letter = clean_enc_message[i]
            # Key letter from the key phrase that corresponds to it.
            key_letter = long_key[i]
            # Get it's index in the square.
            key_index = self.letter_index[key_letter]
            # Find the particular shifted alphabet that was used to encrypt the letter.
            # It's at the row index by key_index
            shifted_alpha = self.vig_square.loc[key_index]
            # shifted_alpha is a pandas series with an index that is the plaintext
            # alphabet and the context being the shifted alphabet.
            # Finally, find out the original letter. It's the index of the
            # encrypted letter.
            decrypted += shifted_alpha[shifted_alpha == cipher_letter].index[0]

        return decrypted

    # We might want to be able to change the key phrase.
    def set_key_phrase(self, key_phase) :
        self.key = self.clean_str(key_phrase)

    # We might also want to be able to retrieve the key phrase
    def get_key_phrase(self) :
        return self.key
