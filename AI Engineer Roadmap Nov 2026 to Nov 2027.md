# AI Engineer Roadmap: Nov 2026 to Nov 2027

Nov 22, 2026 · @Mr Claude

## Goal and ground rules

By November 2027, land an AI Engineer or LLM Engineer role at a big or mid-size company. You'll understand models down to the math and the code, not just call APIs.

- **What "deep" means here:** you can explain and build attention, train a small GPT, fine-tune an open model, and serve it efficiently. Then you build products on top. Most API-only AI engineers can't do this, and that's your edge.
- **What it doesn't mean:** a PhD-style research path. You stay an engineer who ships.
- **Main language:** Python, plus PyTorch. TypeScript stays as a bonus.
- **Your edge:** you already know APIs, databases, AWS (Lambda, EC2, ECR, EventBridge) and shipping to production.
- **Time:** 20 focused hours a week. Weekdays 2h, weekends 5h each day. DSA pauses until August.
- **Output rule:** every phase ends with code shipped publicly on GitHub, with a README and a short write-up.
- **Honest tradeoff:** depth makes 12 months tight. If you're more than 3 weeks behind by June, keep Phases 5 and 6 on schedule and trim paper reading, not projects.

## Phases at a glance

Seven phases, from math up to production and data pipelines. Each one gates the next: don't move on until the gate is met.

| # | Phase | Months | Gate to move on |
| --- | --- | --- | --- |
| 1 | Python and math foundations | 23 Nov 2026 to Jan 2027 | Logistic regression from scratch in NumPy, plus a deployed FastAPI service |
| 2 | ML and deep learning | Feb to Mar 2027 | Your own micrograd, plus a model trained in PyTorch |
| 3 | Transformers from the inside | Apr to May 2027 | A small GPT you built and trained yourself |
| 4 | Fine-tuning, inference and RAG | Jun to Jul 2027 | A fine-tuned open model and a RAG app, both with eval numbers |
| 5 | Agents and production | Aug to Sep 2027 | Capstone agent live on AWS |
| 6 | Job search | Aug to Nov 2027 | Offer in hand |
| 7 | Data engineering for AI | Sep 2027 to Jan 2028 | A pipeline on AWS that keeps your RAG index fresh |

Running through all of it from April: read one paper a week (see the reading list). Phase 7 runs alongside the job search, so in interviews you can say you're already learning it.

## Month-by-month plan

Resources are well-known picks named from general knowledge. Check they're still current before you buy anything. Free GPUs (Google Colab, Kaggle) cover Phases 1 to 3. Budget a small amount for rented GPUs in Phase 4.

### Phase 1: Python and math foundations (23 Nov 2026 to Jan 2027)

Learn Python fast as your second language, and the math deep learning actually uses. Intuition first, proofs never.

- **Weeks 1 to 4, Python:** syntax, type hints, classes, dataclasses, comprehensions, async, pytest, uv. Source: the official Python tutorial. Map everything onto TypeScript.
- **Weeks 3 to 10, math (in parallel):**
  - Linear algebra: vectors, matrices, matrix multiply, dot products. Source: 3Blue1Brown's "Essence of Linear Algebra".
  - Calculus: derivatives, the chain rule, gradients. Source: 3Blue1Brown's "Essence of Calculus".
  - Probability: distributions, expectation, softmax, cross-entropy.
  - Reference book: *Mathematics for Machine Learning* (Deisenroth et al., free online).
- **Weeks 5 to 10, NumPy:** write all the math in code. Vectorisation, broadcasting.
- **Weeks 11 to 12:** FastAPI and Docker, so your backend skills carry over to Python.
- **Ship:** linear and logistic regression from scratch in NumPy (gradient descent by hand), plus one FastAPI service deployed on AWS.

### Phase 2: ML and deep learning (Feb to Mar 2027)

- **Core ML ideas:** loss functions, gradient descent, train/val/test splits, overfitting, regularisation, metrics. Source: Andrew Ng's Machine Learning Specialization (concept videos only).
- **Neural nets from zero:** Karpathy's "Neural Networks: Zero to Hero", the micrograd and makemore videos. Type every line yourself.
- **PyTorch:** tensors, autograd, nn.Module, training loops, DataLoaders, GPU basics. Source: the official PyTorch tutorials, plus fast.ai's Practical Deep Learning for practice.
- **Ship:** your own micrograd, and a small model (e.g. an image or text classifier) trained in PyTorch with a proper eval.

### Phase 3: Transformers from the inside (Apr to May 2027)

- **April:** tokenization (BPE), embeddings, self-attention, multi-head attention, positional encodings, layer norm, residuals. Read "Attention Is All You Need". Watch Karpathy's "Let's build GPT" and "Let's build the GPT tokenizer".
- **May:** build and train a small GPT yourself. Source: Sebastian Raschka's *Build a Large Language Model (From Scratch)*. Then learn pretraining basics, scaling laws, and how instruction tuning and RLHF turn a base model into a chat model.
- **Also in May, model APIs:** the Anthropic and OpenAI docs. Prompting, structured outputs, streaming, tool calling. Now you'll understand why they behave the way they do.
- **Ship:** a small GPT you built and trained, plus a tool-calling assistant.

### Phase 4: Fine-tuning, inference and RAG (Jun to Jul 2027)

- **June, fine-tuning:** supervised fine-tuning, LoRA and QLoRA, preference tuning (DPO). Tools: Hugging Face transformers, PEFT, TRL. Learn when to fine-tune vs prompt vs retrieve.
- **June, inference:** the KV cache, quantization (int8/4-bit), batching, speculative decoding, serving with vLLM. Measure tokens per second and cost.
- **July, RAG done properly:** embeddings, chunking, pgvector (you know Postgres), hybrid search, rerankers, query rewriting.
- **July, evals:** golden test sets, retrieval metrics, LLM-as-judge and its failure modes. Hamel Husain's writing on evals is a good source.
- **Book alongside:** Chip Huyen's *AI Engineering* (O'Reilly).
- **Ship:** a fine-tuned open model beating a prompted baseline on your own eval, plus a RAG app with an eval report.

