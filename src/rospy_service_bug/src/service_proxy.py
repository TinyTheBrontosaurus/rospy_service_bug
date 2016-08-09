#! /usr/bin/env python

import rospy
from rospy_service_bug.srv import *
from rospy_service_bug.msg import *


class BadName:
    def __init__(self):
        rospy.init_node("service_proxy_tester")
        rospy.wait_for_service('service_1')
        rospy.wait_for_service('service_2')
        self._service_1 = rospy.ServiceProxy('service_1', Service1)
        self._service_2 = rospy.ServiceProxy('service_2', Service2)

        self._debug_count = 0

    def one(self):
        self._debug_count += 1
        print '{} One'.format(self._debug_count)
        retval = self._service_1(self._debug_count)
        print retval

    def two(self):
        self._debug_count += 1
        print '{} Two'.format(self._debug_count)
        retval = self._service_2(self._debug_count)
        print retval


def main():
    bn = BadName()

    do_first = True

    if do_first:
        for _ in xrange(3):
            bn.one()

    for _ in xrange(3):
        bn.two()

    if not do_first:
        for _ in xrange(3):
            bn.one()




if __name__ == '__main__':
    main()
