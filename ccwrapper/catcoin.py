from requests import get, post
from time import sleep
from error import CCError

class CatCoinWrapper(object):
    
    __slots__ =  ('__user_id', '__token', '__api_url')
    
    def __init__(self, user_id, token):
        '''
        :param user_id: ID Вконтакте используемый для CatCoin Api
        :param token: Токен CatCoin Api
        '''
        self.__user_id = user_id
        self.__token = token
        self.__api_url = 'likecoin2.ru/api/'
    
    def _send_request(self, params = None):
        try:
            response = post(self.__api_url, params = params, headers={})
        except Exception as err:
            raise CCError("CCWrapper: API server not available or connection problems", err)
            
        if 'error' in response:
            raise CCError("CCWrapper: Error when executing the request", response)
        return response['response']
    
    def get_transfer_history(self, tx):
        params = {
            "method": "tx",
            "merchantId": self.__user_id,
            "key": self.__token,
            "tx": [tx]
        }
        return self._send_request(params = params)
    
    def make_transfer(self, toid, amount, mark=0):
        params = {
        "method": "send",
    	"merchantId": self.__user_id,
    	"key": self.__token,
    	"toId": toid,
    	"amount": amount,
    	"markAsMerchant": mark
        }
        return self._send_request(params = params)
        
    def get_users_score(self, user_ids):
        params = {
        "method": "score",
	    "merchantId": self.__user_id,
    	"key": self.__token,
    	"userIds": user_ids
        }
        return  self._send_request(params = params)
    
    def set_shop_name(self, new_name):
        params = {
        "method": "setName",
        "merchantId": self.__user_id,
    	"key": self.__token,
    	"name": new_name
        }
        return self._send_request(params = params)
    
    def set_callback(self, callback_url):
        params = {
        "method": "set",
	    "merchantId": self.__user_id,
    	"key": self.__token,
	    "callback": callback_url
        }
        return  self._send_request(params = params)
    
    def get_lost_transfer(self):
        params = {
    	"method": "lost",
    	"merchantId": self.__user_id,
    	"key": self.__token
         }
        return  self._send_request(params = params)

class CCPoll(object):

    __slots__ = ('__api', '__LastTransactions')

    def __init__(self, ApiObject):
        self.__api = ApiObject
        self.__LastTransactions = self.__api.get_transfer_history()[0]["id"]

    def listen(self, sleep = 3):
        while True:
            history = self.__api.get_transfer_history()
            if history[0] != self.__LastTransactions:
                for payment in history:
                    if payment['id'] > self.__LastTransactions:
                        yield payment
                else:
                    self.__LastTransactions = self.__api.get_transfer_history()[0]["id"]

            sleep(sleep)