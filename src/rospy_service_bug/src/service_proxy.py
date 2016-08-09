#! /usr/bin/env python

import rospy
from rospy_service_bug.srv import *
from rospy_service_bug.msg import *


class PoorlyNamedClass:
    def __init__(self):
        rospy.init_node("service_proxy_tester")
        rospy.wait_for_service('service_1')
        self._service_1 = rospy.ServiceProxy('service_1', Service1)

        self._debug_count = 0

    def one(self):
        self._debug_count += 1
        print '{} One'.format(self._debug_count)
        # Inserting "BREAKING CODE" here will cause the problem
        retval = self._service_1(self._debug_count)
        print retval

def main():
    bn = PoorlyNamedClass()

    do_first = True

    # Inserting "BREAKING CODE" here will cause the problem
    # The following two lines break it, and are called "BREAKING CODE"
    foo = CustomMessage
    foo.custom_field = "Custom message on the callstack that should be ignored"

    if do_first:
        for _ in xrange(3):
            bn.one()

        for _ in xrange(3):
            bn.two()

        for _ in xrange(3):
            bn.one()

    if not do_first:
        for _ in xrange(3):
            bn.two()

        for _ in xrange(3):
            bn.one()

        for _ in xrange(3):
            bn.two()


if __name__ == '__main__':
    main()
