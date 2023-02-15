import traceback
import jwt
from fastapi import Request
from fastapi.responses import JSONResponse
from common.app_response import AppResponse
from common.log_data import ApplicationLogger as applog
from common.messages import Messages
import os


async def jwt_validation(request: Request):
    """
    This function used to validate the headers
    Args:
        request headers
    """
    app_response = AppResponse()
    applog.info(f"JWT VALIDATION INVOKED | requesting headers ")
    # fetching the headers
    headers = request.headers
    # fetching the authorization token
    if 'Authorization' in headers:
        bearer = headers.get('Authorization')
        if 'Bearer' in bearer:
            token = bearer.split()[1]
        else:
            app_response.set_response(401, {}, Messages.AUTHORIZATION_FAILED, False)
            return app_response
    else:
        app_response.set_response(401, {}, Messages.AUTHORIZATION_MISSING, False)
        return app_response
    try:
        applog.info(f"JWT VALIDATION INVOKED | Using the token:")

        # Decode the JWT
        secret_key = os.getenv("jwt_secret")
        decoded_jwt = jwt.decode(token, key=secret_key, verify=True, algorithms=['HS256'])

        # Access the claims contained in the JWT
        applog.info(f"JWT VALIDATION | JWT validation result: {decoded_jwt}")
        print("Decoded JWT:", decoded_jwt)
        if decoded_jwt:
            applog.info(
                f"JWT VALIDATION | Validated the headers, Token:")
            app_response.set_response(200, {}, "Header validation is successful", True)
        else:
            applog.info(f"JWT VALIDATION | Invalid/Expired Token")
            app_response.set_response(401, {}, "Authorization token is Expired or Invalid", False)

    except jwt.DecodeError:
        applog.error("JWT VALIDATION | JWT Validation failed")
        app_response.set_response(401, {}, Messages.AUTHORIZATION_FAILED, False)
        return app_response

    except Exception as exp:
        applog.error(f"Exception occurred in JWT token validation: {traceback.format_exc()} \n"
                     f"exception: {exp}")
        return JSONResponse(status_code=500, content={"code": 500, "message": Messages.EXCEPTION_JWT, "status": False})

    finally:
        return app_response