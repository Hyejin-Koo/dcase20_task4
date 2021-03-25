import logging
import math
import os
import pandas as pd

workspace = "/home1/irteam/users/koo/share/DB/dcase2020"
# DESED Paths
weak = os.path.join(workspace, 'dataset/metadata/train/weak.tsv')
unlabel = os.path.join(workspace, 'dataset/metadata/train/unlabel_in_domain.tsv')
synthetic = os.path.join(workspace, 'dataset/metadata/train/synthetic20/soundscapes.tsv')
validation = os.path.join(workspace, 'dataset/metadata/validation/validation.tsv')
test2018 = os.path.join(workspace, 'dataset/metadata/validation/test_dcase2018.tsv')
eval2018 = os.path.join(workspace, 'dataset/metadata/validation/eval_dcase2018.tsv')
eval_desed = os.path.join(workspace, "dataset/metadata/eval/public.tsv")
# Useful because does not correspond to the tsv file path (metadata replace by audio), (due to subsets test/eval2018)
audio_validation_dir = os.path.join(workspace, 'dataset/audio/validation')

# Wav2VecModel path (if you don't use it, None)
w2v = '/home1/irteam/users/koo/share/model/checkpoint.pt' 

# Separated data
weak_ss = None #os.path.join(workspace, 'dataset/audio/train/weak_ss/separated_sources')
unlabel_ss = None #os.path.join(workspace, 'dataset/audio/train/unlabel_in_domain_ss/separated_sources')
synthetic_ss = None #os.path.join(workspace, 'dataset/audio/train/synthetic20/separated_sources')
validation_ss = None #os.path.join(workspace, 'dataset/audio/validation_ss/separated_sources')
eval_desed_ss = None #os.path.join(workspace, "dataset/audio/eval/public_ss/separated_sources")

# Scaling data
scaler_type = "dataset"

# Data preparation
ref_db = -55
sample_rate = 16000
max_len_seconds = 10.
# features
n_window = 2048
#hop_size = 255
hop_size = 1 #sample_rate * max_len_seconds #when using w2v
n_mels = 128
max_frames = math.ceil(max_len_seconds * sample_rate / hop_size)
mel_f_min = 0.
mel_f_max = 8000.

# Model
max_consistency_cost = 2

# Training
in_memory = True
in_memory_unlab = False
num_workers = 1
batch_size = 8
noise_snr = 30

n_epoch = 200
n_epoch_rampup = 50

checkpoint_epochs = 1
save_best = True
early_stopping = None
es_init_wait = 50  # es for early stopping
adjust_lr = False
max_learning_rate = 0.001  # Used if adjust_lr is True
default_learning_rate = 0.001  # Used if adjust_lr is False

# Post processing
median_window_s = 0.45

# Classes
file_path = os.path.abspath(os.path.dirname(__file__))
classes = pd.read_csv(os.path.join(file_path, validation), sep="\t").event_label.dropna().sort_values().unique()
# Logger
terminal_level = logging.INFO
