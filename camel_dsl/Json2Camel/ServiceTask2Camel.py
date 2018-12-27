class ServiceTask2Camel:

    def __init__(self, from_uri, to_uri, process_to_execute):
        self.from_uri = from_uri
        self.to_uri = to_uri
        self.process_to_execute = process_to_execute

    def get_as_dict(self):
        servicetask_as_dict = {'from': self.from_uri, 'to': self.to_uri, 'process': self.process_to_execute}
        return servicetask_as_dict
