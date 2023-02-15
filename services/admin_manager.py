
import traceback
from common.app_response import AppResponse
from common.log_data import ApplicationLogger as applog
from common.messages import Messages
from fastapi.exceptions import HTTPException
from repository.admin_sql import country_filter


def country_manager(param):
    """ redirects code to country filter query in sql file
       Args:
        params
       Return:
           json response with status code
     """
    app_response = AppResponse()
    try:
        applog.info(
            f"country_manager invoked | calling the country_query function to fetch the country details")
        get_country_resp = country_filter(param)
        if get_country_resp['code'] == 200:
            applog.info(
                f"country_manager | GET country details by calling country details is successful")
            app_response.set_response(get_country_resp['code'], get_country_resp["data"],
                                      get_country_resp['message'], get_country_resp['status'], get_country_resp['info'])
        else:
            applog.error(f"admin_manager | Failed to get country details")
            app_response.set_response(get_country_resp['code'], get_country_resp["data"], get_country_resp['message'],
                                      get_country_resp['status'])
    except Exception as exp:
        applog.error(f"Exception occurred in country_manager with mode {traceback.format_exc()} \n"
                     f"exception: {exp}")
        raise HTTPException(status_code=500,
                            detail={"code": 500, "data": {}, "message": Messages.FAILED_TO_FETCH, "status": False})

    finally:
        return app_response


''' -----------DOC----------------------
The above code contains a function named country_manager which is responsible for fetching the country details.
 This function receives param as input, and then it logs the execution using ApplicationLogger and executes the 
 query to fetch the country details using country_filter function from the repository.admin_sql module. 
 If the response of the query is successful, then it sets the response using AppResponse module and returns the response. 
 If the response of the query fails, it logs the error and sets the response accordingly. If any exception occurs, it raises an HTTPException.
'''