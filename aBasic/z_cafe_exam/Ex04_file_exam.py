with open('sample.txt', 'rt', encoding='utf-8') as f:
    lines = f.readlines()
    total=0
    for line in lines:
        score= int(line)
        total+=score

average=total/len(lines)

with open("result.txt", "w", encoding='utf-8') as s:
    s.write("총 합은 : {} \n평균 값은 : {}".format(str(total),str(average)))
    f.close()

