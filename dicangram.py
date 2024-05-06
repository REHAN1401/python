wlist = ["listen", "silent", "enlist", "hello", "lone", "noel"]
dic={}
for w in wlist:
    sor = ''.join(sorted(wlist))
    if sor in dic:
        dic[sor].append(w)
    else:
        dic[sor]=[w]
for key in sorted(dic):
    print(", ".join(dic[key]))
