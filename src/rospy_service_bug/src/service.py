#! /usr/bin/env python

import rospy
from rospy_service_bug.srv import *
from rospy_service_bug.msg import *


def service_1(service_info):
    print service_info
    resp = Message1Resp
    resp.resp11 = 11
    resp.resp12 = "Service one response message"
    return 1, "response of service_1", resp


def service_2(service_info):
    print service_info
    resp = Message2Resp
    resp.resp21 = 11.234
    resp.resp22 = "Service two response message"
    return 1.234, "response of service_2", resp


def main():
    rospy.init_node("tupac_system_performance_profiler")
    service_one = rospy.Service('service_1', Service1, service_1)
    service_two = rospy.Service('service_2', Service2, service_2)
    rospy.spin()

if __name__ == '__main__':
    main()
