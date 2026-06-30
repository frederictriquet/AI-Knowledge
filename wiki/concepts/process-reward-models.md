---
title: "Process Reward Models (Let's Verify Step by Step)"
type: "Concept"
theme: reasoning-planning
level: 🔴
source_url: https://arxiv.org/abs/2305.20050
source_title: "Let's Verify Step by Step"
---

# Process Reward Models (Let's Verify Step by Step)

> ⚠️ Sheet built from the **abstract** (the LaTeXML HTML of this paper is unavailable on arXiv; see [md](../../sources/frontier-reasoning/md/verify-step-by-step.md)).

**In one sentence** — rewarding each intermediate reasoning step (process supervision) trains markedly more reliable models than rewarding only the final answer (outcome supervision).

## What the source says
Large language models have improved substantially at multi-step reasoning, but even the best ones still regularly make logical errors. To train more reliable models, one can use either outcome supervision, which provides a signal only on the final result, or process supervision, which provides a signal on each intermediate reasoning step. The authors compare the two and find that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Their process-supervised model solves 78% of a representative subset of the MATH test set. They further show that active learning markedly improves the efficiency of process supervision. To support research, they release PRM800K, the full set of 800,000 step-level human feedback labels.

## Example
On a combinatorics solution (generator pass-rate 18.5%), the generator claims at step 9 that there are "5 ways" to swap a same-colored marble — true on the surface, but undercounting by a factor of 2 (Bob has 2 choices of marble to return). The PRM is fooled: a localized *false positive*. Conversely, on a problem that is in fact easy (pass-rate 93.5%), the PRM catches step 7 where an erroneous simplification slips in. This per-step granularity — green if correct, red if faulty — is exactly what an ORM, judging only the final answer, cannot produce.

## Why it matters
This paper introduces a Process Reward Model (PRM) that scores each reasoning step, laying the groundwork for aligning and evaluating reasoning models. For agents that must reason over multiple steps, this offers a reliability lever (detecting where the reasoning goes off the rails) that mere result-checking cannot provide.

## Key points
- **Process vs outcome supervision**: score each reasoning step, not just the final answer.
- Process supervision **significantly outperforms** outcome supervision on the MATH dataset.
- PRM model: **78%** success on a representative subset of the MATH test.
- **Active learning** improves the efficiency of process supervision.
- **PRM800K**: 800,000 step-level human labels, released to the community.
- **Use**: a PRM then guides search (*verified* best-of-N, reasoning tree) or serves to train the model. Key distinction: the *Outcome Reward Model* (ORM) judges only the result and sometimes rewards a wrong reasoning that happens to land correctly; the PRM gives a dense, localized signal.
- **Cost/risk**: per-step annotation is expensive, and there is a risk of *reward hacking* on the intermediate scoring.

## See also
- [Test-time compute](test-time-compute-thinking.md)
- [DeepSeek-R1: RL makes reasoning emerge](deepseek-r1-rl-reasoning.md)
- [paper](../../sources/frontier-reasoning/md/verify-step-by-step.md)
