l=[20,34,45,70,56,81,104,37,46,39]
h=[None]*11
for key in l:
    index=key%11
    h2=8-(key%8) 
    if h[index]is None:
       h[index]=key
    else: 
        for i in range(len(l)):
            hk=(index+(i*h2))%11
            if h[hk] is None: 
               h[hk]=key
               break
print(h) 
print(len(l))   

