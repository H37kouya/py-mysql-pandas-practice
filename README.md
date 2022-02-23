# Python MySQL and Pandas Practice

## Introduction

MySQL へ接続しクエリを投げる。その結果を pandas で出力する。

## Initalize

```sh
# MySQL の初期化
bash ./scripts/init_sql.sh
```

## SQL への接続

```sh
docker compose exec db bash -c "mysql -u'tester' -p'tester' tester"
```

## Test DB

<https://github.com/datacharmer/test_db>
