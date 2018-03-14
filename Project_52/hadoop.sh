#!/bin/bash

read -p 'Type the number of iteration : ' pass
echo "The number of iteration is $pass"
read -p 'Type the path of hdfs file : ' path
echo "The hdfs path is $path"

dir_java="/usr/local/hadoop/share/hadoop/tools/lib"
version="3.0.0"

dir_wd=$(dirname $0)
echo "first initializing job starting"
hadoop jar $dir_java/hadoop-streaming-$version.jar -mapper "python $dir_wd/job1_mapper1.py" -reducer "python $dir_wd/job1_reducer1.py" -input "$path/input/data.txt" -output "$path/output1"
echo "first initializing job endinging"
for k in `seq 1 $pass`;
do
	echo "$k-th job starting"
	hadoop jar $dir_java/hadoop-streaming-$version.jar -mapper "python $dir_wd/job2_mapper1.py" -reducer "python $dir_wd/job2_reducer1.py" -input "$path/output1" -output "$path/output2"
	hdfs dfs -rmr $path/output1
	hadoop distcp $path/output2 $path/output1
	echo "first $k-th job ending"
done



