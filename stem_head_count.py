from collections import Counter
all_words = Counter()
start = time.time()
progress = 0
def count_everything(x):
    global start
    global all_words
    global progress
    x = x.split(‘ ‘)
    for word in x:
        all_words[word] += 1
    progress += 1
    end = time.time()
 sys.stdout.write(‘\r {} percent, {} position, {} per second ‘.format((str(float(progress / len(articles)))),
 (progress), (1 / (end — start))))
    start = time.time()
for item in articles.stems:
    count_everything(item)
    

allwordsdf = pd.DataFrame(columns = [‘words’, ‘count’])
allwordsdf[‘count’] = pd.Series(list(all_words.values()))
allwordsdf[‘words’] = pd.Series(list(all_words.keys()))
allwordsdf.index = allwordsdf[‘words’]