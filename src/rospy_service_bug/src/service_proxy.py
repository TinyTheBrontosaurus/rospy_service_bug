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


# Fail case #1 is a service that has the same message in the request and the response.
# Fails immediately
def fail_case_1():
    bn = PoorlyNamedClass()
    bn.echo()


# Fail case #2 is a service where the request case succeeds, then the following response fails.
# In this one, the service throws an exception, while the ServiceProxy hangs
def fail_case_2():
    bn = PoorlyNamedClass()
    for _ in xrange(5):
        bn.request()
    bn.response()


# Fail case #3 is similar to #2, except that response is first
def fail_case_3():
    bn = PoorlyNamedClass()
    for _ in xrange(5):
        bn.response()
    bn.request()


# Fail case #4 just calls with an object in the callstack
def fail_case_4():
    bn = PoorlyNamedClass()
    # These work
    for _ in xrange(5):
        bn.request()
    foo = CustomMessage
    foo.custom_field = "Custom message on the callstack that should be ignored"
    # This one fails
    bn.response()


def main():

    fail_case = rospy.get_param("fail_case", 0)

    if fail_case is 1:
        fail_case_1()
    elif fail_case is 2:
        fail_case_2()
    elif fail_case is 3:
        fail_case_3()
    elif fail_case is 4:
        fail_case_4()


if __name__ == '__main__':
    main()
