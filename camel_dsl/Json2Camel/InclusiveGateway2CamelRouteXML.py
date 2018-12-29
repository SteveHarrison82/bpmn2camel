from datetime import datetime

from camel_dsl.Json2Camel.Json2CamelUtil import Json2CamelUtil


class InclusiveGateway2CamelRouteXML:
    def __init__(self, inclusveGateway2Camel):
        self.inclusveGateway2Camel = inclusveGateway2Camel

    def save_inclusivegateways_input_routes(self):
        jcu = Json2CamelUtil(self.inclusveGateway2Camel)
        xml2file = jcu.data2xml(multiple_dict=True)
        with open('inclusive_gateway_input_routes' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.xml', 'a') as file:
            for each_route in xml2file:
                file.write(each_route)
                file.write("\n")
        return xml2file
