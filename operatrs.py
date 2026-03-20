def log_and(a,b):
    return a and b
print("p     q      p and q")
for p in [True,False]:
    for q in [True,False]:
        print(f"{p}  {q}  {log_and(p,q)}")
    

def log_or(a,b):
    return a or b
print("p     q      p or q")
for p in [True,False]:
    for q in [True,False]:
        print(f"{p}  {q}  {log_or(p,q)}")
        
def log_not(a):
    return not a
print("p     not p")
for p in [True,False]:
    print(f"{p}  {log_not(p)}")
    
def log_xor(a,b):
    return True if(a!=b) else False
print("p     q      p xor q")
for p in [True,False]:
    for q in [True,False]:
        print(f"{p}  {q}  {log_xor(p,q)}")
    
def log_biconditional(a,b):
    return False if(a!=b) else True
print("p     q      p fof q")
for p in [True,False]:
    for q in [True,False]:
        print(f"{p}  {q}  {log_biconditional(p,q)}")
    
def log_conditional(a,b):
    return False if(a==True and b== False) else True
print("p     q      p fof q")
for p in [True,False]:
    for q in [True,False]:
        print(f"{p}  {q}  {log_conditional(p,q)}")