# 🫧 safespace

![promo](https://github.com/danlou/safespace/blob/main/safespace_promo.png?raw=true)

**safespace** is a lightweight LLM that can run on your laptop (or desktop) to help you navigate whatever personal issues or concerns may be troubling you.
It's trained to be non-judgemental and support you in coming up with solutions on your [own](https://en.wikipedia.org/wiki/Person-centered_therapy).

If you know about [ELIZA](https://en.wikipedia.org/wiki/ELIZA), you can think of **safespace** as its modern counterpart.

## Main Features
- **Simple**: It's just a single binary executable, no frameworks, no installs. Also, no GPU required.
- **Private**: Designed to be run locally and traceless - no logs, analytics, etc. Runs offline.
- **Lightweight**: Fully conversational at only ~5GB of RAM. See [Model Details](#model-details).
- **Transparent**: App is contained in the 100 lines of [safespace.py](https://github.com/danlou/safespace/blob/main/safespace.py) - have a look at what it's doing.
- **Free**: Use it as much as you want.

## Video Demo
https://github.com/danlou/safespace/assets/16802508/40f2efe5-8586-40e7-a0a5-009814058138

## Quickstart

### 1. Download Binaries
Download the binary appropriate for your platform (~30MB).
- [Apple Silicon (M1/M2) chips](https://github.com/danlou/safespace/releases/download/v1.0.0-mps/safespace)
- [Linux](https://github.com/danlou/safespace/releases/download/v1.0.0-linux/safespace)
- [Windows (Soon!)](TODO)

### 2. Run Binaries
Go to the directory where the binary is located (you may move it anywhere), and type the following on your terminal.

```bash
./safespace
```

The application will search for a `safespace_models` in the same directory. If none is found, it will create it and download the default model (3.8GB) on the first run. If this download is interrupted, you will need to re-run the application with following command:

```bash
./safespace --force-download
```

You might also be able to run the binary by double-clicking on the downloaded binary file, but this hasn't been tested carefully yet.

## Running from Python

If you don't want to use the binary files, you can run **safespace** from the code in this repository. It should run faster this way, but requires some setup.

```bash
git clone https://github.com/danlou/safespace.git
cd safespace
pip install -r requirements.txt
python safespace.py
```

While this project has minimal dependencies, it may still be advisable to use a virtual environment. This installs the default llama.cpp, please check the documentation at the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python#installation-from-pypi) repository for instructions on taking advantage of platform specific optimizations (e.g. Apple Silicon). Tested on Python 3.10.

## Model Details
**safespace** uses a Llama v2 7B model that has been 4-bit quantized using [llama.cpp](https://github.com/ggerganov/llama.cpp) to run efficiently on CPUs.
In particular, it uses a custom fine-tuned model trained on a synthetic dataset of transcripts of therapy sessions with a Rogerian therapist. The sessions in synthetic dataset are derived from a compilation of reddit posts on subreddits related to mental health (r/adhd, r/depression, r/aspergers, ...).
We make our synthetic dataset available [here](), and the reddit dataset may be found [here](https://huggingface.co/datasets/solomonk/reddit_mental_health_posts).

Our model is fine-tuned from the [Samantha-1.11](https://huggingface.co/ehartford/Samantha-1.11-7b) model (by [@ehartford](https://x.com/erhartford)) which, in turn, is a fine-tune of original Llama v2 checkpoints towards developing a companion trained on philosophy, psychology, and personal relationships.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## License
The code in this repository is under the fully permissive MIT License, but the models are subject to the [Llama 2 Community License](https://github.com/facebookresearch/llama/blob/main/LICENSE).
