
import requests
import pprint

def transferAmount(name:str, city:str):
    response = requests.get('https://jsonmock.hackerrank.com/api/transactions').json()    
    totalpages = response['total_pages']
    creditamount = 0.0
    debitamount = 0.0
    for page in range(1,1+totalpages,1):
        response = requests.get(f'https://jsonmock.hackerrank.com/api/transactions?page={page}').json()
        # print(page)
        for entry in response['data']:
            if entry['userName']==name and entry['location']['city']==city:
                if entry['txnType']=='debit':
                    debitamount = max(debitamount,float(entry['amount'][1:].replace(',','')))
                else:
                    creditamount = max(creditamount,float(entry['amount'][1:].replace(',','')))
    return ["${:,.2f}".format(creditamount),"${:,.2f}".format(debitamount)]
    print("${:,.2f}".format(creditamount))
    print("${:,.2f}".format(debitamount))
    
transferAmount('Bob Martin','Bourg');