#! /usr/bin/env python

import rospy
from rospy_service_bug.srv import *
from rospy_service_bug.msg import *


def service_response(service_info):
    print service_info
    retval = CustomMessage
    retval.custom_field = "Custom message that is important"
    return retval

def service_request(service_info):
    print service_info
    return "benign response"


def main():
    rospy.init_node("tupac_system_performance_profiler")
    _service_echo = rospy.Service('service_echo', ServiceEcho, service_response)
    _service_response = rospy.Service('service_response', ServiceResponse, service_response)
    _service_request = rospy.Service('service_request', ServiceRequest, service_request)
    rospy.spin()

if __name__ == '__main__':
    main()
