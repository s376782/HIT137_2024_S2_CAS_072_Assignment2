# HIT137_2024_S2_CAS_072_Assignment2

conda create -n hit137 python=3.10

conda activate hit137

conda install scipy==1.10 requests conllu numpy joblib nmslib scikit-learn pysbd spacy

pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bc5cdr_md-0.5.4.tar.gz

conda install conda-forge::transformers

conda install pytorch torchvision torchaudio cpuonly -c pytorch
