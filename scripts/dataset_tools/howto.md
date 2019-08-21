#Dataset tools

## Convert rovio bag to stamped_traj_estimate.txt
rostopic echo /rovio/odometry

gives the translation T_world_imu in it's odometry message.

Use the following command Extracts rovio pose messages from bagfile:
'''
python2 ~/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/rovio_bag_to_pose.py \
--output ~/git/rpg_trajectory_evaluation/results/laptop/rovio/laptop_rovio_Outdoor_01/stamped_traj_estimate.txt \
--msg_type nav_msgs/Odometry \
~/rosbags/rovio_m545_img.bag \
/rovio/odometry
'''


## Convert VINS bag to stamped_traj_estimate.txt
roslaunch m545_head vins_mono_rosbag.launch
### Extract vins pose messages from vins_result_no_loop.csv

python2 ~/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/vins_to_pose.py \
/home/integration/rosbags/VINS-mono/vins_result_no_loop.csv \
--output ~/git/rpg_trajectory_evaluation/results/laptop/vins_mono/laptop_vins_mono_Outdoor_01/stamped_traj_estimate.txt


### Extract vins pose messages from vins_result_loop.csv

python2 ~/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/vins_to_pose.py \
/home/integration/rosbags/VINS-mono/vins_result_loop.csv \
--output ~/git/rpg_trajectory_evaluation/results/laptop/vins_mono_lc/laptop_vins_mono_lc_Outdoor_01/stamped_traj_estimate.txt


## TFs to stamped_traj_estimate.txt

Transform output to odom to IMU
T_odom_IMU = T_odom_Tele * T_Tele_CAM * T_CAM_IMU

### Extract pose of tfs from rosbag of movement of excavator: T_odom_TELE

python2 ~/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/m545_tf_to_groundtruth.py \
--bag ~/rosbags/m545_tf.bag \
--tf_source_frame TELE \
--tf_target_frame odom \
--txt_output_file traj_odom_tele.txt

###  Transform textfile containing T_odom_Tele trajectory using a constant transformation T_Tele_CAM
python2 ~/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/transform_trajectory.py \
traj_odom_tele.txt \
~/catkin_ws/src/m545_head/config/tf/T_tele_cam.txt \
--output traj_odom_cam.txt

###  Transform textfile containing T_Tele_CAM trajectory using a constant transformation T_CAM_IMU
python2 ~/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/transform_trajectory.py \
traj_odom_cam.txt \
~/catkin_ws/src/m545_head/config/tf/T_cam_imu.txt \
--output traj_odom_imu.txt

## Extract pose of leica rosbag of movement of excavator: T_odom_TELE


## ROS tf
rosrun tf tf_echo world imu

The output of tf echo is the target frame represented in the reference frame. 
rosrun tf tf_echo [reference_frame] [target_frame]

T_ref_target

T_t1_t2 = T_t1_w * T_w_t2
\large{$$\mathbf{T}_{turtle1\_turtle2} =\mathbf{T}_{turtle1\_world} *\mathbf{T}_{world\_turtle2}$$} :

rosrun tf tf_echo turtle1 turtle2

E.g. to get the transformation from world to imu, type
rosrun tf tf_echo world imu

T_world_imu

Align Ground truth to IMU:
Get first translationionslationionn_{world\_turtle2}$$} :

rosrun tf tf_echo turtle1 turtle2

E.g. to get the transformation from world to imu, type
rosrun tf tf_echo world imu

T_world_imu

Align Ground truth to IMU:
Get first translationionslationionn
