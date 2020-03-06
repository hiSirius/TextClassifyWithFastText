# coding:UTF-8
import fasttext as ft
import random
import os
import sys

if __name__ == '__main__':
    #model = ft.train_supervised(input="train.txt", dim = 300,lr = 0.5,epoch=200, loss="hs",pretrainedVectors='cc.ja.300.vec')
    #train without pretrained model
    args = sys.argv
    if len(args) >1:
        if args[1] =="cc.ja.300.vec":
            print("train with pretrained model")
            model = ft.train_supervised(input="train.txt",dim = 300,lr = 0.5,epoch=200, loss="hs",pretrainedVectors='cc.ja.300.vec')
            # model.quantize(input=None,
            #       qout=False,
            #       cutoff=0,
            #       retrain=False,
            #       epoch=None,
            #       lr=None,
            #       thread=None,
            #       verbose=None,
            #       dsub=2,
            #       qnorm=False,
            #      )
            model.save_model("fasttext_with_Pretrain.model")
    else:
        print("train without pretrained model")
        model = ft.train_supervised(input="train.txt",dim = 200,lr = 0.5,epoch=200, loss="hs")
        model.quantize(input=None,
              qout=False,
              cutoff=0,
              retrain=False,
              epoch=None,
              lr=None,
              thread=None,
              verbose=None,
              dsub=2,
              qnorm=False,
             )
        model.save_model("fasttext_without_Pretrain_quantized.model")
    #results = model.test("test.txt")
    #print(results)