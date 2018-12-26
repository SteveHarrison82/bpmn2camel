import lxml.etree as et
from datetime import datetime

class ServiceTask2CamelRouteXML:

    def __init__(self, serviceTask2Camel):
        self.serviceTask2Camel = serviceTask2Camel

    def data2xml(self, name='route'):
        route = et.Element(name)
        return et.tostring(self.buildxml(route, self.serviceTask2Camel.get_as_dict()))

    def save_servicetask_routes(self):
        xml2file = self.data2xml()
        with open('servicetask_routes' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.xml', 'a') as file:
            file.write(xml2file)
            file.write("\n")
        return xml2file

    def buildxml(self, route, xml_ele):
        stc  = xml_ele
        if isinstance(stc, dict):
            for each_key, each_value in stc.iteritems():
                s = et.SubElement(route, each_key)
                self.buildxml(s, each_value)
        elif isinstance(self.serviceTask2Camel, tuple) or isinstance(stc, list):
            pass
        elif isinstance(stc, basestring):
            route.text = stc
        else:
            route.text = str(stc)
        return route
