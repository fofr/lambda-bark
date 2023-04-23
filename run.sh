#!/bin/bash

git clone https://github.com/suno-ai/bark
mv run.py bark/run.py
mv prompts.txt bark/prompts.txt

cd bark
pip install .
sleep 2
pip install .
python run.py
