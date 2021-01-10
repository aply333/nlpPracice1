import csv
import nltk
from datetime import date
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def createlog(data):
    with open('sortLog.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# DUMMY DATA SET
testData = [
    {"title": "The president passed a big bill.", "other": "other stuff"},
    {"title": "The president vetoed a big bill.", "other": "other stuff"},
    {"title": "James won the game.", "other": "other stuff"},
    {"title": "Major League Baseball now hosts golf.", "other": "other stuff"},
    {"title": "The new Hollywood release bombed.", "other": "other stuff"},
    {"title": "Film industry experiments with new cameras.", "other": "other stuff"},
    {"title": "Sony A99 cameras, now run on AA batteries.", "other": "other stuff"},
    {"title": "Fujifilm cameras colors reach new heights", "other": "other stuff"},
    {"title": "Congress voted for a new stimulus bill.", "other": "other stuff"},
    {"title": "Developers pioneer new open source project.", "other": "other stuff"},
    {"title": "Wayzo, open source navigation library.", "other": "other stuff"},
    {"title": "The new python toolkit, Wayzo, expands open source prospects.", "other": "other stuff"},
    {"title": "New vaccines shows to be 100 percent effective.", "other": "other stuff"},
    {"title": "CDC, passed approval of new vaccine, which has shown to be effective.", "other": "other stuff"},
    {"title": "Senate, argues over is helping people is their job.", "other": "other stuff"},
    {"title": "The house, argues why helping poeple is expensive.", "other": "other stuff"},
    {"title": "Massive meteor threat forces Earth to begin evacuations to Mars, the red planet", "other": "other stuff"},
    {"title": "Mars becomes the first planet to effectively support life on its surface after the destruction of Earth.", "other": "other stuff"},
    {"title": "Mars's agriculture program successfully breeds a nee brand of soil resistant carrots.", "other": "other stuff"}
]

# Compare Function
def titleCompare(title1, title2):
    # Remove stop words.
    # Remove punctuation.
    sw = stopwords.words('english')
    sw.append(',')
    sw.append('.')
    # make data lower case
    lowered1 = title1.lower()
    lowered2 = title2.lower()
    # remove sw
    kw1 = [w for w in lowered1 if not w in sw]
    kw2 = [w for w in lowered2 if not w in sw]
    # Keyword pool
    keyword_merge = kw1 + kw2
    kset1 = set(kw1)
    kset2 = set(kw2)
    keywords = set(keyword_merge)
    # Compare keywords:
    res1 = []
    res2 = []
    for w in keywords:
        if w in kset1:
            res1.append(1)
        else:
            res1.append(0)
        if w in kset2:
            res2.append(1)
        else:
            res2.append(0)
    c = 0
    for i in range(len(keywords)):
        c += res1[i]*res2[i]
    cosine = c/float((sum(res1)*sum(res2))**0.5)
    # print("Rating:", cosine)
    return cosine

# Mass Comparison:
def massComparison(dataSet ,initial):
    results = []
    for article in dataSet:
        rating = titleCompare(initial, article["title"])
        if rating > 0.75:
            results.append((article['title'],rating))
    results.sort(key= lambda x:x[1], reverse=True)
    return results


def totalGrouping(dataSet):
    finalGroups = []
    time = date.today()
    createlog([f'Log Start: {time}'])
    for article in dataSet:
        grouping = massComparison(dataSet, article["title"])
        createlog(grouping)
        # finalGroups[article["title"]] = grouping
        finalGroups.append(grouping)
    createlog(['Log End'])

   


totalGrouping(testData)