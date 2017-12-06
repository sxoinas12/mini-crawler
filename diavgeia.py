
# -*- coding: utf-8 -*-

import re
import urllib.request
import urllib.error

arxes = {}

def rss_feed(url): #*
    '''
    Άνοιγμα του rss feed,
    :param url: η διεύθυνση του rss feed.
    Αυτή η συνάρτηση δημιουργεί ένα αρχείο
    με τα περιεχόμενα του rss_feed με όνομα
    την διεύθυνση του rss feed.
    Καλεί την συνάρτηση process_feed
    η οποία επιλέγει και τυπώνει περιεχόμενο
    Προσπαθήστε να κάνετε try/except τα exceptions
    HTTPError και URLError.
    '''
    url += r"/rss" 
    req = urllib.request.Request(url)
    
    try:
        with urllib.request.urlopen(req) as response:
            char_set = response.headers.get_content_charset()
            rss = response.read().decode(char_set)
            filename = "temp.rss"
            with open(filename,"w",encoding = "utf-8") as p:
                p.write(rss)
    except urllib.error.HTTPError as e:
        print("HTTP error",e.code)
        return 0
    except urllib.error.URLError as e:
        print("cant connect to the server")
        print("Reason:",e.reason)
        return 0
    else:
        if(process_feed(filename)):
            return 1
        else:
            return 0
    
    #σύμφωνα με την ανακοίνωση της διαύγειας τα rss feeds είναι στο ίδιο url/rss
    
    pass

def process_feed(filename): # *
    '''
    συνάρτηση που ανοίγει το αρχείο με το rss feed και 
    τυπώνει την ημερομηνία και τους τίτλους των αναρτήσεων που περιέχει.
    Xρησιμοποιήστε regular expressions 
    '''
    #
    print("process feed",filename)
    with open(filename,'r',encoding = 'utf-8') as f:
        rss = f.read().replace("\n", " ")
        date = re.findall(r"<lastBuildDate>(.*?)</lastBuildDate>",rss)
        new_date = process_date(date)
        print('\n')
        print("Ημερομηνια:",new_date)
        print('\n')
        items = re.findall(r"<item>(.*?)</item>",rss)
        string = ''.join(items)
        
        title_items = re.findall(r"<title>(.*?)</title>",string)
        
        print('+++++ Διαύγεια RSS '+ result[epilogh-1] )
        print('\n')
        for r in title_items:
            print(title_items.index(r)+1,r)
        
 #   pass 



def search_arxes(arxh):
    
    '''
    Αναζήτηση ονόματος Αρχής που ταιριάζει στα κριτήρια του χρήστη
    '''       
    pattern = '.*'+arxh+'.*'
    i = 0
    m = 0
    empty = []
    dictlist = []
    res = []
    new = {}
    for key , value in arxes.items():
        w = re.findall(pattern,str(key),re.I)
        if w == empty:
            continue
        else:
            new[key] = value

    for k, v in new.items():
        temp = [k]
        dictlist.append(temp)

    for j in range(0,len(dictlist)):
        str1 = ' '.join(dictlist[j])
        res.append(str1)
 
    return res




def process_date(date): 
    '''
    η συνάρτηση διαμορφώνει την ελληνική ημερομηνία του rss feed:
    Στο rss αρχείο η ημερομηνία είναι της μορφής: Wed, 14 Jun 2017 17:21:16 GMT
    Θα πρέπει να διαμορφώνεται σε ελληνική ημερομηνία, πχ: Τετ, 14 Ιουν 2017
    :param date:
    :return: η ελληνική ημερομηνία
    '''
    days = {"Mon":"Δευ" ,"Tue":"Τρι" ,"Wed":"Τετ" ,"Thu":"Πεμ" ,"Fri":"Παρ" , "Sat":"Σαβ" ,"Sun":"Κυρ" }


    months = {"Jan":"Ιαν","Feb":"Φεβ", "Mar":"Μαρ", "Apr":"Απρ", "May":"Μαι" , "Jun":"Ιουν" , "Jul":"Ιουλ" , "Aug":"Αυγ","Sep":"Σεπ","Oct":"Οκτ","Nov":"Νοε","Dec":"Δεκ"}

    
    st = ''.join(date)
    pattD = "(^...?)"
    pattM = "...,?\s\d\d\s(...?)"
    pattern = r"(^...,\s\d\d\s...\s\d\d\d\d)"
    res = re.findall(pattern,st,re.I)
    
    new  = ''.join(res)
    
    
    M = re.findall(pattM,st,re.I)
    D = re.findall(pattD,''.join(date),re.I)
    month = ''.join(M)
    day = ''.join(D)
    
    
    for k,v in months.items():
        if k == month:
            month = months[k]
           
    for k,v in days.items():
        if k == day:
            day = days[k]
    patty = r"^...,\s\d\d\s...(\s\d\d\d\d)"
    y = re.findall(patty,st,re.I)
   
    year = ''.join(y)

    pattN = r"^...(,\s\d\d\s)...\s\d\d\d\d"
    N = re.findall(pattN,st,re.I)
    #print(N)
    No = ''.join(N)

    
    new_date = day+No+month+year
  
       
    return new_date

    
    


def load_arxes(): 
    #fortonei ta stoixeia twn arxwn me 500 apo to arxei p exei dimiourgithei
    #fortonei to arxeio kai vazei ta onoma sto leksiko arxes
    #to lekskiko einai prosvsimo apo t sunarthsh gt einai katholiko
    '''
    φορτώνει τις αρχές στο λεξικό arxes{}
    '''
    i = 1
    with open('500_arxes.csv','r') as document:
        for line in document:
            line = line.strip()
            (key,val) = line.split(';')
            arxes[key] = val
    return arxes
######### main ###############
'''
το κυρίως πρόγραμμα διαχειρίζεται την αλληλεπίδραση με τον χρήστη
'''
load_arxes()
while True :
    arxh = input(50*"^"+"\nΟΝΟΜΑ ΑΡΧΗΣ:(τουλάχιστον 3 χαρακτήρες), ? για λίστα:")
    if arxh == '':
        break
    elif arxh == "?": # παρουσιάζει τα ονόματα των αρχών
        for k,v in arxes.items():
            print (k,v)
    elif len(arxh) >= 3 :
        # αναζητάει όνομα αρχής που ταιριάζει στα κριτήρια του χρήστη
        result = search_arxes(arxh) 
        for r in result:
            print (result.index(r)+1, r, arxes[r])
        while result:
            epilogh = input("ΕΠΙΛΟΓΗ....")
            if epilogh == "": break
            elif epilogh.isdigit() and 0<int(epilogh)<len(result)+1:
                epilogh = int(epilogh)
                url = arxes[result[epilogh-1]]
                print(url)
                # καλεί τη συνάρτηση που φορτώνει το αρχείο rss:
                rss_feed(url)
            else: continue
    else :
        continue
