from datetime import datetime

from camel_dsl.Json2Camel.Json2CamelUtil import Json2CamelUtil


class EndEvent2CamelRouteXML:
    def __init__(self, endEvent2Camel):
        self.endEvent2Camel = endEvent2Camel

    def save_endevent_routes(self):
        jcu = Json2CamelUtil(self.endEvent2Camel)
        xml2file = jcu.data2xml()
        with open('endevent_routes' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.xml', 'a') as file:
            file.write(xml2file)
            file.write("\n")
        return xml2file

