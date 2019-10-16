class MemiumError(Exception):

    pass


class CommandAlreadyExistsError(MemiumError):

    pass


class CommandDoesNotExistError(MemiumError):

    pass
