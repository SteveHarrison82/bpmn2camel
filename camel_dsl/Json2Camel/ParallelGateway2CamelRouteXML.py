from datetime import datetime

from camel_dsl.Json2Camel.Json2CamelUtil import Json2CamelUtil


class ParallelGateway2CamelRouteXML:
    def __init__(self, parallelGateway2Camel):
        self.parallelGateway2Camel = parallelGateway2Camel

    def save_parallelgateway_routes(self):
        jcu = Json2CamelUtil(self.parallelGateway2Camel)
        xml2file = jcu.data2xml()
        with open('parallel_gateway' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.xml', 'a') as file:
            file.write(xml2file)
            file.write("\n")
        return xml2file
