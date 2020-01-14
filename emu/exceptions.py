from pywps.app.exceptions import ProcessError


class StorageLimitExceeded(ProcessError):
    default_msg = 'You have exceeded the storage limit'

    def __init__(self, msg=None, used=None, available=None):
        if used and available:
            msg = msg or self.default_msg
            self.msg = "{}: used={}, available={}".format(msg, used, available)
        else:
            self.msg = msg


class TimeLimitExceeded(StorageLimitExceeded):
    default_msg = 'You have exceeded the time limit'


class DryRunWarning(ProcessError):
    default_msg = 'You have submitted a job in dry-run mode'

    def __init__(self, msg=None, storage_used=None, time_used=None):
        if storage_used and time_used:
            msg = msg or self.default_msg
            self.msg = "{}. Used resources: storage={}, time={}".format(msg, storage_used, time_used)
        else:
            self.msg = msg
