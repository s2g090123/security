import random,hashlib

def miller_rabin(N,validate_count):
    '''
        透過miller_rabin來判定N是否為質數
        而驗證的次數為validate_count次
    '''
    if (N<2):
        return False
    if(N==3 or N==2):
        return True
    if(N%2==0):
        return False
    u,x = 1,N-1
    r = x
    while x % pow(2,u) != 0:     
        r = x / pow(2,u)
        u+=1

    for _ in range(validate_count):           
        candidate = random.randrange(2,N-1)   
        b = pow(candidate,r,N)                
        if(b==1 or b==N-1):
            continue
        for j in range(u-1):                  
            b = pow(b,2,N)                    
            if(b==N-1):
                break
            elif(b==1):
                return False
        else:                                
            return False
    return True
def square_mul(x,y,N):#x^y
    '''
        透過square_mul來加速 x^y mod N的速度
    '''
    output = x
    for i in y[1:]:
        output = pow(output,2) % N
        if(i=='1'):
            output = output * x % N
    return output
def ext_GCD(a,b):
    '''
        透過ext_GCD找出a在b下的乘法反元素
    '''
    if(b==0):
        return 1,0,a
    else:
        x,y,A = ext_GCD(b,a%b)
        return y,x-(a//b)*y,A

input = input('Please input message： ')
q = 1
while not(miller_rabin(q,256)):
    #先透過random的方式找出160bit的q
    q = random.getrandbits(159) + (1<<159)
while(1):
    p=1
    while not(miller_rabin(p,256)):
        '''
            再來先找出乘數K使得 p = K*q+1
            再透過miller_rabin判斷q是否可能為質數，若不是再重新找K
        '''
        K = 1
        K = random.getrandbits(863) + (1<<863)
        p = K*q+1

    
    if(len(bin(p)[2:])==1024):
        break

h = random.randrange(2,p-1)
alpha = square_mul(h,bin(K)[2:],p)
d = random.randrange(1,q)
beta = square_mul(alpha,bin(d)[2:],p)

#以下為簽署的過程
Ke = random.randrange(2,q)
r = square_mul(alpha,bin(Ke)[2:],p)%q

K_inverse,_,_ = ext_GCD(Ke,q)
K_inverse = K_inverse %q
s = (K_inverse*(int(hashlib.sha1(input.encode('utf-8')).hexdigest(),16)+d*r)) %q

#以下為驗證的過程
s_inverse,_,_ = ext_GCD(s,q)
w = s_inverse % q
u1 = w * int(hashlib.sha1(input.encode('utf-8')).hexdigest(),16) % q
u2 = w * r % q
v = (square_mul(alpha,bin(u1)[2:],p)*square_mul(beta,bin(u2)[2:],p))%p %q

if(v % q ==r):
    print('the result is yes')
else:
    print('the result is no')