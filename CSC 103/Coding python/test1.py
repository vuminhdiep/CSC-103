r = ''
def binaryToDecimal(i): 
    
    dec_value = 0
      
    base = 1
      
    temp = i
    while(temp): 
        last_digit = temp % 10
        temp = int(temp / 10)
          
        dec_value += last_digit * base
        base = base * 2
    return dec_value
  
num = [1110010, 1100101, 1110100, 1110100, 1100101, 1101100, 1110010, 1100101, 1101000, 1110100, 1101111, 1111001, 1110010, 1100101, 1110110, 1100101, 1110011, 1110010, 1100001, 1110011, 1100101, 1100001, 1100011, 1110100, 1101110, 1100101, 1110010, 1100101, 1100110, 1100110, 1101001, 1100100, 1101111, 1110111, 1110100, 111010, 1010]

for i in num:
    character = chr(binaryToDecimal(i))
    r = r + character
print(reversed(r))
from ast import literal_eval  
test_string = ['0x67', '0x66', '0x72', '0x70', '0x72', '0x71', '0x6e', '0x70', '0x72', '0x79', '0x79', '0x6a', '0x6c', '0x65', '0x62', '0x6d', '0x71', '0x6f', '0x68', '0x6d', '0x67', '0x63', '0x6f', '0x77', '0x67', '0x66', '0x72', '0x6d', '0x71', '0x6d', '0x65', '0x63', '0x65', '0x6d', '0x62', '0x71', '0x72', '0x74', '0x72', '0x6a', '0x67', '0x72', "0x75", '0x79', '0x67', '0x67', '0x78', '0x6c', '0x62', '0x75', '0x62', '0x64', '0x73', '0x72', '0x75', '0x63', '0x67', '0x6d', '0x63', '0x6d', '0x73', '0x6b', '0x6c', '0x66', '0x72', '0x79', '0x71']
for i in test_string:
    res = literal_eval(i)
    letter = chr(res)
    r += letter
