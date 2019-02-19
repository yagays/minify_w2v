# Minify word2vec model file
`minify_w2v` make word2vec model smaller and faster to load by filtering specific vocabulary from pretrained model.

## Requirements

- gensim
- numpy

## Usage

```
mw2v = MinifyW2V()
mw2v.load_word2vec("/path/to/model.txt")
mw2v.set_target_vocab(target_vocab=["cat", "dog"])
mw2v.save_word2vec("/path/to/output.bin", binary=True)
```
