import cerver.utils

STATUS_VERSION = "0.1"
STATUS_VERSION_NAME = "Version 0.1"
STATUS_VERSION_DATE = "05/04/2021"
STATUS_VERSION_TIME = "10:14 CST"
STATUS_VERSION_AUTHOR = "Erick Salas"

def status_version_print_full ():
	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"\nPyCerver Status Version: %s".encode ('utf-8'), STATUS_VERSION_NAME.encode ('utf-8')
	)

	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"Release Date & time: %s - %s".encode ('utf-8'),
		STATUS_VERSION_DATE.encode ('utf-8'), STATUS_VERSION_TIME.encode ('utf-8')
	)

	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"Author: %s\n".encode ('utf-8'),
		STATUS_VERSION_AUTHOR.encode ('utf-8')
	)

def status_version_print_version_id ():
	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"\nPyCerver Status Version ID: %s\n".encode ('utf-8'),
		STATUS_VERSION.encode ('utf-8')
	)

def status_version_print_version_name ():
	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"\nPyCerver Status Version: %s\n".encode ('utf-8'),
		STATUS_VERSION_NAME.encode ('utf-8')
	)