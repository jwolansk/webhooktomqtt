#!/usr/bin/env bash
docker stop mqttsender
docker rm mqttsender
docker run -d -p 8190:80 --name mqttsender -v .:/src mqttsender:latest
