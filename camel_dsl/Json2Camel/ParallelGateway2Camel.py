class ParallelGateway2Camel:
    def __init__(self, from_uri, multicast=None):
        self.from_uri = from_uri

        if multicast is None:
            multicast = {}
        self.multicast_receipients = multicast

    def _get_as_dict_fromuri(self):
        parallelgateway_as_dict_fromuri = {'from': self.from_uri}
        return parallelgateway_as_dict_fromuri

    def _get_as_dict_multicast(self):
        return self.multicast_receipients

    def get_as_dict(self):
        x = self._get_as_dict_fromuri()
        y = self._get_as_dict_multicast()

        parallel_gateway_as_dict = x.copy()  # start with x's keys and values
        parallel_gateway_as_dict.update(y)   # modifies z with y's keys and values & returns None
        return parallel_gateway_as_dict
