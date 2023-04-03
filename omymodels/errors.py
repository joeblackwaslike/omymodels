class OMyModelsError(Exception):
    pass


class NoTablesError(OMyModelsError):
    def __init__(self, *args, **kwargs):
        if not args:
            default_msg = "No tables was found in DDL input."
            args = (default_msg,)
        super().__init__(*args, **kwargs)
