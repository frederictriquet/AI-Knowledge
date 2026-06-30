---
title: "DSPy: signatures, modules, optimisers"
type: "Concept"
theme: governance-alignment-ops
level: 🔴
source_url: https://arxiv.org/abs/2310.03714
source_title: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
---

# DSPy: signatures, modules, optimisers

**In one sentence** — DSPy replaces hard-coded "prompt templates" with three composable abstractions — declarative *signatures*, parameterised *modules* (Predict, ChainOfThought, ReAct…) and *teleprompters* (optimisers) — so that you program an LM pipeline instead of writing prompts.

## What the source says
The paper frames DSPy as a *programming model* that treats LMs as "abstract devices for text generation" and abstracts pipelines into *text transformation graphs* (imperative computation graphs where LMs are invoked through declarative modules). It contributes three abstractions toward automatic optimisation:

- **Signatures** — a typed natural-language declaration of a function: a tuple of input and output fields (plus an optional instruction), specifying *what* to do ("consume questions and return answers") rather than *how* to prompt a specific LM. Shorthand notation `question -> answer`; field names carry the semantic role and are expanded into instructions by the compiler (`english_document -> french_translation` prompts an EN→FR translation). Advantage vs a prompt: compilable into self-improving, pipeline-adapted prompts/finetunes, plus structured formatting/parsing handling to reduce fragile string manipulation.
- **Modules** — adaptive components analogous to neural-network layers, which replace manual prompting techniques and compose into arbitrary pipelines. The core module is **Predict** (stores the signature, an optional LM, a list of demonstrations; behaves like a callable function in the style of a PyTorch layer). More sophisticated modules cited: **ChainOfThought**, **ProgramOfThought**, **MultiChainComparison**, **ReAct** — each generalising a technique from the literature (respectively Wei et al. 2022, Chen et al. 2022, Yoran et al. 2023, Yao et al. 2022) and implemented in a few lines by extending the signature and calling Predict. Example: going from `Predict` to `ChainOfThought` adds a `rationale` field ("Reasoning: Let's think step by step.") before the output. **Tools** are modules running computation: `dspy.Retrieve` (built-in support for ColBERTv2, Pyserini, Pinecone), `dspy.SQL`, `dspy.PythonInterpreter` (experimental).
- **Parameterisation** — every LM call implementing a signature specifies: (1) the LM to call, (2) the prompt instructions and the prefix of each field, (3) — most importantly — the *demonstrations* used as few-shot examples (frozen LMs) or as training data (finetuning). DSPy focuses on the automatic generation and selection of demonstrations.
- **Programs** — a *define-by-run* interface inspired by PyTorch and Chainer: declare the modules at init, then compose them in a `forward` method with arbitrary control flow (if, for, exceptions). A full RAG example in ~10 lines (`Retrieve` + `ChainOfThought("context, question -> answer")`).
- **Teleprompters** — optimisers that take a program, a trainset and a metric, and return a new optimised program. Trainsets can be small (a handful of examples), incomplete (inputs only) and without labels for intermediate steps — labels are typically assumed only for the final output. This label efficiency is critical for modularity: building a new pipeline = recompiling its code, not re-annotating. Metrics range from exact match (EM) or F1 up to entire DSPy programs.

The paper explicitly draws on the consensus around neural-network abstractions (composable layers; weights trained by optimisers rather than tuned by hand) and borrows its syntax from PyTorch. DSPy is the second iteration of the Demonstrate–Search–Predict framework (DSP, Khattab et al. 2022).

## Example
A full RAG fits in one class: `self.retrieve = dspy.Retrieve(k=3)` and `self.generate_answer = dspy.ChainOfThought("context, question -> answer")`, then in `forward(self, question)` you chain `context = self.retrieve(question).passages` before returning `self.generate_answer(context=context, question=question)`. Modularity is literal: replacing `ChainOfThought` with `Predict` is a drop-in that only changes the addition of the `rationale` field. And switching the signature from `context, question -> answer` to `context, question -> search_query` turns the module into a query generator — without touching the flow.

## Why it matters
The founding paper provides the conceptual *why*: the analogy of "hand-tuning the weights of a classifier" that makes manual prompting fragile and unscalable, and the theoretical frame of the *text transformation graph* with a define-by-run PyTorch-style interface. It also shows that each generic module (CoT, ReAct…) is a parameterised generalisation of a technique from the literature, encoded in a few lines of code rather than in hand-written prompts.

## Key points
- Three abstractions: *signatures* (declarative typed interface), *modules* (parameterised, composable prompting techniques), *teleprompters* (metric-driven optimisers).
- Shorthand notation `question -> answer`; field names encode the semantic role.
- A module = a few lines; switching `Predict` → `ChainOfThought` is a drop-in.
- Define-by-run inspired by PyTorch/Chainer: declare the modules, then compose them in `forward`.
- Label-efficient: labels required only for the final output; a new pipeline = recompile, not re-annotate.
- "Teleprompter" = abstracting and automating prompting "at a distance", without manual intervention.

## See also
- [DSPy](dspy.md) · [Prompt optimization](prompt-optimization.md)
- [DSPy: compilation & bootstrapping](dspy-compilation-bootstrap.md)
- [full paper](../../sources/dspy/md/dspy-paper.md)
