import random
import string

class Url:

    def __init__(self):

        self.urlMapping = {}

    def uniqueCode(self):

        all = string.ascii_letters + string.digits
        length = len(all)
        code = ""
        for i in range(10):
            code += all[random.randint(0,length-1)]
        
        return code




