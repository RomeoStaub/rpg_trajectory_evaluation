python /home/romeo/git/rpg_trajectory_evaluation/scripts/dataset_tools/tf_to_txt.py --bag /home/romeo/calib_ws/src/hand_eye_calibration/datasets/robot_arm/data/robot_arm_complete_bag_color_and_ir.bag --tf_source_frame sr300_rgb_optical_frame --tf_target_frame base_link --txt_output_file /home/romeo/git/rpg_trajectory_evaluation/results/robot_arm/stamped_groundtruth.txt


Extract pose of tfs from rosbag of movement of excavator

python2 /home/romeo/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/heap_tf_to_groundtruth.py \
--bag ../data/robot_arm_sim_color.bag \
--tf_source_frame BASE \
--tf_target_frame IMU \
--csv_output_file tf_poses_timestamped.csv

Extracts rovio pose messages from bagfile

python2 /home/romeo/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/rovio_bag_to_pose.py \
--output stamped_traj_estimate.txt \
--msg_type nav_msgs/Odometry \
/home/romeo/catkin_ws/src/heap_vio/rosbags/rovio/rovio_test_25_4_6_1_0.bag \
/rovio/odometry


Extract vins pose messages from vins_result_no_loop.csv

python2 /home/romeo/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/vins_to_pose.py \
/home/romeo/git/VINS-Mono/output/vins_result_no_loop.csv \
--output /home/romeo/git/rpg_trajectory_evaluation/results/laptop/stamped_traj_estimate.txt


Extract vins pose messages from vins_result_loop.csv

python2 /home/romeo/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/vins_to_pose.py \
/home/romeo/git/VINS-Mono/output/vins_result_loop.csv \
--output /home/romeo/git/rpg_trajectory_evaluation/results/laptop/lc/stamped_traj_estimate.txt



Test vins mono vs. vins mono lc

python2 /home/romeo/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/vins_to_pose.py \
/home/romeo/git/VINS-Mono/output/vins_result_no_loop.csv \
--output /home/romeo/git/rpg_trajectory_evaluation/results/vins_mono/stamped_traj_estimate.txt


python2 /home/romeo/catkin_ws/src/rpg_trajectory_evaluation/scripts/dataset_tools/vins_to_pose.py \
/home/romeo/git/VINS-Mono/output/vins_result_loop.csv \
--output /home/romeo/git/rpg_trajectory_evaluation/results/vins_mono/stamped_groundtruth.txt




