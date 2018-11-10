import string
import sys
class Encrypt():
    def Caesar(key,text):
        answer=''
        text = text.upper()
        for i in text:
            if(ord('Z') - ord(i) < (key % 26)):
                answer += chr(ord('A') + (key % 26) - (ord('Z') - ord(i)) - 1)
            else:
                answer += chr(ord(i) + (key % 26))
        return answer

#key = input("input key: ")
#text = input("input text: ")
#print(Caesar(int(key),text))
#
#
    def Monoalphabetic(key1,key2,text):
        answer = ''
        text = text.upper()
        key1 = key1.upper()
        key2 = key2.upper()
        for i in text:
            id = key1.find(i)
            answer += key2[id]
        return answer

#key1 = input("input key first row: ")
#key2 = input("input key second row: ")
#text = input("input text: ")
#print(Monoalphabetic(key1,key2,text))
#
#
    def Playfair(key,text):
        answer = ''
        text.replace(" ","")
        key = key.upper()
        text = text.upper()
        table = []
        for i in key:
            if i == 'J':
                i = 'I'
            if i not in table:
                table.append(i)
        for i in string.ascii_uppercase:
            if i == 'J':
                i = 'I'
            if i not in table:
                table.append(i)
        for i in range(0,sys.maxsize,2):
            if(i==len(text)):
                break
            if i==len(text)-1:
                text+='X'
            elif text[i] == text[i+1]:
                text = text[:i+1]+'X'+text[i+1:]
            char1 = table.index(text[i])
            char2 = table.index(text[i+1])
            if(int(char1/5)==int(char2/5)): #判斷是否相同列
                if(char1%5==4):
                    answer += table[int(char1/5)*5]
                else:
                    answer += table[char1+1]
                if(char2%5==4):
                    answer += table[int(char2/5)*5]
                else:
                    answer += table[char2+1]
            elif(char1%5==char2%5):         #判斷是否相同行
                if(int(char1/5)==4):
                    answer += table[char1%5]
                else:
                    answer += table[char1+5]
                if(int(char2/5)==4):
                    answer += table[char2%5]
                else:
                    answer += table[char2+5]
            else:
                answer += table[int(char1/5)*5+(char2%5)]
                answer += table[int(char2/5)*5+(char1%5)]
            answer += " "
        return answer

#key = input("input key: ")
#text = input("input text: ")
#key = "HIT"
#text = "helloworldgoodmorning"
#print(Playfair(key,text))
#
#
    def Vernam(key,text):
        answer = ''
        text = text.upper()
        key = key.upper()+text[:-len(key)]

        for i in range(0,len(text)):
            text_number = string.ascii_uppercase.find(text[i])
            key_number = string.ascii_uppercase.find(key[i])
            answer_position = text_number ^ key_number
            answer+=string.ascii_uppercase[answer_position%26]
        return answer

#key = input("input key: ")
#key = "NBA"
#text = input("input text: ")
#text = "helloworldgoodmorning"
#print(Vernam(key,text))
#
#
    def Row(key,text):
        answer = ''
        text = text.upper()
        for i in range(1,len(key)+1):
            pos = key.find(str(i))
            for j in range(pos,len(text),len(key)):
                answer += text[j]
        return answer

#key = input("input key: ")
#key = "31562487"
#text = input("input text: ")
#text = "keepgoingnevergiveup"
#print(Row(key,text))


    def Product(key,transport,text):
        answer = ''
        text = text.upper()
        print(text)
        for i in transport:
            print(i)
            pos = key.index(i)
            answer += text[pos]
        return answer

#key = input("input key: ")
#key = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
#transport = input("input transport: ")
#transport = "15 11 19 18 16 3 7 14 2 20 4 12 9 6 1 5 17 13 10 8"
#text = input("input text: ")
#text = "helloworldgoodmorning"

#print(Product(key.split(),transport.split(),text))
