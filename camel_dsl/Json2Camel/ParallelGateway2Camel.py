class ParallelGateway2Camel:

    def __init__(self, from_uri, multicast):
        self.from_uri = from_uri
        self.multicast_receipients = multicast

    def get_as_dict(self):
        parallelgateway_as_dict = {'from': self.from_uri, 'to': self.to_uri, 'process': self.process_to_execute}
        return parallelgateway_as_dict
