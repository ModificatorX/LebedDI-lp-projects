import re
import requests
import sys
def req(res, k):
   
    si=re.findall(r'\w+\:\/\/\w+\.\w+\.\w+[/]{0,1}[a-z]*', res)
    sis=set()
    sis.update(si)
    em=re.findall(r'[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+\.{,1}[A-Za-z]*', res)
    setmail.update(em)
    #print(setmail) #Если захочется отслеживать прогресс: разбить стекло/убрать комментарий с функции
    if (k<5) and sis:
        
        for i in sis:
            if i not in forbiddensites:
                k=k+1;
                forbiddensites.update(i)
                try :
                    ru = requests.get(i)
                    resq=ru.text
                except requests.exceptions.ConnectionError:
                    pass
                
                req(resq, k)
    
    
    
    return 0
        

r = requests.get('http://www.rbc.ru')
res=r.text
k=0;
setmail=set()
forbiddensites=set()
req(res, k)
print('\n\n',setmail)

