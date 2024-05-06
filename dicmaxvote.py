from collections import Counter


 
votes =['john','johnny','jackie','johnny','john','jackie',
    'jamie','jamie','john','johnny','jamie','johnny','john']

x = Counter(votes)

maxv = max(x.values())

lst = [name for name,cnt in x.items() if cnt== maxv]
print(sorted(lst))