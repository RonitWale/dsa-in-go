# ML Engineer Roadmap: Uber One Target

Nov 23, 2026 · @Mr Claude

## Goal and honest framing

The target is the **Machine Learning Engineer, Uber One** role: product ML for targeting, personalization, offers and member engagement. It works on uplift models, budget-aware offer allocation, ranking, A/B testing, and production ML at Uber scale.

- **This is a different track from the AI Engineer roadmap.** That role builds products on top of LLMs. This one trains your own models on user behavior data and proves, through experiments, that they made money.
- **The hard blocker is "3+ years building and shipping production ML models."** No study plan creates that. So the plan has two steps:
  1. **By early 2028:** land an ML Engineer role on a growth, personalization or offers team at a consumer company, or move into ML internally at your current company.
  2. **About 1.5 to 2 years after that:** apply to Uber One, or similar roles at Uber, with real production ML experience.
- **Try Uber directly as a stretch in 2028.** A strong portfolio plus several years of production backend work sometimes gets an MLE II interview. Don't make your plan depend on it.
- **Your edge:** backend, APIs, AWS and Postgres. Most data scientists can't serve a model in real time or run a reliable pipeline, and you can. The JD asks for "offline development through serving, monitoring and retraining", which is half your existing job.
- **Time:** 20 focused hours a week. Weekdays 2h, weekends 5h each day.
- **DSA does not pause.** Uber's interviews lean heavily on DSA. Keep 3h a week on it all year (this repo).

## What the JD needs, and where you learn it

| JD requirement | Phase |
| --- | --- |
| Python, SQL | 1 |
| scikit-learn, XGBoost, LightGBM, PyTorch | 2, 6 |
| Experimental design, A/B testing, noisy outcomes | 3 |
| Treatment effects, uplift modeling, incrementality | 4 |
| Ranking and sequencing models, recommendation | 5 |
| Budget-aware allocation, constrained optimization | 5 |
| Spark, Hive, Presto, large-scale batch pipelines | 6 |
| Real-time serving, monitoring, retraining | 6 (and your backend background) |
| Subscription metrics: conversion, retention, LTV, cannibalization | 2, 4, capstone |
| Product mindset, cross-functional work | Every project write-up |

## Phases at a glance

| # | Phase | Months | Gate to move on |
| --- | --- | --- | --- |
| 1 | Python, SQL, math and statistics | 23 Nov 2026 to Jan 2027 | Logistic regression from scratch, plus a SQL analysis of a real dataset |
| 2 | Classical ML on tabular data | Feb to Mar 2027 | A churn or conversion model with proper validation and calibration |
| 3 | Experimentation and A/B testing | Apr to May 2027 | An A/B analysis toolkit with CUPED and a power calculator |
| 4 | Causal inference and uplift modeling | Jun to Jul 2027 | An uplift model with a Qini curve beating a response model |
| 5 | Ranking, bandits and constrained optimization | Aug to Sep 2027 | A budget-aware offer allocator, plus a ranking model |
| 6 | Scale and production ML | Oct to Dec 2027 | Capstone live: Spark batch scoring, real-time API, monitoring, retraining |
| 7 | Job search (bridge role) | Jan to Apr 2028 | Offer on a growth, personalization or offers ML team |

## Month-by-month plan

Resources are well-known picks named from general knowledge. Check they're still current before buying anything. A laptop plus free Colab or Kaggle covers almost all of this, since tabular ML doesn't need big GPUs.

### Phase 1: Python, SQL, math and statistics (23 Nov 2026 to Jan 2027)

This track needs **more statistics** than the AI Engineer one. Statistics is the language of this job.

- **Weeks 1 to 4, Python:** syntax, type hints, classes, dataclasses, comprehensions, pytest, uv. Map everything onto TypeScript. Then pandas and NumPy.
- **Weeks 3 to 8, SQL to an analyst level:** window functions, CTEs, cohort and retention queries, funnels, sessionization. Practice on Postgres. Source: DataLemur or StrataScratch SQL problems (these are asked in Uber interviews).
- **Weeks 5 to 12, math:**
  - Linear algebra and calculus basics: 3Blue1Brown's "Essence" series.
  - **Probability and statistics, in depth:** distributions, expectation and variance, the central limit theorem, confidence intervals, hypothesis tests, p-values, Bayesian basics. Source: *Practical Statistics for Data Scientists* (Bruce, Bruce and Gedeck), or the free online *OpenIntro Statistics*.
- **Ship:** logistic regression from scratch in NumPy matching scikit-learn's accuracy, plus a SQL and pandas retention and cohort analysis of a public e-commerce dataset (e.g. the Olist Brazilian e-commerce dataset on Kaggle).

### Phase 2: Classical ML on tabular data (Feb to Mar 2027)

