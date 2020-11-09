import re

test = "Кстати говоря, работает" 

def ReReplaceString(file, obj : str, new : str):
    f = open(file, 'r', encoding = "utf-8")

    current = f.read()
    f.close()

    try:
        regex = r"{}\s*\=\s*\'(.*)\'".format(obj)
        r = re.search(regex, current).group(1)
    except:
        regex = r'{}\s*\=\s*\"(.*)\"'.format(obj)
        r = re.search(regex, current).group(1)
        
    current = current.replace(r, new)    
        
    f = open(file, "w", encoding = "utf-8")    
        
    f.write(current)
    f.close()    
    
def ReReplacePerem(file, obj : str, new : str):
    f = open(file, 'r', encoding = "utf-8")
    
    current = f.read()
    f.close()
    
    regex = r"{}\s*\=\s*(.*)".format(obj)
    r = re.search(regex, current).group(1)
    
    current = current.replace(r, new, 1)
    
    f = open(file, "w", encoding = "utf-8")
    
    f.write(current)
    f.close()