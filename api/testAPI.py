import requests
import pygal
from pygal.style import LightColorizedStyle as LCS , LightenStyle as LS 

#Make the api CALL
url = 'https://api.github.com/search/repositories?q=language:&sort=stars'
try:
    data = requests.get(url).json()

    print(data.keys())

    print("Total Reposotories:" , data['total_count'])
    print("Results :" , data['incomplete_results'])
    count = data['items']
    print("repos__returned:",  len(count))

    repo_dicts= count[0]
    print("\nKeys:" , len(repo_dicts))

    for key in sorted(repo_dicts.keys()):
        print(key)
    print("\nSelected info about repos§")
    print('Name:', repo_dicts['name'])
    print('Owner:' , repo_dicts['owner']['login'])
    print("Stars:" , repo_dicts['stargazers_count'])
    print("Proogramming language:", repo_dicts['language'])
    print('Created:', repo_dicts['created_at']) 
    print('Updated:', repo_dicts['updated_at'])


    #visualising data using pygal

    names , stars , lang = [], [], []
    for repos in count:
        names.append( repos['name'])
        stars.append(repos['stargazers_count'])
        lang.append(repos['language'])
        print(lang)

    my_style= LS('#333366', base_style=LCS)
    chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
    chart.title = 'Most-Starred Python Projects on GitHub'
    chart.x_labels = names
    chart.add('', stars)
    chart.render_to_file('python_repos.svg') 
    

except requests.exceptions.RequestException as e:
  print(f"and error accured : {e}")

