#!/usr/bin/python
import yaml
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['templates'], module_directory='mako_modules')


def serve_template(templatename, **kwargs):
    mytemplate = mylookup.get_template(templatename)
    return mytemplate.render(**kwargs)

yaml_file = open('yaml/report.yaml', 'r')

data = yaml.safe_load(yaml_file)

print serve_template('data_to_html.mako', data=data)
