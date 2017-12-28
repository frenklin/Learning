
# https://en.wikipedia.org/wiki/De_Bruijn_sequence
#
#
import numpy as np

class DeBrujin():    

    def __init__(self):
        self.sequence = None

    def buildSequence(self, n, k):   
        if k == 1:
            return ''.join(['0' for _ in range(n)])

        self.sequence = np.array([], dtype=np.int8)

        a = np.array([0] * k * n, dtype=np.int8)        

        def db(t, p):
            if t > n:
                if n % p == 0:
                    self.sequence = np.append(self.sequence, a[1:p + 1])
            else:
                a[t] = a[t - p]
                db(t + 1, p)
                for j in range(a[t - p] + 1, k):
                    a[t] = j
                    db(t + 1, t)
        db(1, 1)
        result = "".join(str(i) for i in self.sequence)
        result += result[:n-1]
        
        #print(result_len)
        #print(result)
        return result
    
  
s = DeBrujin()

assert(s.buildSequence(2,3) == '0010211220')
assert(s.buildSequence(2,2) == '00110')
assert(s.buildSequence(3,1) == '000')
assert(s.buildSequence(2,1) == '00')
assert(s.buildSequence(1,1) == '0')
assert(s.buildSequence(1,2) =='10' or s.buildSequence(1,2)== '01')

print(s.buildSequence(22,2))
