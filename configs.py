import abc
import os


class Config:
    BASE_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    VOCABS_DIR = os.path.join(DATA_DIR, 'vocabs')
    CHECKPOINTS_DIR = os.path.join(DATA_DIR, 'checkpoints')


class UniEnViConfig:
    PROBLEM = 'uni_en_vi'
    MODEL = 'transformer'
    CHECKPOINT_PATH = os.path.join(Config.CHECKPOINTS_DIR, 'unienvi', 'model.ckpt-best')
    VOCAB_DIR = Config.VOCABS_DIR
    HPARAMS = 'transformer_base_single_gpu'


class UniViEnConfig:
    PROBLEM = 'uni_vi_en'
    MODEL = 'transformer'
    CHECKPOINT_PATH = os.path.join(Config.CHECKPOINTS_DIR, 'univien', 'model.ckpt-best')
    VOCAB_DIR = Config.VOCABS_DIR
    HPARAMS = 'transformer_base_single_gpu'



