import collections
class InclusiveGateway2Camel:
    def __init__(self, from_uri, node_id, to_uri):
        self.from_uri = from_uri
        self.to_uri = to_uri
        self.intermediate_inclusive_gateway_queue = "seda:" + node_id

    def get_routes_as_dict(self):
        in_routes_as_list_of_dict = []
        for each_from_uri in self.from_uri:
            in_routes_as_list_of_dict.append(self._get_in_route_as_dict(each_from_uri))
        in_routes_as_list_of_dict.append(self._get_out_route_as_dict())
        return in_routes_as_list_of_dict

    def _get_in_route_as_dict(self, each_from_uri):
        inclusive_gatewawy_in_routes = collections.OrderedDict()
        inclusive_gatewawy_in_routes['from'] =  each_from_uri
        inclusive_gatewawy_in_routes['to'] = self.intermediate_inclusive_gateway_queue
        return inclusive_gatewawy_in_routes

    def _get_out_route_as_dict(self):
        completion_size = len(self.from_uri)
        inclusive_gatewawy_out_routes = collections.OrderedDict()
        inclusive_gatewawy_out_routes['from'] = self.intermediate_inclusive_gateway_queue
        inclusive_gatewawy_out_routes['aggregate'] = completion_size
        inclusive_gatewawy_out_routes['to'] = self.to_uri
        return inclusive_gatewawy_out_routes
