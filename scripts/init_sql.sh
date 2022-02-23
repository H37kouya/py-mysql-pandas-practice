#!/usr/bin/env bash

# 変数の設定漏れを防止するオプション
set -u
# Alias を有効にする
shopt -s expand_aliases

alias dc='docker compose'

# ファイルが存在する現在のディレクトリのパスを取得
CONTAINER_NAME=db

dc exec $CONTAINER_NAME /bin/sh -c "cd test_db && mysql -u root -ptester < employees.sql"
