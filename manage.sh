#!/usr/bin/env bash

_exec=$1
_me=`readlink -f $0`
_curr_dir=`dirname $_me`

function build-api() {
  docker build -f $_curr_dir/Docker/api.Dockerfile $_curr_dir
}

$_exec
