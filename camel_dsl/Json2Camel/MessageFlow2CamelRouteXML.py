from datetime import datetime

from camel_dsl.Json2Camel.Json2CamelUtil import Json2CamelUtil


class MessageFlow2CamelRouteXML:
    def __init__(self, messageFlow2Camel):
        self.messageFlow2Camel = messageFlow2Camel

    def save_messageflow_routes(self):
        jcu = Json2CamelUtil(self.messageFlow2Camel)
        xml2file = jcu.data2xml(name="routes")
        with open('messageflow_routes' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.xml', 'a') as file:
            file.write(xml2file)
            file.write("\n")
        return xml2file
