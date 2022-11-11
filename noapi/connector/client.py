import requests, pydantic




class Connection:
	def __init__(self, address: str, port: int):
		"""
		Connection to a NoApi server

		:param address: address/ip of the server
		:param port: a unique port for your program (use the same one on server)
		"""
		self.short_address = address
		self.server_address = f"http://{address}:{port}"  # TODO figure out https
		self.session = requests.Session()


	def connect(self):
		self.call_server('post', 'connect')

	# def disconnect  # TODO


	def call_server(self, method: str, function: str, data=None, **params) -> dict | list:
		method = getattr(self.session, method)
		url = f'{self.server_address}/{function}'
		response = method(url, json=data, params=params)
		json = response.json()

		match response.status_code:
			case 200:
				return json
			case 403:
				raise NotConnectedError(response)
			case 404:
				raise ObjectNotFoundError(response)
			case 500:
				raise ServerError(response)
			case _:
				raise InternalNoApiError(response)


	def test(self):
		try:
			self.call_server('get', 'test')
			return True
		except:
			return False


	def __eq__(self, other):
		if isinstance(other, Connection):
			return self.server_address == other.server_address

	def __hash__(self):
		return hash(self.server_address)




# class Connection(BaseConnection):
# 	def call_server(self, method: str, function: str, data=None, **params):
# 		json = super().call_server(method, function, data, **params)
#
# 		if isinstance(json, dict):
# 			return parse(json)
# 		elif isinstance(json, list):
# 			return [parse(i) for i in json]






class _NoApiError(BaseException):
	message: str

	def __init__(self, server_response: requests.Response):
		super().__init__(f"{self.message} ({server_response.json()['detail']})")


class NotConnectedError(_NoApiError):
	message = "Not connected to server"


class ObjectNotFoundError(_NoApiError):
	message = "object not found on server"


class ServerError(_NoApiError):
	message = "error occured on server"


class InternalNoApiError(_NoApiError):
	def __init__(self, response: requests.Response):
		self.message = f"Internal error with NoApi server - {response.status_code}"
		super().__init__(response)