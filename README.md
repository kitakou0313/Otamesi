# Otamesi

k8s+Vue+flask でつくる学習用コンテナ自動デプロイ web アプリケーション

Voyage group #サマーハッカソン制作物

技育展　ぼくのさいきょうの〇〇　登壇

**開発環境デプロイ方法**

1. リポジトリをダウンロード

2. `k8s`ディレクトリのマニフェストの mount パスを書き換える

3. `k8s\installIngress.ps1` を実行（ローカルで ingress を利用するための環境をデプロイ）

4. kubectl apply -R -f ./k8s

**紹介資料**

https://docs.google.com/presentation/d/1blVK5YSn7u9gGQ6ClBsU4RY-b98x1FxznFKHEE3CvSo/edit#slide=id.g9059ab6a2d_0_40
