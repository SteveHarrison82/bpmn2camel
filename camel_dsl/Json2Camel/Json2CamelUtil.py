import lxml.etree as et


# reference: https://code.activestate.com/recipes/577882-convert-a-nested-python-data-structure-to-xml/

class Json2CamelUtil:
    def __init__(self, element2camel):
        self.element2camel = element2camel

    def data2xml(self, multiple_dict=None, name='route'):
        route = et.Element(name)
        xml2file = []
        if multiple_dict == True:
            for each_dict in self.element2camel.get_routes_as_dict():
                route = et.Element(name)
                xml2file.append(et.tostring(self.buildxml(route, each_dict)))
            return xml2file
        else:
            return et.tostring(self.buildxml(route, self.element2camel.get_routes_as_dict()))

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

        # recursion: basecase
        elif isinstance(stc, basestring):
            self._handle_attribute(route, stc)
        else:
            self._handle_attribute(route, stc)
        return route

    def _handle_attribute(self, route, stc):
        if route.tag == 'from':
            route.set('uri', stc)

        elif route.tag == 'to':
            route.set('uri', stc)

        elif route.tag == 'process':
            route.set('ref', stc)

        elif route.tag == 'aggregate':
            route.set('strategyRef', 'myAggregationStrategy')
            route.set('completionSize', str(stc).decode("utf-8"))
            correlation_exp_element = et.SubElement(route, 'correlationExpression')
            header_element = et.SubElement(correlation_exp_element, 'header')
            header_element.text = 'EXCHANGE_ID'

        else:
            route.text = stc
