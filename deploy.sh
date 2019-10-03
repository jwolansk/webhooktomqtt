#!/usr/bin/env bash
docker stop mqttsender
docker rm mqttsender

BASEDIR=$(pwd)
docker run -d -p 8190:80 --name mqttsender -v $BASEDIR:/src mqttsender:latest
