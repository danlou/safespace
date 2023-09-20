# 🫧 safespace

![promo](https://github.com/danlou/safespace/blob/main/safespace_promo.png?raw=true)

**safespace** is a lightweight LLM that can run on your laptop (or desktop) to help you navigate whatever personal issues or concerns may be troubling you.
It's trained to be non-judgemental and support you in coming up with solutions on your [own](https://en.wikipedia.org/wiki/Person-centered_therapy).

If you know about [ELIZA](https://en.wikipedia.org/wiki/ELIZA), you can think of **safespace** as its modern counterpart.

## Main Features
- **Simple**: It's just a single binary executable, no dependencies, no installation. Also, no GPU required.
- **Private**: Designed to be run locally and traceless - no logs, analytics, etc.
- **Lightweight**: Fully conversational at only ~5GB of RAM. See [model details]().
- **Transparent**: App is contained in the 99 lines of [safespace.py](https://github.com/danlou/safespace/blob/main/safespace.py) - have a look at what it's doing.
- **Free**: Use it as much as you want.

## How to Use
![demo](https://github.com/danlou/safespace/blob/main/safespace_demo.mp4?raw=true)

## Model Details
**safespace** uses a Llama v2 7B model that has been 4-bit quantized using [llama.cpp](https://github.com/ggerganov/llama.cpp) to run efficiently on CPUs.
In particular, it uses a custom fine-tuned model trained on a synthetic dataset of transcripts of therapy sessions with a Rogerian therapist. The sessions in synthetic dataset are derived from a compilation of reddit posts on subreddits related to mental health (r/adhd, r/depression, r/aspergers, ...).
We make our synthetic dataset available [here](), and the reddit dataset may be found [here](https://huggingface.co/datasets/solomonk/reddit_mental_health_posts).

Our model is fine-tuned from the [Samantha-1.11](https://huggingface.co/ehartford/Samantha-1.11-7b) model (by [@ehartford](https://x.com/erhartford)) which, in turn, is a fine-tune of original Llama v2 checkpoints towards developing a companion trained on philosophy, psychology, and personal relationships.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## License
The code in this repository is under the fully permissive MIT License, but the models are subject to the [Llama 2 Community License](https://github.com/facebookresearch/llama/blob/main/LICENSE).
