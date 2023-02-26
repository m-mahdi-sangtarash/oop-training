class bigname:
    def __init__(self, lname, name, nl, nl1):
        self.lname = lname
        self.name = name
        self.nl = nl
        self.nl1 = nl1
        
    def printbn(self):
        for name in nlist:
            nl = len(name)
            if nl > nl1:
                nl1 = nl
                self.lname = name
            else:
                continue
            
        print('big name:', self.lname)


nl1 = 0
nlist = []
i = 1
while i <= 5:
    name = input('please enter a name:')
    nlist.append(name)
    i=i+1

p1 = bigname(lname, name, nl, nl1)
p1.printbn()
