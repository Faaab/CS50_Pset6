import cs50
import sys

# prompt user for credit card number
while True:
    ccNum = cs50.get_int("Number: ")
    if ccNum > 0:
        break

# first check: length and starting numbers
ccString = str(ccNum)
ccLen = len(ccString)

# for American Express: starts with 34 or 37, has 15-digits
if ccString[0] == "3" and (ccString[1] == "4" or ccString[1] == "7") and ccLen == 15:
    company = "AMEX"
# for MasterCard: starts with 51-55, has 16 digits
elif ccString[0] == "5" and (ccString[1] >= "1" and ccString[1] <= "5") and ccLen == 16:
    company = "MASTERCARD"
# for Visa: starts with 4, has 13 or 16 digits
elif ccString[0] == "4" and (ccLen == 13 or ccLen == 16):
    company = "VISA"
else:
    print("INVALID")
    sys.exit()

# step 0: Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products' digits together.
checknum = 0

for i in range(ccLen - 2, -1, -2):
    n = int(ccString[i]) * 2
    if n >= 10:
        checknum += n % 10
        checknum += n // 10
    else:
        checknum += n

# step 1: Add the sum to the sum of the digits that weren’t multiplied by 2.
for i in range(ccLen - 1, -1, -2):
    checknum += int(ccString[i])

# step 2: If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
if checknum % 10 == 0:
    print(company)
else:
    print("INVALID")
