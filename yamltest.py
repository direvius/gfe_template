#!/usr/bin/python
import yaml
from mako.template import Template

yaml_file = open('yaml/report.yaml', 'r')

data = yaml.safe_load(yaml_file)

mytemplate = Template(filename='templates/data_to_html.mako', module_directory='mako_modules')
print mytemplate.render(data=data)
