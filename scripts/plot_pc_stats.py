#!/usr/bin/env python2

import os
import argparse

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

import add_path
from trajectory import Trajectory
import plot_utils as pu

import rosbag

def get_vins_pc_stats(bag_file):

  bag = rosbag.Bag(bag_file)
  vins_est_cpu = []
  vins_est_mem = []
  vins_fea_cpu = []
  vins_fea_mem = []
    
  for topic, msg, t in bag.read_messages():
    if topic == "/cpu_monitor/vins_estimator/cpu":
      vins_est_cpu.append(msg.data)
    if topic == "/cpu_monitor/vins_estimator/mem":
      vins_est_mem.append(msg.data)
    if topic == "/cpu_monitor/feature_tracker/cpu":
      vins_fea_cpu.append(msg.data)
    if topic == "/cpu_monitor/feature_tracker/cpu":
      vins_fea_mem.append(msg.data)
        
  bag.close()
  
  vins_cpu = np.add(vins_est_cpu,vins_fea_cpu)
  vins_mem = np.add(vins_est_mem,vins_fea_mem)
  
#   print("vins_est_cpu: ", np.size(vins_est_cpu))
#   print("vins_est_mem: ", np.size(vins_est_mem))
#   print("vins_fea_cpu: ", np.size(vins_fea_cpu))
#   print("vins_fea_mem: ", np.size(vins_fea_mem))
#   print("vins_cpu: ", vins_cpu)


  

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Analyze PC stats of VIO''')
    parser.add_argument('--vins_bag', required=True, help='Rosbag to parse.')
    args = parser.parse_args()
    
    get_vins_pc_stats(args.vins_bag)


    
    