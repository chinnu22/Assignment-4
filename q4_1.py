try:
    with open("story.txt") as f:
        lines = f.readlines
        w_count = {}
        count = 0
        for line in lines:
            words = line.split(" ")
            for word in words:
                word = word.split()
                word = word.strip("\n")
                word = word.replace(',','')
                word = word.replace('.','')
                try:
                    w_count[word]+=1
                    


                except KeyError:
                    w_count[word] =1
    max_val = max(w_count.values())
    for k,v in w_count.items():
        if v == max_val:
            print(f"{k} : {v}")
    

except Exception as e:
    print(f"File not found please check the path {e}")