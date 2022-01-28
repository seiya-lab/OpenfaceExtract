# -*- coding: utf-8 -*-
#OpenFaceを用いてビデオデータから特徴量を抽出する
import glob
import os

default_path = '/tmp/loggerstation'
# default_path = './loggerstation'
users = ['vp007', 'vp008', 'vp009', 'vp010']

############################################################################
make_cmd = '/home/openface-build/build/make'
# print(make_cmd)
os.system(make_cmd)

for user in users:
    date_dirs = os.listdir(default_path + '/' + user)
    for date_dir in date_dirs:
        video_path = os.path.join(default_path, user, date_dir, 'camera_raw.mp4') 
        out_path = os.path.join(default_path, user, date_dir)
        
        run_cmd = "/home/openface-build/build/bin/FeatureExtraction -f " + video_path + " -out_dir " + out_path + "/FaceFeature"
        print(run_cmd)
        os.system(run_cmd)
        