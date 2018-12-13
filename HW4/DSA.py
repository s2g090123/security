import random,hashlib

def miller_rabin(N,validate_count):         
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

    for i in range(validate_count):           
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
    output = x
    for i in y[1:]:
        output = pow(output,2) % N
        if(i=='1'):
            output = output * x % N
    return output
def ext_GCD(a,b):
    if(b==0):
        return 1,0,a
    else:
        x,y,A = ext_GCD(b,a%b)
        return y,x-(a//b)*y,A

q = 1
while not(miller_rabin(q,128)):
    q = random.getrandbits(159) + (1<<159)
while(1):
    p=1
    while not(miller_rabin(p,128)):
        K = 1
        K = random.getrandbits(863) + (1<<863)
        p = K*q+1
        print(len(bin(p)[2:]))

    
    if(len(bin(p)[2:])==1024):
        break
#p = 113003610536769662365475438074349202902393371149098932488829763899759693942182221311951893491037065838678290591836787867236266829425427477322203921585701270997375076009060429934105831431797790713235693561718253840225010037389994367689434248899226231330475152082648849936270434981210830874017521600353881618277
#q = 1461461359677056032138425664688969714401096527653
h = random.randrange(2,p-1)
alpha = square_mul(h,bin(K)[2:],p)
#alpha = 96504423597250666602463350548382591669983630413397284533161601799828504875913402437338367980529992940898864793759282567968196860849581229764805627921115713088555922323634319263032762806965222542087676328725218634401760700374749451348066585982534624077588633442696948741889609514070233035695255374063221721717
d = random.randrange(1,q)
#d = 936678825459923885095535567029229102235556154286
beta = square_mul(alpha,bin(d)[2:],p)
#beta = 108995193903934240798564100451045627210748695124974357268916707208528553000170266840505861201457239168618690453605371832512801286701989019522907305372175334396049194915209672515965212302226018817730175446251842830527761730120646366217675171871247849970396570237026190763013764161366386690833417893072059869763

Ke = random.randrange(2,q)
r = square_mul(alpha,bin(Ke)[2:],p)%q

K_inverse,_,_ = ext_GCD(Ke,q)
K_inverse = K_inverse %q
input = 'myDSAbooo'
s = (K_inverse*(int(hashlib.sha1(input.encode('utf-8')).hexdigest(),16)+d*r)) %q


s_inverse,_,_ = ext_GCD(s,q)
w = s_inverse % q
u1 = w * int(hashlib.sha1(input.encode('utf-8')).hexdigest(),16) % q
u2 = w * r % q
v = (square_mul(alpha,bin(u1)[2:],p)*square_mul(beta,bin(u2)[2:],p))%p %q

if(v % q ==r):
    print('yes')
else:
    print('no')