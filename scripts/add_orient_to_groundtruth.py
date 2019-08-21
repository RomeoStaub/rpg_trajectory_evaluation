#!/usr/bin/env python2

import os
import argparse

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

import add_path
from trajectory import Trajectory
import plot_utils as pu

rc('font', **{'family': 'serif', 'serif': ['Cardo']})
rc('text', usetex=True)

FORMAT = '.pdf'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Analyze trajectory estimate in a folder.''')
    parser.add_argument(
        'result_dir', type=str,
        help="Folder containing the groundtruth and the estimate.")
    parser.add_argument(
        '--plots_dir', type=str,
        help="Folder to output plots",
        default='')
    parser.add_argument('--recalculate_errors',
                        help='Deletes cached errors', action='store_true')
    parser.add_argument('--dataset', help='MH_01,...,MH_05', default='MH_01')

    args = parser.parse_args()

    assert os.path.exists(args.result_dir)

    plots_dir = args.plots_dir
    if not args.plots_dir:
        plots_dir = os.path.join(args.result_dir, 'plots')
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    if args.recalculate_errors:
        Trajectory.remove_cached_error(args.result_dir)


    print("Going to analyze the results in {0}.".format(args.result_dir))
    print("The plots will saved in {0}.".format(plots_dir))

    # compute the errors
    print(">>> Calculating errors...")
    traj = Trajectory(args.result_dir)

    print("args.dataset:" +str(args.dataset))
    
    # Assign an orientation estimate for the groundtruth (only used for m545)
    with open(os.path.join(plots_dir,str(args.dataset)+'_stamped_groundtruth.txt'), 'w') as f:  
        # write header
        f.write('# timestamp             tx             ty             tz             qx             qy             qz             qw  \n')
        # write each row
        for row in range(len(traj.p_gt)):
            f.write('%.12f ' %(traj.t_gt[row]))
            for col in range(len(traj.p_gt[row])):
                f.write('%.12f ' %(traj.p_gt[row][col]))
            for col in range(len(traj.q_es_aligned[row])):
                f.write('%.12f ' %(traj.q_es_aligned[row][col]))
            f.write('\n')
    with open(os.path.join(plots_dir,str(args.dataset)+'_estimate.txt'), 'w') as f:  
        # write header
        f.write('# timestamp             tx             ty             tz             qx             qy             qz             qw  \n')
        # write each row
        for row in range(len(traj.p_es)):
            f.write('%.12f ' %(traj.t_gt[row]))
            for col in range(len(traj.p_es[row])):
                f.write('%.12f ' %(traj.p_es[row][col]))
            for col in range(len(traj.q_es_aligned[row])):
                f.write('%.12f ' %(traj.q_es_aligned[row][col]))
            f.write('\n')
 

