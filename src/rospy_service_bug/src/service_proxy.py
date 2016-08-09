#! /usr/bin/env python

import rospy
from rospy_service_bug.srv import *


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
        retval = self._service_1(1, "Service one request")
        print retval

    def two(self):
        self._debug_count += 1
        print '{} Two'.format(self._debug_count)
        retval = self._service_2(36, "Service two request", 867.5309)
        print retval


def main():
    bn = BadName()
    bn.one()
    bn.one()
    bn.one()
    bn.two()
    bn.two()
    bn.two()


if __name__ == '__main__':
    main()
