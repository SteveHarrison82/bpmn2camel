from datetime import datetime

from camel_dsl.Json2Camel.Json2CamelUtil import Json2CamelUtil

class ServiceTask2CamelRouteXML:
    def __init__(self, serviceTask2Camel):
        self.serviceTask2Camel = serviceTask2Camel

    def save_servicetask_routes(self):
        jcu = Json2CamelUtil(self.serviceTask2Camel)
        xml2file = jcu.data2xml()
        with open('servicetask_routes' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.xml', 'a') as file:
            file.write(xml2file)
            file.write("\n")
        return xml2file
