import re

test = "Кстати говоря, работает" 

def ReReplaceString(obj : str, new : str):
    f = open(__file__, 'r', encoding = "utf-8")

    current = f.read()
    f.close()

    try:
        regex = r"{}\s*\=\s*\'(.*)\'".format(obj)
        r = re.search(regex, current).group(1)
    except:
        regex = r'{}\s*\=\s*\"(.*)\"'.format(obj)
        r = re.search(regex, current).group(1)
        
    current = current.replace(r, new)    
        
    f = open(__file__, "w", encoding = "utf-8")    
        
    f.write(current)
    f.close()    