try:
    word_count = 0
    with open("story.txt") as f:
        lines = f.readlines()
        for line in lines:
            print(line,end = "")
            word_count+=len(line.split(" "))
    print(f"\nNumber of word is:{word_count}")
except Exception as e:
    print(f"File not found please check path {e}")