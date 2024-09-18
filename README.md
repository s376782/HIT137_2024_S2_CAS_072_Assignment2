# HIT137_2024_S2_CAS_072_Assignment2

--INSTALLATION--

We use Anaconda to create new Python environment for this unit: ‘hit137’ environment  

1. Install Anaconda: https://www.anaconda.com/download 

2. Launch the Anaconda Prompt 

3. Create ‘hit137’ environment with python version 3.10 using command: conda create -n hit137 python=3.10 

4. Activate ‘hit137’ environment using command: conda activate hit137 

5. Install Scipy using command: conda install scipy==1.10 requests conllu numpy joblib nmslib scikit-learn pysbd spacy 

6. Install ’en_ner_bc5cdr_md’ model using command: pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bc5cdr_md-0.5.4.tar.gz 

7. Install scispaCy using command: pip install scispacy 

8. Install Transformers (Hugging Face) using command: conda install conda-forge::transformers 

9. Install Pytorch (for BioBERT model) using command: conda install pytorch torchvision torchaudio cpuonly -c pytorch 

