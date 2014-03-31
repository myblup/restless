from .utils import json, MoreTypesJSONEncoder


class Serializer(object):
    def deserialize(self, body):
        raise NotImplementedError("Subclasses must implement this method.")

    def serialize(self, data):
        raise NotImplementedError("Subclasses must implement this method.")



class JSONSerializer(Serializer):
    def deserialize(self, body):
        """
        The low-level deserialization.

        Underpins ``deserialize``, ``deserialize_list`` &
        ``deserialize_detail``.

        Has no built-in smarts, simply loads the JSON.

        :param body: The body of the current request
        :type body: string

        :returns: The deserialized data
        :rtype: ``list`` or ``dict``
        """
        return json.loads(body)

    def serialize(self, data):
        """
        The low-level serialization.

        Underpins ``serialize``, ``serialize_list`` &
        ``serialize_detail``.

        Has no built-in smarts, simply dumps the JSON.

        :param data: The body for the response
        :type data: string

        :returns: A serialized version of the data
        :rtype: string
        """
        return json.dumps(data, cls=MoreTypesJSONEncoder)