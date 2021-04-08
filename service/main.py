import os, signal, sys
import ctypes

import cerver

from status import *
import version

from routes.service import *

status_cerver = None

# end
def end (signum, frame):
	# cerver.cerver_stats_print (status_cerver, False, False)
	cerver.http_cerver_all_stats_print (cerver.http_cerver_get (status_cerver))
	cerver.cerver_teardown (status_cerver)
	cerver.cerver_end ()
	sys.exit ("Done!")

def start ():
	global status_cerver
	status_cerver = cerver.cerver_create_web (
		"web-cerver".encode ('utf-8'), PORT, CERVER_CONNECTION_QUEUE
	)

	# main configuration
	cerver.cerver_set_receive_buffer_size (status_cerver, CERVER_RECEIVE_BUFFER_SIZE);
	cerver.cerver_set_thpool_n_threads (status_cerver, CERVER_TH_THREADS);
	cerver.cerver_set_handler_type (status_cerver, cerver.CERVER_HANDLER_TYPE_THREADS);

	cerver.cerver_set_reusable_address_flags (status_cerver, True);

	# HTTP configuration
	http_cerver = cerver.http_cerver_get (status_cerver)

	# GET /api/status
	main_route = cerver.http_route_create (cerver.REQUEST_METHOD_GET, "api/status".encode ('utf-8'), main_handler)
	cerver.http_cerver_route_register (http_cerver, main_route)

	# GET api/status/version
	version_route = cerver.http_route_create (cerver.REQUEST_METHOD_GET, "version".encode ('utf-8'), version_handler)
	cerver.http_route_child_add (main_route, version_route);

	# add a catch all route
	cerver.http_cerver_set_catch_all_route (http_cerver, status_catch_all_handler)

	# start
	cerver.cerver_start (status_cerver)

if __name__ == "__main__":
	signal.signal (signal.SIGINT, end)
	signal.signal (signal.SIGTERM, end)
	signal.signal (signal.SIGPIPE, signal.SIG_IGN)

	cerver.cerver_init ()

	cerver.cerver_version_print_full ()

	cerver.pycerver_version_print_full ()

	version.status_version_print_full ()

	status_init ()

	start ()
