from mako.template import Template


def render(component, format):
    template_filename = "templates/%s_components/%s.mako" % (format, component['class'])
    template = Template(filename=template_filename, module_directory='mako_modules')
    return template.render(component=component)


def render_html(component):
    return render(component, 'html')
