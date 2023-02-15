import logging


class ApplicationLogger:
    def info(msg):
        return logging.getLogger('info_application').info(msg)

    def error(msg):
        return logging.getLogger('error_application').error(msg)

    def debug(msg):
        return logging.getLogger('debug_application').debug(msg)

    def warn(msg):
        return logging.getLogger('warning_application').warn(msg)


class ThirdPartyLogger:
    def info(msg):
        return logging.getLogger('info_third_party').info(msg)

    def error(msg):
        return logging.getLogger('error_third_party').error(msg)

    def debug(msg):
        return logging.getLogger('debug_third_party').debug(msg)

    def warn(msg):
        return logging.getLogger('warning_third_party').warn(msg)


class AuditLogger:
    def info(msg):
        return logging.getLogger('info_audit').info(msg)

    def error(msg):
        return logging.getLogger('error_audit').error(msg)

    def debug(msg):
        return logging.getLogger('debug_audit').debug(msg)

    def warn(msg):
        return logging.getLogger('warning_audit').warn(msg)


'''
The above code defines three classes for different types of logging - ApplicationLogger, 
ThirdPartyLogger, and AuditLogger. Each class has methods for logging different levels of messages 
- info, error, debug, and warn. The classes use the Python logging module to log messages to different 
log files, with the appropriate logger name based on the class name. These loggers can be used to log 
different types of messages in a modular and organized way.
'''