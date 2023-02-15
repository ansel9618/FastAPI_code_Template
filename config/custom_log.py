log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "basic": {
            "format": "[%(asctime)s] [APPLOG] [%(levelname)s] : %(message)s"
        },
        "basic2": {
            "format": "[%(asctime)s] [THPLOG] [%(levelname)s] : %(message)s"
        },
        "basic3": {
            "format": "[%(asctime)s] [AUDLOG] [%(levelname)s] : %(message)s"
        },
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "format": "[%(asctime)s] [APPLOG] [%(levelname)s] : %(message)s"
        },

    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "debug_handler_application_stderr": {
            "class": "logging.StreamHandler",
            "formatter": "basic",
            "level": "DEBUG",
            "stream": "ext://sys.stdout"
        },
        "info_handler_application_stderr": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "basic",
            "stream": "ext://sys.stdout"
        },
        "warning_handler_application_stderr": {
            "class": "logging.StreamHandler",
            "level": "WARN",
            "formatter": "basic",
            "stream": "ext://sys.stdout"
        },
        "error_handler_application_stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "basic",
            "stream": "ext://sys.stderr"
        },
        "debug_handler_third_party_stderr": {
            "class": "logging.StreamHandler",
            "formatter": "basic2",
            "level": "DEBUG",
            "stream": "ext://sys.stdout"
        },
        "info_handler_third_party_stderr": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "basic2",
            "stream": "ext://sys.stdout"
        },
        "warning_handler_third_party_stderr": {
            "class": "logging.StreamHandler",
            "level": "WARN",
            "formatter": "basic2",
            "stream": "ext://sys.stdout"
        },
        "error_handler_third_party_stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "basic2",
            "stream": "ext://sys.stderr"
        },
        "debug_handler_audit_log_stderr": {
            "class": "logging.StreamHandler",
            "formatter": "basic3",
            "level": "DEBUG",
            "stream": "ext://sys.stdout"
        },
        "info_handler_audit_stderr": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "basic3",
            "stream": "ext://sys.stdout"
        },
        "warning_handler_audit_stderr": {
            "class": "logging.StreamHandler",
            "level": "WARN",
            "formatter": "basic3",
            "stream": "ext://sys.stdout"
        },
        "error_handler_audit_stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "basic3",
            "stream": "ext://sys.stderr"
        }
    },
    "loggers": {
        "default": {
            "handlers": [
                "default"
            ],
            "level": "DEBUG"
        },
        "debug_application": {
            "handlers": [
                "debug_handler_application_stderr"
            ],
            "level": "DEBUG"
        },
        "info_application": {
            "handlers": [
                "info_handler_application_stderr"
            ],
            "level": "INFO"
        },
        "warning_application": {
            "handlers": [
                "warning_handler_application_stderr"
            ],
            "level": "WARN"
        },
        "error_application": {
            "handlers": [
                "error_handler_application_stderr"
            ],
            "level": "ERROR"
        },
        "debug_third_party": {
            "handlers": [
                "debug_handler_third_party_stderr"
            ],
            "level": "DEBUG"
        },
        "info_third_party": {
            "handlers": [
                "info_handler_third_party_stderr"
            ],
            "level": "INFO"
        },
        "warning_third_party": {
            "handlers": [
                "warning_handler_third_party_stderr"
            ],
            "level": "WARN"
        },
        "error_third_party": {
            "handlers": [
                "error_handler_third_party_stderr"
            ],
            "level": "ERROR"
        },
        "debug_audit": {
            "handlers": [
                "debug_handler_audit_log_stderr"
            ],
            "level": "DEBUG"
        },
        "info_audit": {
            "handlers": [
                "info_handler_audit_stderr"
            ],
            "level": "INFO"
        },
        "warning_audit": {
            "handlers": [
                "warning_handler_audit_stderr"
            ],
            "level": "WARN"
        },
        "error_audit": {
            "handlers": [
                "error_handler_audit_stderr"
            ],
            "level": "ERROR"
        }
    },
}