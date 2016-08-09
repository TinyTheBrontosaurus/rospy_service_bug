#! /usr/bin/env python

import rospy
from rospy_service_bug.srv import *
from rospy_service_bug.msg import *


def service_1(service_info):
    print service_info
    retval = CustomMessage
    retval.custom_field = "Custom message that is important"
    return retval


def main():
    rospy.init_node("tupac_system_performance_profiler")
    service_one = rospy.Service('service_1', Service1, service_1)
    rospy.spin()

if __name__ == '__main__':
    main()
