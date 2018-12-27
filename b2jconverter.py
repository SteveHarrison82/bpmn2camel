import untangle
from bpmn_process import bpmn_messageflow
from bpmn_process import bpmn_endevent
from bpmn_process import bpmn_messagestartevent
from bpmn_process import bpmn_servicetask
from bpmn_process import bpmn_parallelgateway
from bpmn_process import bpmn_inclusivegateway
from bpmn_process import bpmn_intermediate_messagethrowevent
import json


class BpmnXml2py:
    bpmnxml2py = None;
    bpmn_dict = {}

    def load_bpmnxml2py(self, filepath):
        self.bpmnxml2py = untangle.parse(filepath)

    def get_configuration_properties(self, elements):
        configuration_properties = {}
        for each_element in elements:
            configuration_properties[str(each_element['name'])] = str(each_element['value'])
        return configuration_properties

    def get_incomings(self, element):
        incoming_flows = []
        incomings = element.bpmn_incoming
        for each_incoming in incomings:
            incoming_flows.append(str(each_incoming.cdata))
        return list(set(incoming_flows))

    def get_outgoings(self, element):
        outgoing_flows = []
        outgoings = element.bpmn_outgoing
        for each_outgoing in outgoings:
            outgoing_flows.append(str(each_outgoing.cdata))
        return list(set(outgoing_flows))

    def get_processes(self, bpmnxml2py):
        elements_in_mf = bpmnxml2py.bpmn_definitions.bpmn_process.children
        for each_element_of_mf in elements_in_mf:
            if each_element_of_mf.__dict__['_name'] == "bpmn_endEvent":
                self.end_point_name = each_element_of_mf['name']
                self.end_point_id = each_element_of_mf['id']
                self.end_point_configuration__properties = self.get_configuration_properties(
                    each_element_of_mf.bpmn_extensionElements.camunda_properties.camunda_property)
                self.end_point_incoming = self.get_incomings(each_element_of_mf)
                endpoint = bpmn_endevent.EndEvent(self.end_point_name, self.end_point_id, "EndEvent",
                                                  self.end_point_incoming, self.end_point_configuration__properties)
                s = json.dumps(endpoint.__dict__)
                self.bpmn_dict[str(each_element_of_mf['id'])] = json.loads(s)

            if each_element_of_mf.__dict__['_name'] == "bpmn_startEvent":
                self.start_point_name = each_element_of_mf['name']
                self.start_point_id = each_element_of_mf['id']
                self.start_point_configuration__properties = self.get_configuration_properties(
                    each_element_of_mf.bpmn_extensionElements.camunda_properties.camunda_property)
                self.start_point_outcoming = self.get_outgoings(each_element_of_mf)
                startpoint = bpmn_messagestartevent.MessageStartEvent(self.start_point_name, self.start_point_id,
                                                                      "StartEvent", self.start_point_outcoming,
                                                                      self.start_point_configuration__properties)
                s = json.dumps(startpoint.__dict__)
                self.bpmn_dict[str(each_element_of_mf['id'])] = json.loads(s)

            if each_element_of_mf.__dict__['_name'] == "bpmn_inclusiveGateway":
                self.inclusive_gateway_name = each_element_of_mf['name']
                self.inclusive_gateway_id = each_element_of_mf['id']
                self.inclusive_gateway_configuration = self.get_configuration_properties(
                    each_element_of_mf.bpmn_extensionElements.camunda_properties.camunda_property)
                self.inclusive_gateway_incoming = self.get_incomings(each_element_of_mf)
                self.inclusive_gateway_outgoing = self.get_outgoings(each_element_of_mf)
                inclusive_gateway = bpmn_inclusivegateway.InclusiveGateway(self.inclusive_gateway_name,
                                                                           self.inclusive_gateway_id,
                                                                           "InclusiveGateway",
                                                                           self.inclusive_gateway_incoming,
                                                                           self.inclusive_gateway_outgoing,
                                                                           self.inclusive_gateway_configuration)
                s = json.dumps(inclusive_gateway.__dict__)
                self.bpmn_dict[str(each_element_of_mf['id'])] = json.loads(s)

            if each_element_of_mf.__dict__['_name'] == "bpmn_intermediateThrowEvent":
                self.message_throwevent_name = each_element_of_mf['name']
                self.message_throwevent_id = each_element_of_mf['id']
                self.message_throwevent_configuration = self.get_configuration_properties(
                    each_element_of_mf.bpmn_extensionElements.camunda_properties.camunda_property)
                self.message_throwevent_incoming = self.get_incomings(each_element_of_mf)
                self.message_throwevent_outgoing = self.get_outgoings(each_element_of_mf)
                message_throwevent = bpmn_intermediate_messagethrowevent.IntermediateMessageThrowEvent(
                    self.message_throwevent_name, self.message_throwevent_id, "MessageSend",
                    self.message_throwevent_incoming, self.message_throwevent_outgoing,
                    self.message_throwevent_configuration)
                s = json.dumps(message_throwevent.__dict__)
                self.bpmn_dict[str(each_element_of_mf['id'])] = json.loads(s)

            if each_element_of_mf.__dict__['_name'] == "bpmn_intermediateCatchEvent":
                pass

            if each_element_of_mf.__dict__['_name'] == "bpmn_parallelGateway":
                self.parallel_gateway_name = each_element_of_mf['name']
                self.parallel_gateway_id = each_element_of_mf['id']
                self.parallel_gateway_configuration = self.get_configuration_properties(
                    each_element_of_mf.bpmn_extensionElements.camunda_properties.camunda_property)
                self.parallel_gateway_incoming = self.get_incomings(each_element_of_mf)
                self.parallel_gateway_outgoing = self.get_outgoings(each_element_of_mf)
                parallel_gateway = bpmn_parallelgateway.ParallelGateway(self.parallel_gateway_name,
                                                                        self.parallel_gateway_id, "ParallelGateway",
                                                                        self.parallel_gateway_incoming,
                                                                        self.parallel_gateway_outgoing,
                                                                        self.parallel_gateway_configuration)
                s = json.dumps(parallel_gateway.__dict__)
                self.bpmn_dict[str(each_element_of_mf['id'])] = json.loads(s)

            if each_element_of_mf.__dict__['_name'] == "bpmn_serviceTask":
                self.service_task_name = each_element_of_mf['name']
                self.service_task_id = each_element_of_mf['id']
                self.service_task_configuration__properties = self.get_configuration_properties(
                    each_element_of_mf.bpmn_extensionElements.camunda_properties.camunda_property)
                self.serivce_task_incoming = self.get_incomings(each_element_of_mf)
                self.serivce_task_outgoing = self.get_outgoings(each_element_of_mf)
                service_task = bpmn_servicetask.ServiceTask(self.service_task_name, self.service_task_id, "ServiceTask",
                                                            self.serivce_task_incoming, self.serivce_task_outgoing,
                                                            self.service_task_configuration__properties)
                s = json.dumps(service_task.__dict__)
                self.bpmn_dict[str(each_element_of_mf['id'])] = json.loads(s)

            if each_element_of_mf.__dict__['_name'] == "bpmn_sequenceFlow":
                pass

            if each_element_of_mf.__dict__['_name'] == "bpmn_extensionElements":
                self.mf_name = bpmnxml2py.bpmn_definitions.bpmn_process['name']
                self.mf_id = bpmnxml2py.bpmn_definitions.bpmn_process['id']
                self.mf_configuration_properties = self.get_configuration_properties(
                    bpmnxml2py.bpmn_definitions.bpmn_process.bpmn_extensionElements.camunda_properties.camunda_property)
                mf = bpmn_messageflow.MessageFlow(self.mf_name, self.mf_id, "MessageFlow",
                                                  self.mf_configuration_properties)
                s = json.dumps(mf.__dict__)
                self.bpmn_dict[str(bpmnxml2py.bpmn_definitions.bpmn_process['name'])] = json.loads(s)
                pass

            if each_element_of_mf.__dict__['_name'] == "bpmn_subProcess":
                pass

            print each_element_of_mf['name']

    def generate_json(self):
        with open("bpmn2json.json", "w") as file:
            file.write(json.dumps(self.bpmn_dict))
        pass
