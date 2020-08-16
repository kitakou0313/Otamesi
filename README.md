# Otamesi
k8s + Vue+flaskでつくる学習用コンテナ自動デプロイアプリケーション

開発環境デプロイ

1.リポジトリをフォーク

2.`k8s`ディレクトリのマニフェストのmountパスを書き換える

3.kubectl apply -f ./k8s

紹介資料

https://docs.google.com/presentation/d/1blVK5YSn7u9gGQ6ClBsU4RY-b98x1FxznFKHEE3CvSo/edit#slide=id.g9059ab6a2d_0_40

API test用

コンテナ作成
Invoke-WebRequest -Method GET  http://localhost:5000/servers

コンテナ削除

Invoke-WebRequest -Method DELETE  http://localhost:5000/servers
