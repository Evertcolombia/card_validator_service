import re


# Regex expressions for the principals card suppliers
suppliers = {
    "Visa": r'^4[0-9]{12}(?:[0-9]{3})?$',
    "Master card": r'^5[1-5][0-9]{14}$',
    "Master card coporate": r'^2[1-5][0-9]{14}',
    "American Express": r'^3[47][0-9]{13}$',
    "Maestro": r'^(5018|5020|5038|6304|6759|6761|6763|6935)[0-9]{8,15}$',
    "Dinners club": r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
    "Unionpay": r'^(62[0-9]{14,17})$',
    "Bc Global": r'^(6541|6556)[0-9]{12}$',
    "Carte Blanche": r'^389[0-9]{11}$',
    "Discover": r'^65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})$',
    "Insta payment": r'^63[7-9][0-9]{13}$',
    "Jcb": r'^(?:2131|1800|35\d{3})\d{11}$',
    "Korean local": r'^9[0-9]{15}$',
    "Laser": r'^(6304|6706|6709|6771)[0-9]{12,15}$',
    "Solo card": r'^(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}$',
    "Switch card": r'^(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{13}$',
}

def getSupplier(num):
    """" get the supplier for a card number
    
        Attributes:
        @num: card number
    """
    supplier = str()

    for key, value in suppliers.items():
        if bool(re.match(value, num)):
            supplier = key
            break
    if supplier == "":
        supplier = "Ukwnow"

    return supplier

def checkLuhn(num):
    """
    checkLuhn algorithm
    test if a number is valid for a credit or debit card number

    Attributes:
    @num: card number
    """
    len_num = len(num)
    num_sum = 0
    isSecond = False
     
    for i in range(len_num - 1, -1, -1):
        digit = int(num[i])
     
        if (isSecond == True):
            digit = digit * 2
  
        # manage case when a number is bigger than 9
        num_sum += (digit // 10) + (digit % 10)

        # iterate to know when multiple digit by 2
        isSecond = not isSecond
     
    if (num_sum % 10 == 0):
        return True
    else:
        return False