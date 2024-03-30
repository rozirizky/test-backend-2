import pandas as pd

df = pd.read_csv('movies.csv')

headers = []
movies = df['Title']
csv = []

for m in movies:
    replace = m.replace('Unknown','"null"')
    split = replace.split('"')
    index0 = split[0].split(',')
    split.pop(0)
    list = index0 + split
    csv.append(list)
    list[:] = [x for x in list if x != ',']
    list[:] = [x for x in list if x != '']
   
    if len(list) == 12:     
        genre = list[8].split(',')
        genre[:] = [x for x in genre if x != '']
        list.pop(8)
        index = 8
        for g in genre:
            list.insert(index,g)
            index+=1
    if len(list) == 12:
        list.insert(4,'null')
    if len(list) == 14:
        list[0] = list[0] + list[1]
        list.pop(1)
        
   
    release_date  = list[2] +" "+ list[3]
    list.append(release_date)
   

    list[9] = list[9].replace(',','')
    
   

    
    try:
        li = list[10]
        number = "".join([c for c in li if c.isdigit()]) 
        list[10] = int(number)
    except:
        li = 0
    
    try:
        li = list[11]
        number = "".join([c for c in li if c.isdigit()]) 
        list[11] = int(number)
    except:
        li = '0'
    
  
   
       
   

  

for h in df.columns:
    headers.append(h.lower())

headers.append('release_date')

data = pd.DataFrame(csv,columns=headers)

data.to_csv('new.csv')
