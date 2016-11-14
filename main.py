from bs4 import BeautifulSoup
import re
import mechanize
from threading import Thread

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
#br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
num1 = 999999 
num = 100000
num2 = 500000


def stuff(num):
    try:
        url = 'https://rt2012-chauffage.com/public/frontend/product/'+str(num)
        print url+'\n'
        page = br.open(url)
        content = page.read()
        soup = BeautifulSoup(content)
        isboiler = soup.body.findAll(text=re.compile('Chaudi'))
        if isboiler[0]:
            filename= str(num)+'.html'
            fp = open(filename,'wb')
            fp.write(soup.encode('utf-8'))
            fp.close()
            print"success :",num,'\n'
            isboiler=[]

    except:
        print "not available: ",num,'\n'
    return 1

while num < num1:

    t0 = Thread(target=stuff,args=(num,))
    t0.start()
    t1 = Thread(target=stuff,args=(num+1,))
    t1.start()
    t2 = Thread(target=stuff,args=(num+2,))
    t2.start()
    t3 = Thread(target=stuff,args=(num+3,))
    t3.start()
    t4 = Thread(target=stuff,args=(num+4,))
    t4.start()
    t5 = Thread(target=stuff,args=(num+5,))
    t5.start()
    t6 = Thread(target=stuff,args=(num+6,))
    t6.start()
    t7 = Thread(target=stuff,args=(num+7,))
    t7.start()

    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()

    num=num+8
