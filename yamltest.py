#!/usr/bin/python
import yaml
from mako.template import Template

yaml_file = open('yaml/report.yaml', 'r')

data = yaml.safe_load(yaml_file)


def graphite_chart_url(graphite_chart):
    metrics = []
    for target in graphite_chart['targets']:
        metrics.append("%s.%s" % (graphite_chart['prefix'], target['metric']))
    targets = '&'.join("target=%s" % metric for metric in metrics)
    return "http://advmon.yandex.ru/render?%s" % targets

mytemplate = Template(filename='templates/data_to_html.mako', module_directory='mako_modules')
print mytemplate.render(data=data)
