def factorial(n):
	if n == 0: return 1
	return n*factorial(n-1)

#no overlapping subproblems

def fib(n):
    if n<=1: return 1
    return fib(n-1)+fib(n-2)
#fibonacci bottom-up
def fib2(n):
    n1,n2=1,1
    for i in range(n-1):
        print(i)
        res=n2
        n2=n2+n1
        n1=res
    return n2


#find max sum of a contiguous subarray of a list
def msum(a):
    return max([(sum(a[j:i]),(j,i)) for i in range (1,len(a)+1) for j in range (i)])

#find max sum of a contiguous subarray of a list
def msum2(a):
    bounds,s,t,j=(0,0),-float('infinity'),0,0
     
    for i in range (len(a)):
        t=t+a[i]
        if t>s:
            bounds=(j,i)
            s=t
        if t<0:
            j=i+1
            t=0
    print(bounds,s)
    
    
    def MaxVal(w,v,i,aW):
    global numCalls
    numCalls+=1
    if i==0:
        if w[i]<=aW: return v[i]
    else: return 0
    without_i=MaxVal(w, v, i-1, aW)
    if w[i]>aW:
        return without_i
    else:
        with_i=v[i]+MaxVal(w, v, i-1, aW-w[i])
    return max(without_i,with_i)
#takes a long time to run

def fastMaxval(w,v,i,aW,m):
    global numCalls
    numCalls+=1
    try: return m[(i,aW)]
    except KeyError:
        if i==0:
            if w[i]<=aW: 
                m[(i,aW)]=v[i]
                return v[i]
        else: 
            m[(i,aW)]=0
            return 0
        without_i=fastMaxval(w, v, i-1, aW,m)
        m[(i-1,aW)]=without_i
        if w[i]>aW:
            return without_i
        else:
            with_i=v[i]+fastMaxval(w, v, i-1, aW-w[i],m)
            res=max(without_i,with_i)
            m[(i,aW)]=res
        return res
        
            
        