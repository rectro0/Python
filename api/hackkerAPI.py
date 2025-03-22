import requests
from operator import itemgetter

url= 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("status_code", r.status_code)

data= r.json()
submition= []
for submition_id in data[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submition_id) + '.json')

submition_r= requests.get(url).json()

submition_dict={
    'title' : submition_r['title'],
    'link' : 'http://news.ycombinator.com/item?id=' + str(submition_id),

    'comment': submition_r.get('decendants', 0)
}

submition.append(submition_dict)
submition = sorted(submition , key=itemgetter('comment'), reverse=True)


for sub in submition_dict:
    print("\nTitle:" , submition_dict['title'])
    print("Disscution link:" , submition_dict['link'])
    print("Comments:" , submition_dict['comment'])