### Phase 5: Agents and production (Aug to Sep 2027)

- **August:** agent loops written by hand first, then one framework (LangGraph or similar). Tool design, MCP (Model Context Protocol), planning, memory, failure recovery.
- **September:** production. Tracing (Langfuse or similar), guardrails, prompt caching, cost and latency budgets, retries, model routing between a self-hosted model and an API.
- **Ship:** the capstone (see Portfolio).

### Phase 6: Job search (Aug to Nov 2027)

See the Job search section.

### Phase 7: Data engineering for AI (Sep 2027 to Jan 2028)

AI systems are only as good as their data. An engineer who can build both the model side and the data pipelines is rare and valuable.

- **September:** data modeling, advanced SQL (window functions, CTEs, on your Postgres base), batch vs streaming, ETL vs ELT, Parquet, data lakes and warehouses (S3 + Athena; Snowflake and BigQuery concepts).
- **October:** orchestration with Airflow (or Dagster), transformations with dbt, data quality tests.
- **November:** Spark (PySpark) for large data, streaming with Kafka.
- **December to January, data for AI:** ingestion pipelines for RAG with incremental re-embedding, dataset curation and cleaning for fine-tuning, feature stores, lineage.
- **Books:** *Fundamentals of Data Engineering* (Reis and Housley), then *Designing Data-Intensive Applications* (Kleppmann).
- **Hours from September:** about 7h data engineering, 8h finishing the capstone (September only, then that time goes to interviews), 3 to 5h interview prep.
- **Ship:** Project 7 (see Portfolio).

### Reading list (one paper a week from April)

Read each one, then write a half-page summary in your own words.

1. Attention Is All You Need (2017)
2. GPT-2 and GPT-3 papers (2019, 2020)
3. Scaling Laws for Neural Language Models (2020) and Chinchilla (2022)
4. InstructGPT (2022)
5. LoRA (2021) and QLoRA (2023)
6. DPO: Direct Preference Optimization (2023)
7. Retrieval-Augmented Generation (Lewis et al., 2020)
8. ReAct (2022) and Toolformer (2023)
9. FlashAttention (2022) and vLLM / PagedAttention (2023)
10. Then: whatever the top labs publish that month

## Portfolio projects

Seven projects, from the bottom of the stack to the top. Together they show you understand the whole stack, not just the API layer.

| Project | Phase | What it proves | Done when |
| --- | --- | --- | --- |
| 1. ML from scratch in NumPy | 1 | You understand gradients and loss | Logistic regression matches scikit-learn's accuracy |
| 2. micrograd + PyTorch model | 2 | You understand backprop and training | Training curves and eval in the README |
| 3. Your own small GPT | 3 | You understand transformers | Trained on a dataset you chose, generates text, write-up explains each part |
| 4. Fine-tuned open model | 4 | You can adapt and serve models | LoRA model beats a prompted baseline on your eval, served with vLLM |
| 5. RAG with evals | 4 | Retrieval and measurement | Eval report with numbers, before/after one improvement |
| 6. Production agent (capstone) | 5 | You can ship AI to production | On AWS, uses your fine-tuned model plus an API model, tracing, cost per request tracked, a design doc |
| 7. Data pipeline for AI | 7 | You can feed AI systems real data | Airflow pipeline on AWS ingests raw data, cleans it, stores Parquet on S3, and keeps the RAG index from Project 5 fresh |

Pick a domain you know for Projects 4 to 6. Geospatial and infrastructure data is a real niche, and it gives you a story in interviews.

## Job search

Applications start in August 2027. The aim is an offer by November.

- **From now on:** post a short write-up on LinkedIn whenever a project ships. By August, people should already know you as "the backend engineer building AI systems".
- **July:** rewrite your resume around Projects 1 to 3 plus your production backend experience. Title it "Backend / AI Engineer".
- **August to September:** apply to 5 to 10 roles a week. Look for titles like AI Engineer, LLM Engineer, Applied ML Engineer, ML Engineer (LLMs), or AI Platform / Inference Engineer. Your depth opens these doors, which API-only candidates can't get through. Try for referrals first.
- **Interview prep, 3h a week from August:**
  - DSA at medium level (keep the TUF+ sheet going, lighter than before)
  - AI and ML system design: design a RAG system, an agent, an eval pipeline, a fine-tuning pipeline, an LLM serving setup
  - Take-home practice: build a small LLM feature in 4 to 6 hours
  - Deep-dive questions: explain attention, the KV cache, LoRA, quantization, and why a model hallucinates. Plus tradeoffs: RAG vs fine-tuning, cost vs quality, latency
- **Plan B:** if there's no offer by November, try an internal move into AI work at your current company, which also counts as experience.

## Rules against the restart loop

The biggest risk to this plan is starting over, not falling behind.

1. **Never restart from zero.** If you miss a week, pick up exactly where you stopped. Don't redo old material "to be safe".
2. **One resource at a time.** Finish or drop it. Don't stack three courses.
3. **Ship ugly.** A working project with a messy README beats a perfect one that's never done.
4. **Learn by building.** At most 40% of the week on videos and reading, at least 60% writing code.
5. **Sunday review, 30 minutes:** what shipped, what's blocked, next week's one goal. Write it down.
6. **No switching tracks until November 2027.** New shiny thing? Note it in a "later" list and keep going.
