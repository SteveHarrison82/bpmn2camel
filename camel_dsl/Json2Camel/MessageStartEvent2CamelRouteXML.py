from datetime import datetime
from camel_dsl.Json2Camel.Json2CamelUtil import Json2CamelUtil


class MessageStartEvent2CamelRouteXML:
    def __init__(self, messageStartEvent2Camel):
        self.messageStartEvent2Camel = messageStartEvent2Camel

    def save_message_start_event_routes(self):
        jcu = Json2CamelUtil(self.messageStartEvent2Camel)
        xml2file = jcu.data2xml()
        with open('messagestartevent_routes' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.xml', 'a') as file:
            file.write(xml2file)
            file.write("\n")
        return xml2file
