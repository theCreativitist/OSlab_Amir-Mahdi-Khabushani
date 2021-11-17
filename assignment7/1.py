import random
random.seed()
boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']

results = []
married_girls = ['default'] 
for b in boys:
    wife = 'default' # "default" is set to help avoid duplicate wives
    while (wife in married_girls):
        wife = girls[random.randint(0,len(girls)-1)]
    married_girls.append(wife)
    couple = (b, wife)
    results.append(couple)

print(results)
