#!/bin/bash

# install A1111's stable-diffusion-webui
git clone https://github.com/suno-ai/bark
mv run.py bark/run.py
mv prompts.txt bark/prompts.txt

cd bark
pip install .

mv run.py bark/run.py
mv prompts.txt bark/prompts.txt

python run.py
