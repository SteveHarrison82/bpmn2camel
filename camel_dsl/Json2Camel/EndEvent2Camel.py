import collections
class EndEvent2Camel:
    def __init__(self, from_uri):
        self.from_uri = from_uri
        self.to_uri = "seda:outbound"
        self.process_to_execute = "outbound_process"

    def get_routes_as_dict(self):
        end_event_as_dict = collections.OrderedDict()
        end_event_as_dict['from'] =  self.from_uri
        end_event_as_dict['process'] = self.process_to_execute
        end_event_as_dict['to'] = self.to_uri
        return end_event_as_dict
