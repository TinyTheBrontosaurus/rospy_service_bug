#! /usr/bin/env python

import rospy
from rospy_service_bug.srv import *
from rospy_service_bug.msg import *


class PoorlyNamedClass:
    def __init__(self):
        rospy.init_node("service_proxy_tester")
        rospy.wait_for_service('service_echo')
        rospy.wait_for_service('service_response')
        rospy.wait_for_service('service_request')
        self._service_echo = rospy.ServiceProxy('service_echo', ServiceEcho)
        self._service_response = rospy.ServiceProxy('service_response', ServiceResponse)
        self._service_request = rospy.ServiceProxy('service_request', ServiceRequest)

        self._debug_count = 0

    def echo(self):
        self._debug_count += 1
        print '{} Echo'.format(self._debug_count)
        important = CustomMessage
        important .custom_field = "Custom message that is important"
        retval = self._service_echo(important)
        print retval

    def request(self):
        self._debug_count += 1
        print '{} Request'.format(self._debug_count)
        important = CustomMessage
        important .custom_field = "Custom message that is important"
        retval = self._service_request(important)
        print retval

    def response(self):
        self._debug_count += 1
        print '{} Response'.format(self._debug_count)
        retval = self._service_response("benign request")
        print retval

def main():
    bn = PoorlyNamedClass()

    do_first = True

    # Inserting "BREAKING CODE" here will cause the problem
    # The following two lines break it, and are called "BREAKING CODE"
    #foo = CustomMessage
    #foo.custom_field = "Custom message on the callstack that should be ignored"

    #for _ in xrange(3):
    #    bn.echo()

    #for _ in xrange(3):
    #    bn.request()

    for _ in xrange(3):
        bn.response()


if __name__ == '__main__':
    main()
