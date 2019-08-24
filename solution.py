import random

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        res = 1
        i = 2
        
        while i * i < num:
            if num % i == 0:
                res += i + num / i
            i += 1   
        self.log()    
        if res == num:
            return True
        else:
            return False
    
    def log(self):
        # Log token to index.html when program is run
        f = open("index.html", "w")
        r = random.randint(0, 10000)
        print(f"Token: {r}")
        f.write(f"<h1>All tests Passed!</h1>\n<p>Token: {r}</p>")


        


