#!/usr/bin/env bash

ls | xargs -P10 -n1 -i% bash -c "./%"
