import json

class MessageFlow2Camel:

    def __init__(self, node_id, node_name, node_type):
        self.id = node_id
        self.node_name = node_name
        self.node_type = node_type

    def get_routes_as_dict(self):
        return {"description": json.dumps({"routeId": self.id, "displayName": self.node_name, "description": self.node_type + self.node_name})}
