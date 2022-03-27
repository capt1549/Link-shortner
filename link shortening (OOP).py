import random
import string


class Shortlink:                                                   # Defining a class

    def __init__(self):
        self.dict = dict()
        self.list = list()


# Function 1: Creating the shortlink.

    def getshortlink(self, longlink):
        l = random.randint(6, 10)                                   # This will generate random number from 6 to 10.
        chars = string.ascii_lowercase                              # This will generate aphabets in lowercase.
        shortlink = ""

        for i in range(l):
            b = random.choice(chars)                                # This will generate a random alphabet from "alpha" variable.
            shortlink = shortlink+b                                 # Concatenation of the alphabets.

        if shortlink in self.dict:
            return self.getshortlink()                              # If the shortlink already exists in d, then this will run the program again.
        else:
            self.dict[shortlink] = longlink
        r = "https://www.shortenedlink.com/"+shortlink              # "https://www.shortenedlink.com/ + (the random letters)" this is a link that will be generated after concatenation.
        return r

# Function 2: Accessing the longlink using shortlink which is stored in a dictionary as a key.

    def getlonglink(self, shortlink):                               # Here, a function is defined to acess the long link whose input will be the short link 
        k = shortlink[len(longlink):]                               # as the main objective is to concatenate the last letters whose length is from 6 to 10, only those letters should be concatenated.
        if k in self.dict:                                          # This will fetch the longlink whose shortlink is stored in a dictionary as a key.
            return self.dict[k]
        else:
            return None


s = Shortlink()                                                     # Creating the Object with reference of class "Shortlink".
longlink = "https://www.youtube.com/watch?v=SQT1jqW6_UA"            # This is a link that we have to convert into shortlink.
print(s.getshortlink(longlink))                                         