class Decrypt():
    def decrypt_caeser(key, crypto):
        key = int(key)
        result=""
        crypto = crypto.lower()
        for each in crypto:
            t = ord(each)-key
            if t < 97:
                result+=chr(t+26)
            else:
                result+=chr(t)
        return result
    def decrypt_monoalphabetic(key_row1,key_row2, crypto):
        key_dict = {}
        for i in range(0,26):
            key_dict[key_row2[i]] = key_row1[i]
            #key = key[0:-1]
        #print(key_dict)
        result=""
        for each in crypto:
            result+=key_dict[each]
        return result
    def decrypt_playfair(key, crypto):
        crypto = crypto.replace(" ","")
        class data():
            def __init__(self,c,r,v):
                self.col=c
                self.row=r
                self.value=v
            def __str__(self):
                return "test"
        table=[]
        text = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for each in key:
            text = text.replace(each,"")
        for i in range(0,5):
            for j in range(0,5):
                if key!="":
                    table.append(key[0].upper())
                    key = key[1:]
                else:
                    table.append(text[0])
                    text = text[1:]
        crypto = crypto.replace("J","I")
        if len(crypto)%2!=0:
            crypto+="X"
        c_list = []
        i=0
        while i<len(crypto):
            c_list.append(crypto[i:i+2])
            i+=2                
        result=""
        for each in c_list:
            index_0 = table.index(each[0])
            index_1 = table.index(each[1])
            if (index_0-index_1)%5==0:
                #same col
                index_0 = index_0-5
                if index_0<0:index_0=20
                index_1 = index_1-5
                if index_1<0:index_1=20
            elif abs(index_0-index_1)<5 and (index_0//5 ==index_1//5):
                #same row
                if index_0%5==0:
                    index_0=index_0+4
                else:
                    index_0=index_0-1
                if index_1%5==0:
                    index_1=index_1+4
                else:
                    index_1=index_1-1
            else:
                for i in range(0,5):
                    if index_0%5>index_1%5:
                        if (index_0-i-index_1)%5==0:
                            index_0-=i
                            index_1+=i
                    else:
                        if (index_1-i-index_0)%5==0:
                            index_0+=i
                            index_1-=i
            result+=table[index_0]+table[index_1]
        return result.lower()
    def decrypt_vernam(key,crypto):
        table="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        table=[table[i:i+1] for i in range(0,len(table),1)]
        #print(table)
        n_key = key
        result=""

        for i in range(len(crypto)):
            tmp=""
            t_1 = crypto[i]
            t_2 = key[i]
            t_3 = table.index(t_1)
            t_4 = table.index(t_2)
            tmp=table[(table.index(crypto[i])^table.index(key[i]))%26]
            result+=tmp
            key+=tmp
            #print("key:"+key)
            #print("result:"+result)
        return result.lower()
    def decrypt_row_transposiion(key,crypto):
        length = len(crypto)
        num = len(crypto)//len(key)
        pad = len(crypto)%len(key)
        table={}
        for i in range(1,len(key)+1):
            if i<=pad:   
                table[key[i-1]]=""
            else:
                table[key[i-1]]="0"
        if pad!=0:
            num+=1
        for i in range(1,len(key)+1):
            if table[str(i)]=="":
                table[str(i)]=crypto[0:3]
                crypto = crypto[3:]
            else:
                table[str(i)]=crypto[0:2]
                crypto = crypto[2:]
        count=0
        result=""
        while(count<length):
            index = count%len(key)
            result+=table[key[index]][0]
            table[key[index]] = table[key[index]][1:]
            count+=1
        return result.lower()
    def decrypt_product(key,crypto):
        result=""
        s_list = key.split(" ")
        l_list = {}
        length=len(s_list)
        for i in range(length):
            l_list[int(s_list[i])]=crypto[i]
        #print(l_list)
        for key, value in sorted(l_list.items()):
            #print(key,value)
            result+=value
        return result.lower()
if __name__=="__main__":
    #crypto_caeser = "RLLWNVPUNULCLYNPCLBW"
    #print("Caeser_plain_text:"+decrypt_caeser(7, crypto_caeser))

    #crypto_mono = "ATTHUGOFUFTCTKUOCTXH"
    #key_mono_row1 = "zyxwvutsrqponmlkjihgfedcba"
    #key_mono_row2 = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
    #print("Monoalphabetic:"+decrypt_monoalphabetic(key_mono_row1,key_mono_row2, crypto_mono))

    #crypto_playfair = "TCMWMKZLQMECMZLGNKSMALEZ"
    #print("Playfair:"+decrypt_playfair("HIT",crypto_playfair))

    crypto_vernam = "LPKMKDFFDNXFNFCASBGCL"
    print("Vernam:"+decrypt_vernam("MLB",crypto_vernam))

    #crypto_rowtrans = "EDNOOGHLRWDLGILONROOM"
    #print("Row transposition:"+decrypt_row_transposiion("31562487",crypto_rowtrans))

    #crypto_product = "GEUEIEIREPPVGOKGVENN"
    #key_product = "15 11 19 18 16 03 07 14 02 20 04 12 09 06 01 05 17 13 10 08"
    #print("Product:"+decrypt_product(key_product,crypto_product))
    