Uber's product ML is mostly tabular data and gradient-boosted trees.

- **Core ML ideas:** bias and variance, regularization, cross-validation (including time-based splits), leakage, class imbalance, metrics (AUC, log loss, precision and recall at k), probability calibration. Source: Andrew Ng's Machine Learning Specialization (concept videos), then *Hands-On Machine Learning* (Géron), tabular chapters.
- **Gradient boosting:** XGBoost and LightGBM in depth. Hyperparameter tuning, feature importance, SHAP values for explaining models.
- **Feature engineering for user behavior:** recency, frequency, monetary value (RFM), rolling-window aggregates, target encoding.
- **Subscription metrics:** conversion, churn, retention curves, LTV, cannibalization. Read growth-team blog posts (Uber, DoorDash, Airbnb, Netflix engineering blogs).
- **Ship:** a churn or subscription-conversion model (e.g. the KKBox churn dataset on Kaggle) with time-based validation, calibration, SHAP explanations, and a write-up on **what business action** the model drives.

### Phase 3: Experimentation and A/B testing (Apr to May 2027)

Every model in this role is judged by an experiment. This phase is what separates product ML engineers from Kaggle players.

- **April, fundamentals:** randomization units, power and sample size, minimum detectable effect, multiple testing, guardrail metrics, sample ratio mismatch, novelty effects. Source: *Trustworthy Online Controlled Experiments* (Kohavi, Tang and Xu). This book is essential.
- **May, advanced:** variance reduction with **CUPED**, ratio metrics and the delta method, heavy-tailed revenue metrics, sequential testing, interference and network effects in two-sided marketplaces (switchback tests, which Uber and DoorDash write about).
- **Ship:** a small Python A/B analysis library with a power calculator, a t-test with confidence intervals, CUPED and an SRM check. Demonstrate it on simulated data and write up how much CUPED shrank the variance.

### Phase 4: Causal inference and uplift modeling (Jun to Jul 2027)

This is **the center of the Uber One role**: "who should get this offer, given that some would have subscribed anyway?"

- **June, causal inference:** potential outcomes, confounding, propensity scores, inverse propensity weighting, doubly robust estimation, difference-in-differences. Source: *Causal Inference for the Brave and True* (Matheus Facure, free online, Python), then *Causal Inference: The Mixtape* (Cunningham).
- **July, uplift modeling:** conditional average treatment effect (CATE), meta-learners (S, T, X and R learners), uplift trees and causal forests, evaluation with Qini and AUUC curves. Libraries: **CausalML** (built by Uber, so read its docs and papers closely) and EconML (Microsoft).
- **Ship:** an uplift model on the Criteo Uplift dataset or the Hillstrom email dataset. Compare T-learner, X-learner and causal forest on Qini curves, and show that targeting by uplift beats targeting by "likely to convert". Explain cannibalization in the write-up.

### Phase 5: Ranking, bandits and constrained optimization (Aug to Sep 2027)

- **August, ranking and sequencing:** learning-to-rank (pointwise, pairwise, listwise), LambdaMART with LightGBM's ranker, NDCG and MAP, two-tower retrieval basics, position bias. Then **contextual bandits** (epsilon-greedy, Thompson sampling, LinUCB) for picking which message to send next.
- **September, constrained optimization:** linear and integer programming, the knapsack problem, Lagrangian relaxation for budget constraints. Tools: PuLP or Google OR-Tools. Read Uber's and DoorDash's engineering posts on incentive and promotion allocation.
- **Ship:**
  - **Budget-aware offer allocator:** take uplift scores from Phase 4, attach a cost per offer, and solve "maximize incremental conversions with a fixed budget" with an LP. Compare against the naive "top-k by uplift" approach.
  - **Message ranker:** a LightGBM LambdaRank model that orders membership messages, plus a Thompson-sampling simulator.

### Phase 6: Scale and production ML (Oct to Dec 2027)

Your backend skills make this phase the fastest. Lean into it.

