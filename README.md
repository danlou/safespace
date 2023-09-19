# 🫧 safespace - Your Local AI Counsellor

![alt text](https://github.com/danlou/safespace/blob/main/safespace_promo.png?raw=true)

**safespace** is a lightweight LLM that can run on your laptop (or desktop) to help you navigate whatever issues or concerns may be troubling you.
It's designed to be non-judgemental and support you in coming up with solutions on your own, rather than providing its own advice.

If you know about [ELIZA](https://en.wikipedia.org/wiki/ELIZA), you can think of **safespace** as its modern counterpart.

## Main Features
- **Simple**: It's just a single binary executable, no dependencies, no installation. Also, no GPU required.
- **Lightweight**: Fully conversational at only ~5GB of RAM. See [model details]().
- **Private**: Designed to be run locally and traceless - no logs, analytics, etc.
- **Transparent**: App is fully contained in the 99 lines of [safespace.py](https://github.com/danlou/safespace/blob/main/safespace.py) - have a look at what it's doing.
- **Free**: Unlimited access at no cost.

## How to use
...

## Model Details
**safespace** uses a Llama v2 7B model that has been quantized using [llama.cpp](https://github.com/ggerganov/llama.cpp) to run efficiently on CPUs.
In particular, it uses a custom fine-tuned model trained on a synthetic dataset of transcripts of therapy sessions with a Rogerian therapist. The sessions in synthetic dataset are derived from a compilation of reddit posts on subreddits related to mental health (r/ADHD, r/depression, r/Autism, ...).
We make our synthetic dataset available [here](), and the reddit dataset may be found [here](https://huggingface.co/datasets/solomonk/reddit_mental_health_posts).

Our model is fine-tuned from the [Samantha-1.11](https://huggingface.co/ehartford/Samantha-1.11-7b) model (by [@ehartford](https://x.com/erhartford)), which in turn, is a fine-tune of original Llama v2 checkpoints towards developing a companion trained on philosophy, psychology, and personal relationships.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## License
...
