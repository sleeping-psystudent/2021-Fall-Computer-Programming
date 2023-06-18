class Fraction:
    def __init__(self, *args):
        self.Num = args[0]
        self.Den = args[1]
        self.a = args[0]
        self.b = args[1]
        
    def gcd(self, *args):
        if self.Den == 0:
            return self.Num
        elif self.Num < self.Den:
            a = self.Num
            self.Num = self.Den
            self.Den = a
            return self.gcd(self)
        else:
            a = self.Den
            self.Den = self.Num % self.Den
            self.Num = a
            return self.gcd(self)
    def findroot(self):
        gcd = self.gcd()
        m = int(self.a/gcd)
        n = int(self.b/gcd)
        res = ""
        mc, nc = 1, 1
        ml, nl = 0, 1
        mr, nr = 1, 0
            
        while mc !=m or nc != n:
            if m * nc > n * mc:
                ml, nl = mc, nc
                res += "R"
            else:
                mr, nr = mc, nc
                res += "L"
            mc, nc = ml + mr, nl + nr
        return res        
        
    def __str__(self):       
        return self.findroot()

    pass

def solution(A):
    result = Fraction(A[0], A[1]).findroot()
    return result
  
if __name__ == "__main__":
    start = time.time()
    q = [int(i) for i in input().split(' ')]
    print(solution(q))
    
"""
5 7
LRRL
"""
