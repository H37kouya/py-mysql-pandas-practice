#!/usr/bin/env bash

# 変数の設定漏れを防止するオプション
set -u
# Alias を有効にする
shopt -s expand_aliases

alias dc='docker compose'

# ファイルが存在する現在のディレクトリのパスを取得
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONTAINER_NAME=db
INIT_SQL_FILE=${DIR}/init.sql

dc exec $CONTAINER_NAME /bin/sh -c "cd test_db && mysql -u root -ptester < employees.sql"

dc cp $INIT_SQL_FILE $CONTAINER_NAME:/init.sql
dc exec db /bin/sh -c 'mysql -u root -ptester < /init.sql'
