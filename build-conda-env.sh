envname=tweeterminal

conda create -n $envname python=3 -y
conda install -n $envname -c conda-forge tweepy -y
conda install -n $envname -c conda-forge dotenv -y