import lxml.etree as et

class Json2CamelUtil:

    def __init__(self, element2camel):
        self.element2camel = element2camel

    def data2xml(self, name='route'):
        route = et.Element(name)
        return et.tostring(self.buildxml(route, self.element2camel.get_as_dict()))

    def buildxml(self, route, xml_ele):
        stc  = xml_ele
        if isinstance(stc, dict):
            for each_key, each_value in stc.iteritems():
                s = et.SubElement(route, each_key)
                self.buildxml(s, each_value)
        elif isinstance(self.element2camel, tuple) or isinstance(stc, list):
            pass
        elif isinstance(stc, basestring):
            route.text = stc
        else:
            route.text = str(stc)
        return route
