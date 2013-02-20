def chart_url(chart):
    metrics = []
    for target in chart['targets']:
        metrics.append("%s.%s" % (chart['prefix'], target['metric']))
    targets = ["target=%s" % metric for metric in metrics]
    if 'compare' in chart:
        targets.extend("target=timeShift(%s, %s)" % (metric, chart['compare']) for metric in metrics)
    return "http://advmon.yandex.ru/render?%s" % '&'.join(targets)
