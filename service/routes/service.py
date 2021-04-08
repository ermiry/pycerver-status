import ctypes

import cerver

import status
import runtime
import version

# GET /api/status
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def main_handler (http_receive, request):
	response = cerver.http_response_json_msg (
		cerver.HTTP_STATUS_OK, "PyCerver Status!".encode ('utf-8')
	)

	if status.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
		cerver.http_response_print (response)
	
	cerver.http_response_send (response, http_receive)
	cerver.http_response_delete (response)

# GET /api/version
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def version_handler (http_receive, request):
	v = '%s - %s' % (version.STATUS_VERSION_NAME, version.STATUS_VERSION_DATE)

	response = cerver.http_response_json_key_value (
		cerver.HTTP_STATUS_OK, "version".encode ('utf-8'), v.encode ('utf-8')
	)

	if status.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
		cerver.http_response_print (response)
	
	cerver.http_response_send (response, http_receive)
	cerver.http_response_delete (response)

# GET *
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def status_catch_all_handler (http_receive, request):
	response = cerver.http_response_json_msg (
		cerver.HTTP_STATUS_OK, "PyCerver Status Service!".encode ('utf-8')
	)

	if status.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
		cerver.http_response_print (response)
	
	cerver.http_response_send (response, http_receive)
	cerver.http_response_delete (response)
