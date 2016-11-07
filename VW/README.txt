python extract.py train-tiny.csv train_.csv

python csv2vw.py train_.csv train.vw

vw --loss_function logistic --oaa 5 -d train.vw -f model

vw --loss_function logistic --oaa 5 -i model -t -d test.vw -r raw_predictions.txt