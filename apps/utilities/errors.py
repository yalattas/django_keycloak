from rest_framework.exceptions import ValidationError
from enum import Enum
import logging
logger = logging.getLogger('django')

class Error(Enum):
    NO_ACTIVE_ACCOUNT = {'code': -500, 'detail': ('No active account found with the given credentials!')}
    ACCOUNT_ALREADY_EXIST = {'code': -301, 'detail': ('Account with this mobile number or email already exist')}
    ACCOUNT_DELETED = {'code': -302, 'detail': ('The account was deleted, please contact us to activate it')}
    USER_GROUP_ERROR = {'code': -303, 'detail': ('User doesn\'t belong to a group, add user to valid group')}
class APIError:
    def __init__(self, error: Error, extra=None):
        self.error = error
        self.extra = extra or None
        error_detail = error.value
        if self.extra:
            # Extra values can be used in foramtting a string that contains {}
            if isinstance(self.extra, list):
                error_detail['detail'] = error_detail['detail'].format(*extra)
        try:
            logger.warning(error.value)
        except BaseException:
            pass
        raise ValidationError(**error_detail)
