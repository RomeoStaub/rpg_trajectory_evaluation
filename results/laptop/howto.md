rosrun rpg_trajectory_evaluation analyze_trajectories_new.py \
  --output_dir /home/romeo/catkin_ws/src/rpg_trajectory_evaluation/results/laptop/plots \
  --results_dir /home/romeo/catkin_ws/src/rpg_trajectory_evaluation/results/ \
  --platform laptop \
  --odometry_error_per_dataset \
  --overall_odometry_error \
  --plot_trajectories \
  --rmse_table


  --output_dir OUTPUT_DIR
                        Folder to output plots and data
  --results_dir RESULTS_DIR
                        base folder with the results to analyze
  --platform PLATFORM   HW platform: [laptop, nuc, odroid, up]
  --alg ALG             Algorithm configurations
  --dataset DATASET     [MH_01,...,MH_05,V1_01,...,V1_03,V2_01,...,V2_03, all]
  --odometry_error_per_dataset
                        Analyze odometry error for individual dataset. The
                        same subtrajectory length will be used for the same
                        dataset and different algorithms
  --overall_odometry_error
                        accumulate and analyze the odometry error over all
                        datasets. Fixed distances will be used for all
                        datasets and algorithms.
  --rmse_table          Output rms erros into latex tables
  --recalculate_errors  Deletes cached errors
  --plot_trajectories   Plot the trajectories
  --png                 Save plots as png instead of pdf
