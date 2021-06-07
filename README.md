# vigenere
This is code implements a Vigenere cipher. I wrote the code so that my daughter could exchange encrypted messages with a couple of her friends. It's based on the description of a Vigenere Square as descibed by Simon Singh in *The Code Book*.

The repository includes the following files:
** `vigenere.py` which defines a VigenereSquare class.
** `example.py` which gives an example of how to use a VigenereSquare object to encrypt and decrypt messages.
** `__init__.py` which is an empty file that simply tells python to look in the current directory when you `import vigenere`.
In order to run the code you will need all of the files.

You will also need to have pandas installed because `vigenere.py` imports it and uses a pandas DataFrame to store the square. If you don't have pandas installed, running `pip install pandas` should take care of it.

As outlined in `example.py`, to encrypt and decrypt a message, first define a key phrase string. Then instantiate a VigenereSquare object passing that key phrase into the contructor. The square has both `encrypt` and `decrypt` methods that you can run on either a plaintext message or a ciphertext method respectively.
