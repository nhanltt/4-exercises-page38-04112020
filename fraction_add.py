# gdc function
def gdc(m,n):
    while m % n != 0 :
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n


# Fraction class
# Implements: Addition and equality
# To do: mutiplication, division, subtraction and comparision operator (<,>)

class Fraction:
    def __init__(self, top, bottom):
        temp = gdc(top, bottom)
         #maintain fraction in lowest terms right from the start.
        self.num = top // temp
        self.den = bottom // temp

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def show(self):
        print(self.num,'/',self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gdc(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    # get the numerator of a fraction (exercise 1)
    def get_num(self):
        return self.num

    # get the denominator of a fraction (exercise 2)
    def get_den(self):
        return self.den

    # Implement the remaining simple arithmetic operators (__sub__, __mul__, and __truediv__). (exercise 3)
    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gdc(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gdc(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common = gdc(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    # 4. Implement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and __ne__) (exercise 4)
    def __gt__(self, other_fraction):
        temp = (self.den * other_fraction.den)/gdc(self.den, other_fraction.den)
        new_num1 = self.num * (temp/self.den)
        new_num2 = other_fraction.num * (temp/other_fraction.den)
        return new_num1 > new_num2  

    def __ge__(self, other_fraction):
        temp = (self.den * other_fraction.den)/gdc(self.den, other_fraction.den)
        new_num1 = self.num * (temp/self.den)
        new_num2 = other_fraction.num * (temp/other_fraction.den)
        return new_num1 >= new_num2 

    def __lt__(self, other_fraction):
        temp = (self.den * other_fraction.den)/gdc(self.den, other_fraction.den)
        new_num1 = self.num * (temp/self.den)
        new_num2 = other_fraction.num * (temp/other_fraction.den)
        return new_num1 < new_num2

    def __le__(self, other_fraction):
        temp = (self.den * other_fraction.den)/gdc(self.den, other_fraction.den)
        new_num1 = self.num * (temp/self.den)
        new_num2 = other_fraction.num * (temp/other_fraction.den)
        return new_num1 <= new_num2

    def __ne__(self, other_fraction):
        temp = (self.den * other_fraction.den)/gdc(self.den, other_fraction.den)
        new_num1 = self.num * (temp/self.den)
        new_num2 = other_fraction.num * (temp/other_fraction.den)
        return new_num1 != new_num2 

    
siglist = ['+', '-', '*', '/', '==', '!=', '>=', '<=', '>', '<']
ob_sig = ['x.get_num', 'x.get_den','y.get_num', 'y.get_den']

while True:

    input("Please enter two fractions (press any key to continue)")
    top1 = int(input("Numerator of first fraction: "))
    bot1 = int(input("Denominator of first fraction: "))
    top2 = int(input("Numerator of second fraction: "))
    bot2 = int(input("Denominator of second fraction: "))
    x = Fraction(top1, bot1)
    y = Fraction(top2, bot2)
    print('The first fraction (x) is ', end='')
    print(x)
    print('The second fraction (y) is ', end='')
    print(y)
    print('You can use these operator: ')
    print(siglist)
    print(ob_sig)
    while True:
        sig = input("Operator: ")
        if sig == 'exit': 
            break
        elif sig in siglist:
            command = "print(x " + sig + " y)"
            print(x,sig,y,'= ',end='')
            exec(command)
        elif sig in ob_sig:
            command = "print(" + sig + "())"
            print(sig + ' is ', end='')
            exec(command)
        else: 
            print("The operator is not define in this calculator.")
            print("Please enter correct operator")
    
    e_sig = input("Do you want to exit program? (enter 'exit'): ")
    if e_sig == 'exit':
        break
# Finish 4 exercises at p.38, 04 Nov 2020, by Nhan Thi Thanh Le    