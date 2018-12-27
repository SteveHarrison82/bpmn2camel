class MessageStartEvent2Camel:
    def __init__(self, from_uri, to_uri):
        self.from_uri = from_uri
        self.to_uri = to_uri

    def get_as_dict(self):
        message_start_event_as_dict = {'from': self.from_uri, 'to': self.to_uri}
        return message_start_event_as_dict
