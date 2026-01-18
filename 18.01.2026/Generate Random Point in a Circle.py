class Solution:
    def __init__(self, r, x, y):
        self.r=r; self.x=x; self.y=y
    def randPoint(self):
        import random,math
        a=random.random()*2*math.pi
        d=math.sqrt(random.random())*self.r
        return [self.x+d*math.cos(a),self.y+d*math.sin(a)]
