class EndEvent:
    def __init__(self, bpmn_node_name, bpmn_id, node_type, bpmn_incoming=None,
                 bpmn_configuration_properties=None):
        if bpmn_incoming is None:
            bpmn_incoming = []

        if bpmn_configuration_properties is None:
            bpmn_configuration_properties = {}

        self.node_type = node_type
        self.incomings = bpmn_incoming
        self.node_name = bpmn_node_name
        self.id = bpmn_id
        self.configuration_properties = bpmn_configuration_properties