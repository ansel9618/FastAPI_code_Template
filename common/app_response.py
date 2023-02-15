from common.messages import Messages
from common.app_constants import AppConstants


class AppResponse(dict):
    def _init_(self, code_param =AppConstants.UNSUCCESSFULL_STATUS_CODE, data_param={},
                 message_param=Messages.FAILED, status_param=Messages.FALSE):
        dict._init_(self, code=code_param, data=data_param, message=message_param, status=status_param)

    def set_response(self, code_param, data_param, message_param, status_param, info_param=None):
        self['code'] = code_param
        self['data'] = data_param
        self['message'] = message_param
        self['status'] = status_param
        self['info'] = info_param

'''---------DOC---------------
The above code defines a class AppResponse that extends the built-in dict class. 
It provides methods to set and initialize an HTTP response with a JSON payload
 that includes the following keys: code, data, message, status, and info.

The _init_ method initializes the dictionary with default values. 
The set_response method updates the dictionary with the given parameters and corresponding keys.

code_param is the HTTP status code, data_param is the JSON payload, 
message_param is a message string, status_param is a boolean value to indicate success or failure, 
and info_param is an optional dictionary that can contain additional information about the response.

Overall, this class is used to generate consistent JSON responses for an API.
'''