# Sloth test env

## Usage

slothのテスト環境を立ち上げる．
```
$ docker-compose up -d
```

データベースの初期化を行う．

まずはappのコンテナに入る．
```
$ docker-compose exec app /bin/bash
```

初期化スクリプトを実行する．

```
root@4adfafd:/home# python init_tables.py create
```

これでデータベースコンテナにデータベースとテーブルが出来上がる．

確認
```
$ docker-compose exec database /bin/bash
root@4adfafd:/home# mysql -u sloth -p
mysql > パスワードはsloth
mysql > use test;
mysql > show tables;
```
