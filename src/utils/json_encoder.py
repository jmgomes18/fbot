import datetime
from json import JSONEncoder


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()

        try:
            return obj.tojson()
        except AttributeError:
            return JSONEncoder.default(self, obj)
