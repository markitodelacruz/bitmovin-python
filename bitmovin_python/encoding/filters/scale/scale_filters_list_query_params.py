
class ScaleFiltersListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, name: str = None, *args, **kwargs):
        super(ScaleFiltersListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
        self.name = name