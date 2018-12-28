import lxml.etree as et


# reference: https://code.activestate.com/recipes/577882-convert-a-nested-python-data-structure-to-xml/

class Json2CamelUtil:
    def __init__(self, element2camel):
        self.element2camel = element2camel

    def data2xml(self, name='route'):
        route = et.Element(name)
        return et.tostring(self.buildxml(route, self.element2camel.get_as_dict()))

    def buildxml(self, route, xml_ele):
        stc = xml_ele
        if isinstance(stc, dict):
            for each_key, each_value in stc.iteritems():
                s = et.SubElement(route, each_key)
                self.buildxml(s, each_value)
        elif isinstance(stc, tuple) or isinstance(stc, list):
            for each_value_of_element2camel in stc:
                s = et.SubElement(route, 'to')
                self.buildxml(s, each_value_of_element2camel)

        elif isinstance(stc, basestring):
            self._handle_attribute(route, stc)
        else:
            self._handle_attribute(route, stc)
        return route
        # recursion: basecase

    def _handle_attribute(self, route, stc):
        if route.tag == 'from':
            route.set('url', stc)

        elif route.tag == 'to':
            route.set('url', stc)

        elif route.tag == 'process':
            route.set('ref', stc)

        else:
            route.text = stc
