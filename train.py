# coding:UTF-8
import fasttext as ft
import random
import os

if __name__ == '__main__':
    #model = ft.train_supervised(input="train.txt", dim = 300,lr = 0.5,epoch=200, loss="hs",pretrainedVectors='cc.ja.300.vec')
    #train without pretrained model
    model = ft.train_supervised(input="train.txt", dim = 300,lr = 0.5,epoch=200, loss="hs")
    model.save_model("fasttext_without_pretrain.model")
    
    results = model.test("test.txt")
    print(results)