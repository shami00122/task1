path = 'C:/Users/shuf4/TASK1/source.csv'      

with open(path, mode = 'r', encoding = "utf-8_sig") as f:
        l_strip = [s.strip() for s in f.readlines()]
        print(l_strip)

def characterEdit():

    name = input("キーワードを入力してください")
   
    if name in l_strip:
        print(f"{name}はキャラクターリストに存在します")
    else:
        print(f"{name}はキャラクターリストに存在しません")     
        l_strip.append(name.strip())  
        print(l_strip)  
            
        with open(path, mode='w', encoding='utf-8_sig') as f:
            f.write('\n'.join(l_strip))
    
characterEdit()    
    






          