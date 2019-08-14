#!/usr/bin/env python

import json
import yaml

with open('../config/handeye_calibration/results/calibration_optimized.json') as json_file:  
    data = json.load(json_file)
        
    #Use the new datastore datastructure
    #print data["rotation"]["i"]
    
    yaml_data ={
                    'header':
                    {
                        'frame_id': 'TELE'
                    },
                    'child_frame_id': 'CAM',
                    'transform':
                    {
                        'translation':
                        {
                          'x': float(data["translation"]["x"]),
                          'y': float(data["translation"]["y"]),
                          'z': float(data["translation"]["z"]),  
                        },
                        'rotation':
                        {
                          'x': float(data["rotation"]["i"]),
                          'y': float(data["rotation"]["j"]),
                          'z': float(data["rotation"]["k"]), 
                          'w': float(data["rotation"]["w"]),  
                        },
                         
                    }
                }
    with open('../config/tf/tf_tele_cam.yaml', 'w') as outfile:
        yaml.dump(yaml_data, outfile, default_flow_style=False)
        
        

