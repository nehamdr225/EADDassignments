from email import message_from_string

class EmailReader(object):
    def __init__(self,client):
        try:
            self._client = client
        except Exception as e:
            raise e

    def read(self):
        pass
