sudo apt-get update

sudo apt install openjdk-8-jdk

wget http://apache.forsale.plus/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz

tar spark-2.4.5-bin-hadoop2.7.tgz  
sudo mv spark-2.4.5-bin-hadoop2.7 /spark
rm spark-2.4.5-bin-hadoop2.7.tgz 

echo 'export SPARK_HOME=/spark'>>.bashrc 

echo 'export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin'>>.bashrc
