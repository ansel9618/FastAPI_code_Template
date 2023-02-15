from common.app_response import AppResponse
from fastapi.exceptions import HTTPException
from common.messages import Messages
from common.messages import Messages as msg
from common.log_data import ApplicationLogger as applog
import traceback
from sqlalchemy import Table, MetaData
from config.db_config import Session, engine
from functools import lru_cache


@lru_cache()
def get_db():
    return Session()

@lru_cache()
class Tables:
    def __init__(self):
        self.country = Table("country_table", MetaData(), autoload_with=engine)


table = Tables()
session = get_db()


def country_filter(param):
    '''
    fetches country details based on query params in param
    and returns result to admin_manager
    :param:param:
    :return:
    list of admin results
    '''
    try:
        app_response = AppResponse()
        applog.info("Country QUERY | Executing query to get all country details")
        # Listing all country details
        country_obj = session.query(table.country)
        columns_list = list(country_obj.first().keys())

        search_list = []
        keyword = param['keyword']
        search_list.append(table.country.c.country_code.ilike(f'%{keyword}%'))
        limit = param['limit']

        admin_result = country_obj.filter(*search_list).limit(limit).all()
        country_count = country_obj.filter(*search_list).limit(limit).count()
        admin_list=[]
        if admin_result:
            applog.info(f"Country QUERY | Successfully retrieved all Country details for")
            page_data = {'count': country_count, 'limit': param['limit']}
            for item in admin_result:
                res = {'country_code': item.country_code,
                       'country_name': item.country_name}
                admin_list.append(res)
            applog.info(f"Country QUERY | country Details fetched successfully ")
            app_response.set_response(200, admin_list, msg.ADMIN_DETAIL_FETCHED_SUCCESS,
                                      msg.TRUE, page_data)
        else:
            app_response.set_response(404, {}, "Failed to retrieve admin details for the given filters",
                                      msg.FALSE)

    except Exception as exp:
        applog.error(f"Exception occurred in Country QUERY: {traceback.format_exc()} \n"
                     f"exception: {exp} for {param['type']}")
        raise HTTPException(status_code=500,
                            detail={"code": 500, 'data': {}, "message": Messages.SOMETHING_WENT_WRONG, 'status': False})
    finally:
        session.close()
        return app_response


'''
This code contains a function called country_filter which fetches country details based on 
query parameters in param and returns the result to the country_manager function. I
t uses an SQL Alchemy session to query a database table called "country_table". 
The query parameters include a keyword and a limit parameter. The function returns an AppResponse 
object with the result of the query, which includes a list of country details and page data. 
It also handles exceptions and raises an HTTPException in case of an error. The code also contains
 a function called get_db, which returns a session object, and a Tables class that initializes an 
 object with a reference to the "country_table" table.
'''