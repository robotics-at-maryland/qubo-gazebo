import pygame
import rospy
import time
from geometry_msgs.msg import Wrench
from geometry_msgs.msg import Vector3

def teleop():
    pub = rospy.Publisher('qubo_gazebo/thruster_manager/input', Wrench, queue_size=10)
    rospy.init_node('keyboard_teleop', anonymous=False)
    rate = rospy.Rate(50)
    pygame.init()
    pygame.display.set_mode([100,100])
    pygame.key.set_repeat(10,10)

    while not rospy.is_shutdown():
        fx = fy = fz = tx = ty = tz = 0
        linF = 4
        rotT = 3
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print event.key

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:
            fy = linF
        elif keys_pressed[pygame.K_s]:
            fy = -linF
        else:
            fy = 0

        if keys_pressed[pygame.K_a]:
            fx = -linF
        elif keys_pressed[pygame.K_d]:
            fx = linF
        else:
            fx = 0

        if keys_pressed[pygame.K_UP]:
            fz = linF
        elif keys_pressed[pygame.K_DOWN]:
            fz = -linF
        else:
            fz = 0

        if keys_pressed[pygame.K_LEFT]:
            tz = rotT
        elif keys_pressed[pygame.K_RIGHT]:
            tz = -rotT
        else:
            tz = 0

        if keys_pressed[pygame.K_j]:
            ty = -rotT
        elif keys_pressed[pygame.K_l]:
            ty = rotT
        else:
            ty = 0

        if keys_pressed[pygame.K_i]:
            tx = -rotT
        elif keys_pressed[pygame.K_k]:
            tx = rotT
        else:
            tx = 0

        msg = Wrench(force=Vector3(x=fx, y=fy, z=fz), torque=Vector3(x=tx, y=ty, z=tz))

        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        teleop()
    except rospy.ROSInterruptException:
        pass
