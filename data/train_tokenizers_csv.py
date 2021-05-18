"""
Train different tokenizers on all item names.
"""

import os
import pandas as pd
from tokenizers import Tokenizer
from tokenizers.models import BPE, WordPiece, Unigram
from tokenizers.normalizers import Lowercase
from tokenizers.pre_tokenizers import Whitespace, Digits, Sequence
from tokenizers.trainers import BpeTrainer, WordPieceTrainer, UnigramTrainer


TRAIN_DATA_PATH = 'data/pretrain.csv'
OUTPUT_PATH = 'data/tokenizers/'

# Prepare data
train = pd.read_csv(TRAIN_DATA_PATH)

item_names_0 = train.text.drop_duplicates().tolist() 
item_names = []
for text in item_names_0:
    item_names += [ str(text) ]
print( 'item_names = ', item_names )


# WordPiece tokenizer
tokenizer = Tokenizer(WordPiece(unk_token="[UNK]"))
tokenizer.pre_tokenizer = Sequence([Whitespace(), Digits()])
tokenizer.normalizer = Lowercase()

trainer = WordPieceTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
                           vocab_size=2300)
tokenizer.train_from_iterator(item_names, trainer)
tokenizer.save(os.path.join(OUTPUT_PATH, 'wordpiece_3600.json'))


# BPE tokenizer
tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
tokenizer.pre_tokenizer = Sequence([Whitespace(), Digits()])
tokenizer.normalizer = Lowercase()

trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
                     vocab_size=20000)
tokenizer.train_from_iterator(item_names, trainer)
tokenizer.save(os.path.join(OUTPUT_PATH, 'bpe_3300.json'))


# Unigram tokenizer
tokenizer = Tokenizer(Unigram())
tokenizer.pre_tokenizer = Sequence([Whitespace(), Digits()])
tokenizer.normalizer = Lowercase()

trainer = UnigramTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
                         vocab_size=17000)
tokenizer.train_from_iterator(item_names, trainer)
tokenizer.save(os.path.join(OUTPUT_PATH, 'unigram_3000.json'))
