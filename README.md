# Minify word2vec model file

`minify_w2v` make word2vec model smaller and faster to load by filtering specific vocabulary from pretrained model.

## Requirements

-   gensim
-   numpy

## Usage

```py
mw2v = MinifyW2V()
mw2v.load_word2vec("/path/to/model.txt")
mw2v.set_target_vocab(target_vocab=["cat", "dog"])
mw2v.save_word2vec("/path/to/output.bin", binary=True)
```

## Benchmark

See `ipynb/benchmark.ipynb` for details.

| Name                                 | Vocab. size | File size | Load time |
| :----------------------------------- | :---------- | :-------- | :-------- |
| `jawiki.word_vectors.200d.txt`       | 727,471     | 1.6G      | 1min 27s  |
| `jawiki.word_vectors.200d.bin`       | 727,471     | 563M      | 5.9 s     |
| `jawiki.word_vectors.200d.10000.txt` | 10,000      | 22M       | 1.18 s    |
| `jawiki.word_vectors.200d.10000.bin` | 10,000      | 7.7M      | 190 ms    |
