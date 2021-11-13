import lxml.etree as et
from datetime import datetime
from operator import attrgetter
import collections


# reference: https://code.activestate.com/recipes/577882-convert-a-nested-python-data-structure-to-xml/

class Json2CamelUtil:
    camel_route = []
    camel_sub_routes = []

    def __init__(self, element2camel):
        self.element2camel = element2camel

    def data2xml(self, multiple_dict=None, name='route'):
        route = et.Element(name)
        xml2file = []
        if multiple_dict == True:
            for each_dict in self.element2camel.get_routes_as_dict():
                route = et.Element(name)
                route_as_string = et.tostring(self.buildxml(route, each_dict))
                self.generate_camel_route(route, route_as_string)
                xml2file.append(route_as_string)
            return xml2file
        else:
            route_as_string = et.tostring(self.buildxml(route, self.element2camel.get_routes_as_dict()))
            self.generate_camel_route(route, route_as_string)
            return route_as_string

    def buildxml(self, route, xml_ele):
        stc = xml_ele
        if isinstance(stc, dict) or isinstance(stc, collections.OrderedDict):
            for each_key, each_value in stc.items():
                s = et.SubElement(route, each_key)
                self.buildxml(s, each_value)
        elif isinstance(stc, tuple) or isinstance(stc, list):
            for each_value_of_element2camel in stc:
                s = et.SubElement(route, 'to')
                self.buildxml(s, each_value_of_element2camel)

        # recursion: basecase
        elif isinstance(stc, str):
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

    def generate_camel_route(self, route, route_as_string):
        root = et.fromstring(route_as_string)
        if root.tag == 'route':
            Json2CamelUtil.camel_sub_routes.append(route)
        if root.tag == 'routes':
            Json2CamelUtil.camel_route.append(route)
        if len(Json2CamelUtil.camel_route) == 1:
            for each_route_defined in Json2CamelUtil.camel_sub_routes:
                lang = et.ElementTree(Json2CamelUtil.camel_route[0])
                routes = lang.getroot()
                routes.append(each_route_defined)
                Json2CamelUtil.camel_route = []
                Json2CamelUtil.camel_route.append(routes)

            root = Json2CamelUtil.camel_route[0]
            save_route = et.tostring(root).decode("utf-8")
            self.save_camel_routes(save_route)

    def save_camel_routes(self, save_to_file):
        with open('camel_route' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.xml', 'w+') as file:
            file.write(save_to_file)
            file.write("\n")
