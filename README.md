# TextClassifyWithFastText
- What is FastText

    Library for efficient text classification and representation learning
https://fasttext.cc

## classify Japanese text with fastText

### requirement
```
mecab-python3 
fasttext
neologdn
emoji
gensim
```

### usage 
- Create the train and test data. The data the data format will be like this ```__label__XX```

     ```python pretrain.py``` 

- Train and evaluate the model.
     
     ```
     #download the pretrained vector 
     !wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ja.300.vec.gz
     #unpack it
     gzip -d cc.ja.300.vec.gz 
     #train with pretrained vector
     python train.py cc.ja.300.vec
     ```
     
     The accuracy will be improve, if you train the model with pretrained model. 
     Download the preatrained model from [here](https://fasttext.cc/docs/en/crawl-vectors.html).
     
     
- Predict the text. (example: predict.txt)

     ```python predict.py``` 
- use as API

``` nohup python server.py ```
