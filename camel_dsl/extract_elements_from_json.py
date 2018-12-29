import json
import logging
from Json2Camel import ServiceTask2Camel
from Json2Camel import ServiceTask2CamelRouteXML
from Json2Camel import MessageStartEvent2Camel
from Json2Camel import MessageStartEvent2CamelRouteXML
from Json2Camel import ParallelGateway2Camel
from Json2Camel import ParallelGateway2CamelRouteXML
from Json2Camel import EndEvent2Camel
from Json2Camel import EndEvent2CamelRouteXML
from camel_dsl.Json2Camel import InclusiveGateway2Camel
from camel_dsl.Json2Camel import InclusiveGateway2CamelRouteXML

logging.basicConfig(filename='example.log', level=logging.DEBUG)

json_file = "../acceptance-test/bpmn2json.json"


class JsonUtil:
    def load_elements(self):
        with open(json_file) as file:
            self.loaded_json = {}
            bpmn_elements = file.read()
            self.loaded_json = json.loads(bpmn_elements)
            for x in self.loaded_json:
                logging.info("%s: %s" % (x, self.loaded_json[x]))
        return self.loaded_json

    def from_uri(self, bpmn_ref_incomings, multiple_uri=False):

        if multiple_uri:
            from_uris = []
            for each_from_uri in bpmn_ref_incomings:
                from_uris.append("seda:" + each_from_uri)
            return from_uris

        else:
            incoming = bpmn_ref_incomings[0]
            from_uri = "seda:" + incoming
            return from_uri

    def from_source(self, msg_source):
        from_uri = 'activemq:' + 'my_queue'
        return from_uri

    def to_uri(self, bpmn_ref_outgoings):
        outgoing = bpmn_ref_outgoings[0]
        to_uri = "seda:" + outgoing
        return to_uri

    def multiple_receipients(self, bpmn_ref_outgoings):
        mul_receipients = {}
        bpmn_ref_outgoings_with_queues = []
        use_queue = "seda:"
        for each_value in bpmn_ref_outgoings:
            bpmn_ref_outgoings_with_queues.append(use_queue + each_value)
        mul_receipients["multicast"] = bpmn_ref_outgoings_with_queues
        return mul_receipients

    def process_to_execute(self, bpmn_ref_process):
        process_to_execute = bpmn_ref_process
        return process_to_execute

    def find_camel_elements(self):

        camel_elements = self.load_elements()
        for each_key, each_value in camel_elements.iteritems():
            logging.info('node is: ' + each_key)
            logging.info('node content is: ' + str(each_value))
            logging.info('node type is: ' + str(each_value['node_type']))
            if each_value['node_type'] == "ServiceTask":
                serviceTask2Camel = ServiceTask2Camel.ServiceTask2Camel(self.from_uri(each_value['incomings']),
                                                                        self.to_uri(each_value['outgoings']),
                                                                        self.process_to_execute(each_value['node_name'])
                                                                        )
                gen_servicetask_route = ServiceTask2CamelRouteXML.ServiceTask2CamelRouteXML(serviceTask2Camel)
                logging.info('generated xml is: ' + gen_servicetask_route.save_servicetask_routes())

            if each_value['node_type'] == "StartEvent":
                messageStartEvent2Camel = MessageStartEvent2Camel.MessageStartEvent2Camel(self.from_source('my_queue'),
                                                                                          self.to_uri(
                                                                                              each_value['outgoings']))
                gen_message_start_event_route = MessageStartEvent2CamelRouteXML.MessageStartEvent2CamelRouteXML(
                    messageStartEvent2Camel)
                logging.info('generated xml is: ' + gen_message_start_event_route.save_message_start_event_routes())

            if each_value['node_type'] == "ParallelGateway":
                parallelGateway2Camel = ParallelGateway2Camel.ParallelGateway2Camel(
                    self.from_uri(each_value['incomings']),
                    self.multiple_receipients(
                        each_value['outgoings']))
                gen_parallel_gateway_route = ParallelGateway2CamelRouteXML.ParallelGateway2CamelRouteXML(
                    parallelGateway2Camel)
                logging.info('generated xml is: ' + gen_parallel_gateway_route.save_parallelgateway_routes())

            if each_value['node_type'] == "InclusiveGateway":
                inclusiveGateway2Camel = InclusiveGateway2Camel.InclusiveGateway2Camel(
                    self.from_uri(each_value['incomings'], multiple_uri=True),
                    each_value['id'])
                gen_inclusive_gateway_route = InclusiveGateway2CamelRouteXML.InclusiveGateway2CamelRouteXML(
                    inclusiveGateway2Camel)
                logging.info(
                    'generated xml is: ' + str(gen_inclusive_gateway_route.save_inclusivegateways_input_routes()))

            if each_value['node_type'] == "EndEvent":
                endEvent2Camel = EndEvent2Camel.EndEvent2Camel(self.from_uri(each_value['incomings']))
                gen_end_event_route = EndEvent2CamelRouteXML.EndEvent2CamelRouteXML(
                    endEvent2Camel)
                logging.info('generated xml is: ' + gen_end_event_route.save_endevent_routes())
