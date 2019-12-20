#! /usr/bin/env python
import rospy
from ast import literal_eval
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import os


class terminate(object):

    def __init__(self):
        self.target = ""
        self.position = ""
        self.probabilityThreshold = 0.80
        # Subscriber to get Target Position
        self._hunter = rospy.Subscriber('/drone_hunter_topic', String, self.get_target_location)
        self.terminateIt()

    # Subscriber callback for Target Position Information
    def get_target_location(self, msg):
        # rospy.loginfo(msg)
        if msg.data != "-999":
            self.target = literal_eval(msg.data);
            if type(self.target) is not dict:
                self.target = self.target[0]
        if msg.data == "-999":
            self.target = ""

    # Function to Publish data to the publisher
    def terminateIt(self):
        while not rospy.is_shutdown():
            rospy.loginfo("Standing By")
            if (self.target != "" and self.target["prob"] > self.probabilityThreshlold):
                # terminated
                os.system("./kill.sh")
                break


if __name__ == "__main__":
    rospy.init_node('terminator', log_level=rospy.INFO)
    go_home_object = terminate()
    rospy.spin()
