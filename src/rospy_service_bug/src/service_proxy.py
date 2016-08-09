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
        req = Message1Req
        req.req11 = 11
        req.req12 = "Service one request message"

        cpumem_init_info = PerformanceProfileStartStruct
        cpumem_init_info.parent_by_pid = False
        cpumem_init_info.parent_pid = 0
        cpumem_init_info.parent_by_name = True
        cpumem_init_info.parent_name = 'roslaunch'
        cpumem_init_info.use_record_period = True
        cpumem_init_info.record_period = rospy.Duration(1.0)
        cpumem_init_info.roslog_outputs = False

        retval = self._service_1(1, "Service one request", req)#, cpumem_init_info)
        print retval

    def two(self):
        self._debug_count += 1
        print '{} Two'.format(self._debug_count)
        req = Message2Req
        req.req21 = 36
        req.req22 = "Service two request message"
        req.req23 = 8671.5309
        cpumem_info = PerformanceProfileStruct
        cpumem_info.performance_profile_id = int(self._debug_count)
        retval = self._service_2(36, "Service two request", 867.5309, req, cpumem_info)
        print retval


def main():
    bn = BadName()
    for _ in xrange(3):
        bn.one()

    for _ in xrange(3):
        bn.two()


if __name__ == '__main__':
    main()
