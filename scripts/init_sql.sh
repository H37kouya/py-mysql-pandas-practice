#!/usr/bin/env bash

# 変数の設定漏れを防止するオプション
set -u
# Alias を有効にする
shopt -s expand_aliases

alias dc='docker compose'

# ファイルが存在する現在のディレクトリのパスを取得
DIR=$(cd $(dirname $0); pwd)
EMPLOYEES_SQL_DIR=${DIR}/../resources/test_db
CONTAINER_NAME=db

dc exec $CONTAINER_NAME /bin/sh -c "cd test_db && mysql -u root -ptester < employees.sql"
