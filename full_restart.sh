#!/usr/bin/env bash
cd ~/Devel/alloydflanagan || exit
docker-compose down; rm -r assets/webpack_bundles/; npm run compile; docker-compose up --build
