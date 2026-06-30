---
title: "DSPy: compilation & bootstrapping"
type: "Concept"
theme: governance-alignment-ops
level: 🔴
source_url: https://arxiv.org/abs/2310.03714
source_title: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
---

# DSPy: compilation & bootstrapping

**In one sentence** — compiling a DSPy program means letting a teleprompter automatically *bootstrap* good demonstrations by simulating the pipeline, filtering the traces that pass the metric, then selecting the best candidates — and the paper shows this process takes modest LMs from 4–20% to 49–88% accuracy on GSM8K in a few minutes.

## What the source says
**The DSPy compiler** automatically optimises any program via a teleprompter (unifying prompting and finetuning). A typical teleprompter goes through three stages:

- **Stage 1 — Candidate generation.** The compiler recursively finds all unique `Predict` modules (predictors), including nested ones. For each predictor, the teleprompter generates candidate values for its parameters: instructions, field descriptions, or — above all — *demonstrations* (input-output pairs). This iteration of DSPy focuses on demonstrations via a rejection-sampling-style approach. The simplest teleprompter, **BootstrapFewShot**, simulates a *teacher program* (or the zero-shot version of the program being compiled) on training inputs, sometimes several times at high temperature; in compile mode, the *multi-step traces* are tracked thread-safely; the metric filters the traces that help the pipeline pass, and the good examples are kept as potential demonstrations for all signatures in the program. Key finding: "LMs can be highly unreliable" but are effective at searching the solution space; a well-decomposed program generally finds a few examples passing the constraints of signatures and metrics, which allows iterative bootstrapping.
- **Stage 2 — Parameter optimisation.** Each parameter has a discrete set of candidates. Hyperparameter-tuning algorithms apply for selection: random search or Tree-structured Parzen Estimators (HyperOpt, Optuna) — hence **BootstrapFewShotWithRandomSearch** and **BootstrapFewShotWithOptuna**. Another route: **BootstrapFinetune**, where the demonstrations are used to update each predictor's *LM weights* (optimising average quality by cross-validation, possible even without any labels depending on the metric).
- **Stage 3 — Higher-order optimisation.** Modifying the control flow, notably **ensembles**: bootstrap several copies of the program, run them in parallel and reduce their predictions (e.g. majority vote). Future work: dynamic bootstrapping at test time, automatic backtracking logic.

Additional compilers mentioned: **LabeledFewShot** (samples k=8 random demonstrations from the trainset); composition of teleprompters via a `teacher` (an expensive program with a large LM can supervise a cheap program with a small LM, or finetune a T5).

**Results — GSM8K (math problems, 1.3k test).** Programs: `vanilla` (Predict), `CoT` (ChainOfThought), `reflection` (ThoughtReflection = 5 sampled chains compared by MultiChainComparison). Trainset/dev = 200/300 examples. Zero-shot (`none`), `vanilla` reaches 24.0% (dev) / 25.2% (test) for GPT-3.5 and 7.0% / 9.4% for Llama2-13b-chat. Compiling `vanilla` with `bootstrap` then `bootstrap×2` brings it to 64.7% / 61.7% (GPT-3.5) and 37.3% / 36.5% (Llama2). The paper's bottom line: **"composing the right generic modules, rather than manipulating string prompts, improves different LMs from 4–20% accuracy to 49–88% accuracy"**, with programs composing 2 to 4 modules and teleprompters. For the CoT program, `bootstrap` matches or exceeds expert human reasoning chains (`+human_CoT`); `reflection` is best. Compilation runs in minutes to tens of minutes (e.g. 10–20 trials over 150–300 validation examples, parallelisable).

**Results — HotPotQA (multi-hop QA, fullwiki, ColBERTv2 retriever over the 2017 Wikipedia dump).** Metrics: answer exact match (Ans) and pair-retrieval accuracy (Psg). `multihop` (generating queries over several "hops") is overall best; `bootstrap` exceeds few-shot (for multihop) and expert human reasoning (for react). Compiling makes **llama2-13b-chat competitive with GPT-3.5**. The `multihop_t5` compiler (BootstrapFinetune) produces a **T5-Large (770M parameters)** scoring **39.3% answer EM and 46.0% passage accuracy** on the dev set, with only **200 labelled inputs and 800 unlabelled questions**, supervised by a teacher = an ensemble of two `multihop` Llama2-13b-chat — for an inference cost orders of magnitude lower than a proprietary LM.

**Numerical summary (abstract / conclusion).** Compiled DSPy programs exceed standard few-shot "generally by over 25%" (GPT-3.5) and "65%" (Llama2-13b-chat), and pipelines with expert demonstrations "by up to 5–46%" (GPT-3.5) and "16–40%" (Llama2). Simple programs go from 33% to 82% (GSM8K) and from 32% to 46% (HotPotQA) for GPT-3.5, and from 9% to 47% then 22% to 41% for Llama2-13b-chat.

## Example
The trainset contains only question→final-answer pairs, e.g. `dspy.Example(question="What is the capital of France?", answer="Paris")` — no reasoning chain or labelled retrieved context. You call `tp = dspy.BootstrapFewShot(metric=dspy.evaluate.answer_exact_match)` then `compiled_rag = tp.compile(RAG(), trainset=qa_trainset)`. The teleprompter replays the RAG pipeline on these inputs, tracks the multi-step traces, and the metric filters those that produce "Paris": the *missing labels* (rationale, ColBERTv2 passages) are thus bootstrapped and reinjected as few-shot demonstrations into each predictor.

## Why it matters
The paper provides the three-stage mechanics (candidate generation by rejection-sampling over filtered traces → hyperparameter optimisation → higher-order/ensemble optimisation) **and the primary figures**: the 4–20% → 49–88% jumps on GSM8K, the T5-770M at 39.3% EM with 200 labels, and bringing Llama2-13b up to GPT-3.5.

## Key points
- Bootstrapping = simulate the pipeline (teacher or zero-shot), track multi-step traces, filter by metric, keep the good examples as demonstrations.
- Three stages: candidates → parameter optimisation (random search / Optuna / finetune) → higher order (ensembles, majority vote).
- GSM8K: `vanilla` zero-shot 24.0%/7.0% (dev GPT-3.5/Llama2) → `bootstrap×2` 64.7%/37.3%; global bottom line 4–20% → 49–88%.
- HotPotQA: `multihop` best; T5-Large 770M reaches 39.3% EM / 46.0% Psg with 200 labels + 800 unlabelled.
- Compiling makes Llama2-13b-chat competitive with GPT-3.5; compilation in minutes to tens of minutes, parallelisable.
- Label efficiency: labels typically required only for the final output, the rest is bootstrapped.

## See also
- [DSPy](dspy.md)
- [Prompt engineering is empirical](prompt-engineering-is-empirical.md)
- [Eval-driven development](eval-driven-development.md)
- [DSPy: signatures, modules, optimisers](dspy-signatures-modules-optimizers.md)
- [full paper](https://arxiv.org/abs/2310.03714)
