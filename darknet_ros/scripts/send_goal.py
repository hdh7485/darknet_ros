#! /usr/bin/env python
from __future__ import print_function
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import darknet_ros_msgs.msg
import cv2
from cv_bridge import CvBridge, CvBridgeError

def darknet_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('/darknet_ros/check_for_objects', darknet_ros_msgs.msg.CheckForObjectsAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    src_img = cv2.imread("/home/hdh7485/Desktop/my_video-8_406.jpg")
    bridge = CvBridge()
    ros_img = bridge.cv2_to_imgmsg(src_img, "bgr8")
    # Creates a goal to send to the action server.
    goal = darknet_ros_msgs.msg.CheckForObjectsGoal(image=ros_img)

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('darknet_client_py')
        result = darknet_client()
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
