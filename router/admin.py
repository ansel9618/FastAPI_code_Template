from fastapi import APIRouter, status, Request, Depends
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from common.log_data import ApplicationLogger as applog
from schema.schemas import admin_role, GoogleLogin, responses, CreateAdmin, PostMakerChecker, AuthorizeActivity, \
    PostAdminRoles, DeactivateMessage
from services.admin_manager import country_manager
import traceback
from common.messages import Messages as msg
from dependencies.jwt_token_validation import jwt_validation

from fastapi import Query
from pydantic import Required

router_country = APIRouter(prefix='/country')

@router_country.get('/', status_code=status.HTTP_200_OK, tags=['Admin'],
                  responses={**responses, 200: {"description": "Successful Response",
                                                "content": {
                                                    "application/json": {
                                                        "example": {"code": 200,
                                                                    "message": "countries details fetch successful",
                                                                    "data": {}, "status": True, "info": {}}}}}})
async def get_country(request: Request,
                    keyword: str = Query(default=None),
                    limit: int = Query(default=None),
                    validation: dict = Depends(jwt_validation)):
    """
    This function is to fetch all the country details
    API name : GET list all country details
    Args:
        headers,id
    Return:
        json response with status code
    """
    try:
        param = {"keyword": keyword,"limit": limit}
        applog.info(f" GET get_country invoked | Starting the API call with mode ")
        if validation['code'] == 200:
            # fetching the headers
            headers = request.headers
            # calling get_user_manager function
            applog.info(f" GET get_country | Calling Manager function using headers: {headers} with mode ")
            manager_response = country_manager(param)
            if manager_response['code'] == 200:
                applog.info(f" GET get_country | Manager Function executed successfully with mode ")
                return JSONResponse(status_code=manager_response['code'],
                                    content={'code': manager_response['code'], \
                                             "message": manager_response['message'], 'data': manager_response['data'],
                                             'status': manager_response['status'], 'info': manager_response['info']})
            else:
                applog.error(f" GET get_country | API execution failed with mode ")
                return JSONResponse(status_code=manager_response['code'],
                                    content={"code": manager_response['code'], 'data': {},
                                             "message": manager_response['message'], 'status': False})
        else:
            applog.error(f" GET get_country | Headers validation failed ")
            return JSONResponse(status_code=validation['code'],
                                content={"code": validation['code'], "data": {},
                                         "message": validation['message'], "status": False})
    except Exception as exp:
        applog.error(
            f"Exception occurred in fetching GET get_country with mode {param['type']}, message: {traceback.format_exc()}"
            f"Exception: {exp}")
        raise HTTPException(status_code=500,
                            detail={"code": 500, 'data': {}, "message": msg.SOMETHING_WENT_WRONG, 'status': False})
    finally:
        pass

'''-------------------DOC--------------------------
The above code is a FastAPI route that defines a GET API endpoint to fetch country details from the database. 
It uses the APIRouter to define the endpoint with the prefix '/country'.

The endpoint is decorated with the @router_country.get decorator, which takes the endpoint path as an argument. 
It also specifies the expected HTTP status code for a successful response, along with other response details in the responses dictionary.

The function definition takes several parameters, including a Request object, and two query parameters 'keyword' and 'limit'. 
It also has a dependency on the jwt_validation function to validate the JWT token.

Within the function, it retrieves the query parameters 'keyword' and 'limit' using FastAPI's Query object.
It also retrieves the headers from the request object. It then logs an info message and passes the query parameters 
to the country_manager function to fetch country details.

If the JWT validation is successful, the function calls the country_manager function passing in the query parameters. 
The country_manager function returns a dictionary response containing a success or error message along with country data.

If the manager function returns a 200 status code, the endpoint returns a JSONResponse object containing the success 
message, country data, and a 200 status code. 
Otherwise, it returns a JSONResponse object with an error message and the error status code.

If there is an exception during the execution of the function, it logs an error message and raises an HTTPException 
with a 500 status code along with an error message.
'''