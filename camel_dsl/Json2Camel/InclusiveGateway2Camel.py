class InclusiveGateway2Camel:
    def __init__(self, from_uri, node_id):
        self.from_uri = from_uri
        self.intermediate_inclusive_gateway_queue = "seda:" + node_id

    def get_in_routes_as_dict(self):
        in_routes_as_list_of_dict = []
        for each_from_uri in self.from_uri:
            in_routes_as_list_of_dict.append(self._get_in_route_as_dict(each_from_uri))
        in_routes_as_list_of_dict.append(self._get_out_route_as_dict())
        return in_routes_as_list_of_dict

    def _get_in_route_as_dict(self, each_from_uri):
        return {'from': each_from_uri, 'to': self.intermediate_inclusive_gateway_queue}

    def _get_out_route_as_dict(self):
        completion_size = len(self.from_uri)
        return {'aggregate': completion_size, 'from': self.intermediate_inclusive_gateway_queue}
