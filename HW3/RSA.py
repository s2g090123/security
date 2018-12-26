from fractions import gcd
import random #123


def miller_rabin(N,validate_count):         # watch https://www.youtube.com/watch?v=qdylJqXCDGs
    if (N<2):
        return False
    if(N==3 or N==2):
        return True
    if(N%2==0):
        return False
    u,x = 1,N-1
    r = x
    while x % pow(2,u) != 0:    # (N-1) mod (2^u) != 0 
        r = x / pow(2,u)
        u+=1

    for i in range(validate_count):           # validate_count means I can't check the N is a prime ,but I can through many validations ,and validate it is probably a prime
        candidate = random.randrange(2,N-1)   # candidate is 1 < candidate < N-1
        b = pow(candidate,r,N)                # in the first validate if b = 1 or -1 that b is probably a prime
        if(b==1 or b==N-1):
            continue
        for j in range(u-1):                  # in the next validate, I check b^2 mod N
            b = pow(b,2,N)                    # if b is -1 that b is probably a prime,but if b is 1 that b is not a prime
            if(b==N-1):
                break
            elif(b==1):
                return False
        else:                                # if I can check whether it is probably a prime, that it is not a prime
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
def CRT(D,P1,P2,Cipher):                    # x^y mod N can split to x^y mod p and x^y mod q  *N is p*q
    Dp = D % (P1-1)                         # 化簡次方項 *PHI(P) = P-1 if P is a prime, ex: 15^2987 mod 37
    Dq = D % (P2-1)                         # PHI(37) = 37-1 = 36, 15^(36*82+35) mod 37,through Fermat a^(P-1) mod P = 1, so it = 15^35 mod 37
    (Xq,_,_) = ext_GCD(P2,P1)               # Mi is 對方 , Yi is Mi inverse , Ai自己
    (Xp,_,_) = ext_GCD(P1,P2)               # watch https://www.youtube.com/watch?v=6ytuvahX1tQ
    return (Xq*P2*(square_mul(Cipher,bin(Dp)[2:],P1))+(Xp*P1)*(square_mul(Cipher,bin(Dq)[2:],P2))) % (P1*P2)
def RSA_GO(P1,P2,text):
    N = P1*P2
    PHI = (P1-1)*(P2-1)
    for i in range(2,PHI):
        if(gcd(i,PHI)==1):
            e = i
            break
    (d,_,_) = ext_GCD(e,PHI)

    cipher = square_mul(text,bin(e)[2:],N)
    Decipher = square_mul(cipher,bin(d % PHI)[2:],N)
    CRT_Decipher = CRT(d % PHI,P1,P2,cipher)
    return cipher,Decipher,CRT_Decipher

plaintext = input("Please input plaintext： ")
#P1 = input("Please input Prime1： ")
#P2 = input("Please input Prime2： ")
while(1):
    P1 = 1
    while not(miller_rabin(P1,512)):
        P1 = random.getrandbits(1024)
    P2 = 1
    while not(miller_rabin(P2,512)):
        P2 = random.getrandbits(1024)
    if(P1*P2>=int(plaintext)and P1!=P2 and P1*P2>=1.340781e+154):  #1.340781e+154 is 2^512 , so N is > 1024 bits    1.797693134862315907729305190785e+308
        break
E,D,CRT_D = RSA_GO(int(P1),int(P2),int(plaintext))



print("Cipher is",E)
print("DeCipher is",D)
print("CRT DeCipher is",CRT_D)