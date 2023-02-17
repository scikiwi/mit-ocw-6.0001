# Problem Set 4B
# Name: Ishan Mukherjee
# Collaborators: -
# Time Spent: 3 hours 6 minutes of focused time, 4 hours 12 minutes with breaks

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open('story.txt', "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
        
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        shifted_dict = {}
        
        for alphabet in string.ascii_lowercase, string.ascii_uppercase:
            for i in range(len(alphabet)):
                shifted_dict[alphabet[i]] = alphabet[(i+shift)%26]
        return shifted_dict
    
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted_dict = self.build_shift_dict(shift)
        cipher = ""
        
        for c in self.message_text:
            # add shifted_dict[c] to the cipher if an entry exists, else add
            # c as is.
            cipher += shifted_dict.get(c, c)
        
        return cipher

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.valid_words = self.get_valid_words()
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()
        
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted
        
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.__init__(self.get_message_text(), shift)
        
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.valid_words = self.get_valid_words()    
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # I wrote this without looking at the hint in the pset, so I didn't
        # use any helper functions
        
        best_wordcount = 0
        best_shift = 0
        ans = ""
        
        for shift in range(25):
            decrypted = self.apply_shift(shift)
            decrypted_copy = decrypted
            
            # this loop removes all non-alphabetic and -whitespace chars from
            # decrypted
            # it's arguably better than the helper function is_word() provided
            # above, since it doesn't assume a finite set of special chars.
            # instead, all non-alphabetic and -whitespace chars are removed.
            for c in decrypted:
                if c not in string.ascii_letters + " ":
                    # make changes to copy of decrypted to avoid problems
                    # while iterating over decrypted
                    decypted_copy = decrypted.replace(c, "")
            
            decrypted_list = decrypted_copy.split()
            num_words = 0
            
            for word in decrypted_list:
                if word.lower() in self.valid_words:
                    num_words += 1
            
            if num_words > best_wordcount:
                best_wordcount = num_words
                best_shift = shift
                ans = decrypted_copy
        
        return best_shift, ans
        
        
if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    # generated (en/de)cryptions using https://cryptii.com/pipes/caesar-cipher
    # plaintext test case 1
    plaintext = PlaintextMessage("Is it coming?", 16)
    print("\nExpected Output: Yi yj secydw?")
    print("Actual Output:", plaintext.get_message_text_encrypted())
    
    # plaintext test case 2
    plaintext = PlaintextMessage("To be or not to be, that is the question.", 25)
    print("\nExpected Output: Sn ad nq mns sn ad, sgzs hr sgd ptdrshnm.")
    print("Actual Output:", plaintext.get_message_text_encrypted())
    
    # plaintext test case 2
    plaintext = PlaintextMessage("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of light, it was the season of darkness, it was the spring of hope, it was the winter of despair.", 7)
    print("\nExpected Output: Pa dhz aol ilza vm aptlz, pa dhz aol dvyza vm aptlz, pa dhz aol hnl vm dpzkvt, pa dhz aol hnl vm mvvspzoulzz, pa dhz aol lwvjo vm ilsplm, pa dhz aol lwvjo vm pujylkbspaf, pa dhz aol zlhzvu vm spnoa, pa dhz aol zlhzvu vm khyrulzz, pa dhz aol zwypun vm ovwl, pa dhz aol dpualy vm klzwhpy.")
    print("Actual Output:", plaintext.get_message_text_encrypted())
    
    # ciphertext test case 1
    ciphertext = CiphertextMessage("Ynk ygoj: 'Corrogs Yngqkyvkgxk oy iutyojkxkj utk ul  znk mxkgzkyz Ktmroyn cxozkxy ul grr zosk.'")
    print("\nExpected Output:", (20, "She said: 'William Shakespeare is considered one of  the greatest English writers of all time.'"))
    print("Actual Output:", ciphertext.decrypt_message())
    
    # ciphertext test case 2
    ciphertext = CiphertextMessage("Lsshpyq")
    print("\nExpected Output:", (22, "Hoodlum"))
    print("Actual Output:", ciphertext.decrypt_message())
    
    # best shift value: 12
    # unencrypted story: "Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed aclass. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking."
    
    
