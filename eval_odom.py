# Copyright (C) Huangying Zhan 2019. All rights reserved.

import argparse

from kitti_odometry import KittiEvalOdom

parser = argparse.ArgumentParser(description='KITTI evaluation')
parser.add_argument('--result', type=str, required=True, help="Result directory")
parser.add_argument('--source', type=str, help="Source directory")
parser.add_argument('--align', type=str,  choices=['scale', 'scale_7dof', '7dof', '6dof'], default=None, help="alignment type")
parser.add_argument('--seqs', nargs="+", type=int, help="sequences to be evaluated", default=None)
args = parser.parse_args()

eval_tool = KittiEvalOdom()
gt_dir = "dataset/kitti_odom/gt_poses/"

# continue_flag = input("Evaluate result in {}? [y/n]".format(result_dir))

# if continue_flag == "y":
eval_tool.eval(gt_dir, result_dir = args.result, source_dir=args.source, alignment=args.align, seqs=args.seqs,)
# else:
    # print("Double check the path!")

# python eval_odom.py --result result/test --source source/test  --align 7dof
# python eval_odom.py --result result/test  --align 7dof