- **October, big data:** Spark and PySpark (DataFrames, joins, partitioning, skew), Hive and Presto/Trino concepts, Parquet, data lakes on S3. Source: *Learning Spark* (2nd ed.). Practice on Databricks Community Edition or local Spark.
- **November, production ML:** feature stores (offline and online consistency, training-serving skew), batch versus real-time scoring, model registry and experiment tracking with MLflow, orchestration with Airflow, monitoring (data drift, prediction drift, delayed labels), retraining triggers. Sources: Chip Huyen's *Designing Machine Learning Systems*, and Uber's Michelangelo blog posts.
- **December, PyTorch and deep models:** tensors, autograd, training loops, then a simple deep model for tabular or sequence data (e.g. predicting the next action from a user's event sequence). The JD lists PyTorch, and interviews may ask about it.
- **Ship:** the capstone (see Portfolio).

### Reading list (one a week from April)

Write a half-page summary of each in your own words.

1. Kohavi et al., "Controlled experiments on the web: survey and practical guide" (2009)
2. Deng et al., CUPED paper, "Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data" (2013)
3. Gutierrez and Gérardy, "Causal Inference and Uplift Modeling: A Review of the Literature" (2017)
4. Künzel et al., "Metalearners for estimating heterogeneous treatment effects" (X-learner, 2019)
5. Wager and Athey, "Estimation and Inference of Heterogeneous Treatment Effects using Random Forests" (2018)
6. Uber's CausalML paper (Chen et al., 2020)
7. Burges, "From RankNet to LambdaRank to LambdaMART" (2010)
8. Li et al., "A Contextual-Bandit Approach to Personalized News Article Recommendation" (LinUCB, 2010)
9. Covington et al., "Deep Neural Networks for YouTube Recommendations" (2016)
10. Uber Engineering blog: Michelangelo, experimentation platform, and marketplace incentive posts

## Portfolio projects

Six projects that together tell one story: **"I can decide who gets which membership offer, prove it worked, and run it in production."**

| Project | Phase | What it proves | Done when |
| --- | --- | --- | --- |
| 1. ML from scratch and a SQL cohort analysis | 1 | Fundamentals and analyst-level SQL | Logistic regression matches scikit-learn; a retention analysis with charts |
| 2. Subscription churn and conversion model | 2 | Tabular ML done properly | Time-based validation, calibration, SHAP, and a business-action write-up |
| 3. A/B analysis toolkit | 3 | Experiment rigor | Power calculator, CUPED and SRM check, with variance reduction measured |
| 4. Uplift model | 4 | Treatment-effect thinking | Qini curves for three methods; uplift targeting beats response targeting |
| 5. Budget-aware allocator and message ranker | 5 | Optimization and ranking | LP allocation beats top-k at equal budget; the ranker reports NDCG |
| 6. Capstone: membership offer engine | 6 | End-to-end production ML | See below |

**Capstone, the membership offer engine:** a simulated subscription business with members, trips and orders.
- Spark batch job computing features and nightly uplift scores
- An LP allocator assigning offers within a budget
- A FastAPI real-time endpoint ranking messages for each user, deployed on AWS
- MLflow registry, Airflow schedule, drift monitoring, and a retraining trigger
- A simulated A/B test that measures incremental conversions with CUPED
- A design doc written like an internal Uber proposal: problem, metrics, tradeoffs, results

## Job search

### Bridge roles (Jan to Apr 2028)

Look for ML Engineer, Applied Scientist or Data Scientist (ML) roles on **growth, personalization, offers, pricing, incentives or recommendations** teams. Consumer companies in India with this kind of work include Swiggy, Zomato, Flipkart, Meesho, PhonePe, CRED, Myntra, Dream11 and Razorpay. Check their engineering blogs to find the right teams.

- **Internal move:** ask to work on ML or experimentation in your current company. Even 6 months of shipping a production model counts as real experience.
- **Stretch:** apply directly to Uber MLE roles in Bengaluru with the capstone. Use referrals.

### Interview prep (3h a week from Oct 2027, on top of the 3h DSA)

- **DSA:** medium to hard. Uber is known for strong DSA rounds.
- **ML fundamentals:** bias and variance, regularization, trees versus linear models, calibration, metrics, leakage.
- **Statistics and experimentation:** power, p-values, CUPED, what to do when an A/B test is noisy or metrics conflict.
- **Causal and uplift:** explain uplift versus response modeling, Qini, meta-learners, cannibalization.
- **ML system design:** design a promo targeting system, a notification ranking system, or a churn-prevention system. Cover data, features, model, serving, experiments and monitoring.
- **SQL:** live window-function and funnel questions.
- **Product sense:** "Uber One renewals dropped 5%. What do you investigate?"

### Plan for the Uber role itself (2029 onward)

After about 1.5 to 2 years in a bridge role, with shipped models, experiments and measured incremental impact, apply to Uber One MLE or similar Uber roles (Eats growth, Marketplace incentives). In the interview, use the impact numbers from real work, not just projects.

## Rules

1. **Never restart from zero.** If you fall behind, continue from where you stopped.
2. **One resource at a time.** Finish or drop it.
3. **Ship ugly, then improve the one thing that would impress a hiring manager.**
4. **Every project write-up answers "what decision does this change, and how would you measure it?"** That's the product mindset the JD asks for.
5. **Sunday review, 30 minutes:** what shipped, what's blocked, next week's one goal.
6. **Choose one track.** This roadmap and the AI Engineer roadmap overlap only in Phase 1. Decide by the end of Phase 1 (Jan 2027) and stick with it.
