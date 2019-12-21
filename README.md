# TextClassifyWithFastText
- What is FastText

    Library for efficient text classification and representation learning
https://fasttext.cc

## classify Japanese text with fastText
### usage 
- Create the train and test data. The data the data format will be like this ```__label__XX```

     ```python pretrain.py``` 

- Train and evaluate the model. 

     ```python train.py```
     
     The accuracy will be improve, if you train the model with pretrained model. 
     Download the preatrained model from [here](https://fasttext.cc/docs/en/crawl-vectors.html).
     
     
- Predict the text. (example: predict.txt)

     ```python predict.py``` 
