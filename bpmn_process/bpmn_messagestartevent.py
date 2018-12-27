class MessageStartEvent:
    def __init__(self, bpmn_node_name, bpmn_id, node_type, bpmn_outgoing=None, bpmn_configuration_properties=None):

        if bpmn_outgoing is None:
            bpmn_outgoing = []

        if bpmn_configuration_properties is None:
            bpmn_configuration_properties = {}

        self.outgoings = bpmn_outgoing
        self.node_name = bpmn_node_name
        self.id = bpmn_id
        self.configuration_properties = bpmn_configuration_properties
        self.node_type = node_type
