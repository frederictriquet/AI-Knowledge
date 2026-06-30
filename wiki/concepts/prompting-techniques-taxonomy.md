---
title: "Taxonomy of prompting techniques (The Prompt Report)"
type: "Concept"
theme: prompting
level: 🟡
source_url: https://arxiv.org/abs/2406.06608
source_title: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
---

# Taxonomy of prompting techniques (The Prompt Report)

**In one sentence** — the systematic, sourced version of the prompting catalog: ~58 text-based techniques classified into 5 families (ICL, Thought Generation, Decomposition, Ensembling, Self-Criticism), each attributed to its originating paper.

> Source: The Prompt Report — A Systematic Survey of Prompting Techniques, Schulhoff et al., 2024 ([full paper](../../sources/prompt-report/md/prompt-report.md), [arXiv](https://arxiv.org/abs/2406.06608)).
> The **systematic and sourced** version of the techniques catalog (~58 text-based techniques).

Text-based techniques are organized into families. For each: name (original form), a one-line description, and the author/origin as cited.

**Exact count (5 or 6?).** The text of §2.2 announces "58 text-based prompting techniques, broken into 6 major categories (Figure 2.2)", and Figure 2.2 does show six head boxes: Zero-Shot, Few-Shot, Thought Generation, Ensembling, Self-Criticism, Decomposition. **But** the report's numbered-section breakdown counts only **5 families**: Zero-Shot and Few-Shot are grouped under **In-Context Learning (ICL)** (§2.2.1, with Few-Shot in §2.2.1.2 and Zero-Shot in §2.2.1.3), the other four being Thought Generation (§2.2.2), Decomposition (§2.2.3), Ensembling (§2.2.4) and Self-Criticism (§2.2.5). This fiche adopts the section count: **5 families, Zero-Shot and Few-Shot filed under ICL** (the "6" of the figure comes from their visual separation). A technique that can belong to several families is placed in the category "of most relevance". The authors also note that the term "learn" in ICL is misleading: it can be a simple task specification.

## In-Context Learning (ICL)

ICL: the ability of generative models to learn a task from exemplars and/or instructions placed in the prompt, without updating weights (Brown et al., 2020; Radford et al., 2019).

### Few-Shot — exemplar selection and generation
- **K-Nearest Neighbor (KNN)** — selects exemplars close to the test sample to boost performance; effective but costly in time/resources (Liu et al., 2021).
- **Vote-K** — two-step selection of similar exemplars: a model proposes unlabeled candidates to annotate, then the labeled pool serves for few-shot; also guarantees diversity (Su et al., 2022).
- **Self-Generated In-Context Learning (SG-ICL)** — uses a generative model to automatically generate exemplars when training data is lacking (Kim et al., 2022).
- **Prompt Mining** — discovers the optimal "middle words" of a prompt by analyzing a large corpus, instead of the usual "Q: A:" format (Jiang et al., 2020).

### Zero-Shot
- **Role Prompting** — assigns a specific role or persona to the model (e.g. "travel writer"); also called persona prompting (Wang et al., 2023; Zheng et al., 2023).
- **Style Prompting** — specifies the desired style, tone or genre in the prompt to shape the output (Lu et al., 2023).
- **Emotion Prompting** — incorporates phrasing with human psychological weight (e.g. "This is important to my career") to improve performance (Li et al., 2023).
- **System 2 Attention (S2A)** — first asks the model to rewrite the prompt by removing irrelevant information, then submits this new prompt to obtain the answer (Weston and Sukhbaatar, 2023).
- **SimToM** — for questions involving several people/objects: establishes the set of facts known to one person, then answers solely on that basis (a two-prompt process) (Wilf et al., 2023).
- **Rephrase and Respond (RaR)** — asks the model to rephrase and expand the question before generating the final answer (Deng et al., 2023).
- **Re-reading (RE2)** — adds the sentence "Read the question again:" and repeats the question; improves reasoning on complex questions (Xu et al., 2023).
- **Self-Ask** — has the model decide whether it should ask follow-up questions; if so, it generates them, answers them, then answers the original question (Press et al., 2022).

## Thought Generation (CoT and variants)

A set of techniques pushing the model to make its reasoning explicit during solving (Zhang et al., 2023).

- **Chain-of-Thought (CoT) Prompting** — exploits few-shot to have the model express its reasoning process before the final answer; markedly improves math and reasoning (Wei et al., 2022).

### Zero-Shot CoT
- **Zero-Shot-CoT** — adds a thought-inducing sentence like "Let's think step by step.", without exemplars (Kojima et al., 2022).
- **Step-Back Prompting** — a CoT variant where the model first answers a generic high-level question about the relevant concepts before reasoning (Zheng et al., 2023).
- **Analogical Prompting** — close to SG-ICL: automatically generates exemplars including CoTs; improves mathematical reasoning and code generation (Yasunaga et al., 2023).
- **Thread-of-Thought (ThoT) Prompting** — an improved thought inducer: "Walk me through this context in manageable parts step by step, summarizing and analyzing as we go."; effective on long and complex contexts (Zhou et al., 2023).
- **Tabular Chain-of-Thought (Tab-CoT)** — a Zero-Shot CoT prompt that outputs the reasoning as a markdown table, thereby structuring the reasoning (Jin and Lu, 2023).

### Few-Shot CoT
- **Contrastive CoT Prompting** — adds exemplars with both correct AND incorrect explanations to show the model how not to reason (Chia et al., 2023).
- **Uncertainty-Routed CoT Prompting** — samples several CoT reasoning paths, keeps the majority if it exceeds a threshold, otherwise samples greedily (Google, 2023).
- **Complexity-based Prompting** — selects complex examples (length, number of steps) and does a majority vote among chains exceeding a length threshold (Fu et al., 2023).
- **Active Prompting** — has the model solve exemplars, computes uncertainty (disagreement), then has human annotators rewrite the most uncertain exemplars (Diao et al., 2023).
- **Memory-of-Thought Prompting** — builds Few-Shot CoT prompts at test time from unlabeled exemplars processed beforehand with CoT (Li and Qiu, 2023).
- **Automatic Chain-of-Thought (Auto-CoT) Prompting** — uses Wei et al.'s (2022) Zero-Shot prompt to automatically generate the chains of thought of a Few-Shot CoT prompt (Zhang et al., 2022).

## Decomposition

Decomposing complex problems into simpler sub-questions (Patel et al., 2022).

- **Least-to-Most Prompting** — first has the problem decomposed into sub-problems without solving them, then solves them sequentially, accumulating the answers (Zhou et al., 2022).
- **Decomposed Prompting (DECOMP)** — few-shot showing the model how to call functions (string splitting, internet search...); the model breaks down its problem and delegates to the functions (Khot et al., 2022).
- **Plan-and-Solve Prompting** — an improved Zero-Shot CoT prompt: "Let's first understand the problem and devise a plan... Then, let's carry out the plan and solve the problem step by step" (Wang et al., 2023).
- **Tree-of-Thought (ToT)** — creates a tree-based search problem by generating several thought-steps, evaluating their progress and deciding which to pursue; effective for search and planning (Yao et al., 2023; also Long, 2023).
- **Recursion-of-Thought** — like CoT, but each complex sub-problem encountered is sent to another call/prompt whose answer is reinserted; handles problems exceeding the context length (Lee and Kim, 2023).
- **Program-of-Thoughts** — uses Codex-type models to generate code as reasoning steps, executed by an interpreter; excels at math and programming (Chen et al., 2023).
- **Faithful Chain-of-Thought** — generates a CoT mixing natural language and symbolic language (e.g. Python), with different symbolic languages depending on the task (Lyu et al., 2023).
- **Skeleton-of-Thought** — speeds up the answer through parallelization: has a response skeleton (sub-problems) created, solved in parallel then concatenated (Ning et al., 2023).
- **Metacognitive Prompting** — a five-part prompt chain imitating human metacognition: clarification, preliminary judgment, evaluation, decision confirmation, confidence assessment (Wang and Zhao, 2024).

## Ensembling

Using several prompts for the same problem, whose answers are aggregated (often by majority vote); reduces variance but multiplies model calls.

- **Demonstration Ensembling (DENSE)** — creates several few-shot prompts, each with a distinct subset of exemplars, then aggregates their outputs (Khalifa et al., 2023).
- **Mixture of Reasoning Experts (MoRE)** — creates reasoning "experts" via specialized prompts (retrieval for factual, CoT for multi-hop/math, generated knowledge for commonsense); selects the best answer by agreement score (Si et al., 2023).
- **Max Mutual Information Method** — creates several prompt templates (varied styles and exemplars) and keeps the one maximizing the mutual information between prompt and outputs (Sorensen et al., 2022).
- **Self-Consistency** — samples several CoT reasoning paths (non-zero temperature) then does a majority vote over the answers (Wang et al., 2022).
- **Universal Self-Consistency** — like Self-Consistency but selects the majority answer by inserting all outputs into a prompt; useful for free text (Chen et al., 2023).
- **Meta-Reasoning over Multiple CoTs** — generates several reasoning chains then inserts them into a single prompt to produce the final answer (Yoran et al., 2023).
- **DiVeRSe** — creates several prompts, applies Self-Consistency to each, scores the reasoning paths step by step then selects the final answer (Li et al., 2023).
- **Consistency-based Self-adaptive Prompting (COSP)** — builds Few-Shot CoT prompts by running Zero-Shot CoT + Self-Consistency, keeping a high-agreement subset as exemplars (Wan et al., 2023).
- **Universal Self-Adaptive Prompting (USP)** — generalizes COSP to all tasks via unlabeled data and a more complex scoring function, without Self-Consistency (Wan et al., 2023).
- **Prompt Paraphrasing** — transforms a prompt by changing the vocabulary while preserving the meaning; a data augmentation technique to generate an ensemble (Jiang et al., 2020).

## Self-Criticism

Having the model criticize its own outputs, either through judgment or through feedback reinjected to improve the answer (Huang et al., 2022).

- **Self-Calibration** — after a first answer, builds a new prompt including the question, the answer and an instruction asking whether the answer is correct; useful for gauging confidence (Kadavath et al., 2022).
- **Self-Refine** — an iterative framework: the model gives an answer, produces feedback on it, then improves it, until a stopping condition (Madaan et al., 2023).
- **Reversing Chain-of-Thought (RCoT)** — has the problem reconstructed from the generated answer, compares it finely to the original to detect inconsistencies, converted into revision feedback (Xue et al., 2023).
- **Self-Verification** — generates several candidate solutions via CoT, then scores each by masking parts of the question and asking the model to predict them (Weng et al., 2022).
- **Chain-of-Verification (COVE)** — generates an answer, creates a list of verification questions, answers them, then produces the final revised answer from all of this (Dhuliawala et al., 2023).
- **Cumulative Reasoning** — generates several potential steps, has the model accept/reject them, checks whether the final answer is reached, otherwise repeats (Zhang et al., 2023).

## Takeaways (for an engineer)

- This taxonomy is **systematic and sourced** (PRISMA review, 58 techniques, each attributed to its originating paper), whereas an ad hoc catalog lists a few recipes without genealogy or provenance.
- It clearly distinguishes **families often absent from basic catalogs**: **Ensembling** (Self-Consistency, DiVeRSe, COSP/USP, MoRE...) which aggregates several answers to reduce variance, and **Self-Criticism** (Self-Refine, Chain-of-Verification, Self-Verification, RCoT...) where the model revises its own outputs.
- **Decomposition** goes well beyond Tree-of-Thought alone: Least-to-Most, DECOMP, Plan-and-Solve, Program-of-Thoughts, Skeleton-of-Thought, Recursion-of-Thought, etc. — as many explicit splitting strategies absent from a basic catalog.
- Many techniques are **composable**: Self-Consistency applies on top of CoT, COSP combines Zero-Shot CoT + Self-Consistency, DiVeRSe stacks multiple prompts + Self-Consistency + scoring.
- Several techniques are simple **text inducers** (Zero-Shot-CoT, ThoT, RE2, RaR, Plan-and-Solve): near-zero cost, worth trying first before the costly multi-call approaches (Ensembling, ToT).

## Example
The report does not stop at the catalog: §2.3 measures the actual usage of the 58 techniques by proxy of citations between papers in the dataset (assuming that a paper citing a technique probably used or evaluated it). The top-25 is dominated by Few-Shot and Chain-of-Thought, with the long tail (Tab-CoT, RCoT, USP...) remaining marginal in practice. Another concrete contribution absent from an ad hoc catalog: the PRISMA methodology and the fact that a technique belonging to several families is filed under the one "of most relevance" — which explains non-obvious classification choices (Active Prompting under Few-Shot CoT rather than under Ensembling despite its majority vote).

## See also
- [Techniques catalog](techniques-catalog.md)
- [full paper](../../sources/prompt-report/md/prompt-report.md)
