import numpy as np
from gensim.models import KeyedVectors


class MinifyW2V():
    def __init__(self):
        pass

    def load_word2vec(self, input_path, binary=False):
        self.model = KeyedVectors.load_word2vec_format(input_path, binary=binary)
        self.vocab_set = set(self.model.index2word)

    def set_target_vocab(self, target_vocab):
        self.target_vocab = target_vocab

    def save_word2vec(self, output_path, binary=False):
        # ref. _save_word2vec_format() in gensim/models/utils_any2vec.py

        with open(output_path, "wb") as f:
            # write header
            f.write(f"{len(self.target_vocab)} {self.model.vector_size}\n".encode("utf-8"))

            for target_word in self.target_vocab:
                # get vector from model
                if target_word in self.vocab_set:
                    vector = self.model.get_vector(target_word)
                else:
                    vector = np.zeros(self.model.vector_size)

                # save file in a word2vec format
                if binary:
                    target_vector = vector.astype(np.float32).tostring()
                    f.write(target_word.encode("utf-8") + b" " + target_vector)
                else:
                    target_vector = " ".join(repr(val) for val in vector)
                    f.write(f"{target_word} {target_vector}\n".encode("utf-8"))
