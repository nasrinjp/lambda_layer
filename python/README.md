Module for Lambda Layer
====

## 説明
Lambda Layerとして使用するモジュールです。
python/aws_security.py : AWS KMSから暗号化されたテキストを復号化するモジュールです。
python/backlog.py : Backlog APIをコールするモジュールです。


## Install

下記のARNをLambda Layerで指定してください。
ランタイムは Python 3.7 で動作確認しています。  

|LayerName|ARN|
|-|-|
|aws-security|arn:aws:lambda:ap-northeast-1:593649893041:layer:aws_security:1|
|backlog|arn:aws:lambda:ap-northeast-1:593649893041:layer:backlog:2|
