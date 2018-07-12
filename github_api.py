__author__ = 'xianda'

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=start'
r = requests.get(url)
response_dict = r.json()
repo_dicts = response_dict['items']
name, stars = [], []
for repo_dict in repo_dicts:
    name.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
my_style = LS('#333366', base_style=LCS)
char = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
char.title = 'Most Starred Python Project On Github'
char.x_labels = name
char.add('', stars)
char.render_to_file('git.svg')
char.render_to_file('git.png')

