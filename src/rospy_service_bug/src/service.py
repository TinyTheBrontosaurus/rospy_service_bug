#! /usr/bin/env python

import rospy
from rospy_service_bug.srv import *
from rospy_service_bug.msg import *


def service_1(service_info):
    print service_info
    #retval = PerformanceProfileStruct
    #retval.performance_profile_id = 1
    #retval.dummy = 8
    return 8


def service_2(service_info):
    print service_info
    return 1.234


def main():
    rospy.init_node("tupac_system_performance_profiler")
    service_one = rospy.Service('service_1', Service1, service_1)
    service_two = rospy.Service('service_2', Service2, service_2)
    rospy.spin()

if __name__ == '__main__':
    main()
