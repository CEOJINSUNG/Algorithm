class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        if num >= 1000:
            take = num//1000
            output += take*"M"
            num -= take*1000
        if num >= 900:
            output += "CM"
            num -= 900
        if num >= 500:
            take = num//500
            output += take*"D"
            num -= take*500
        if num >= 400:
            output += "CD"
            num -= 400
        if num >= 100:    
            take = num//100
            output += take*"C"
            num -= take*100
        if num >= 90:    
            output += "XC"
            num -= 90
        if num >= 50:
            take = num//50
            output += take*"L"
            num -= take*50
        if num >= 40:
            output += "XL"
            num -= 40
        if num >= 10:
            take = num//10
            output += take*"X"
            num -= take*10
        if num == 9:
            output += "IX"
            num -= 9
        if num >= 5:
            take = num//5
            output += take*"V"
            num -= take*5
        if num == 4:
            output += "IV"
            num -= 4
        if num > 0:
            output += num*"I"
        return output