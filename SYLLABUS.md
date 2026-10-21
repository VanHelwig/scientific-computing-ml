# Scientific Computing, Data Engineering & ML — Curriculum v1.1

**Status:** Proposed revision to the existing mastery-based curriculum  
**Nominal duration:** 24 weeks, flexible pacing  
**Expected effort:** 5–7 hours/week  
**Core stack:** Python, SQL (PostgreSQL), Linux, AWS  
**Guiding principle:** Scientific reasoning and independent implementation come first; infrastructure supports the investigation.

## Goals

By the end, be able to:

1. Implement, test, profile, and explain scientific Python programs and numerical methods.
2. Ingest, validate, persist, and query real observational data using Python and SQL.
3. Apply probability, statistical inference, optimization, and time-series reasoning.
4. Train and evaluate ML models with defensible baselines, appropriate validation, and leakage controls.
5. Package reproducible software and operate a small scientific data workflow on Linux.
6. Deploy **one bounded component** on AWS, documenting security, cost, and operational behavior.
7. Present a reproducible scientific investigation with results, limitations, and a technical report.

## Working rules

- **Mastery over calendar:** Move on when the deliverable and understanding checks are satisfied; 24 weeks is a roadmap, not a deadline.
- **Independent implementation:** Attempt core algorithms, transformations, and experiments yourself. Use AI for conceptual explanations, hints, debugging discussions, and review; request complete implementations only when needed.
- **Local first:** Build and validate locally on Linux before introducing AWS.
- **Scope discipline:** No mandatory Kubernetes, Spark, Terraform, or elaborate cloud architecture.
- **Reproducibility:** Track dependencies, configuration, dataset provenance, random seeds where applicable, and repeatable commands.
- **Data integrity:** Distinguish observed time from ingestion time; document missingness, units, sampling intervals, and quality flags.

## Phase 1 — Scientific Python Foundations (Weeks 1–4)

### Week 1 — NumPy and numerical representation

- Arrays, shapes, broadcasting, indexing, vectorized operations.
- Floating-point representation, rounding error, precision, and numerical stability.
- **Deliverable:** Small NumPy-based analysis with tests for shape, dtype, and numerical edge cases.
- **Check:** Explain when approximate equality is appropriate and why exact float comparisons can fail.

### Week 2 — Visualization and exploratory computation

- Matplotlib; distributions, trends, outliers, and appropriate visual encodings.
- Reproducible notebooks versus reusable Python modules.
- **Deliverable:** Short exploratory analysis with labeled plots and an interpretation of limitations.
- **Check:** Explain what the visualizations establish—and what they cannot establish.

### Week 3 — SciPy and computational methods

- Numerical integration, interpolation, root finding, and basic optimization using SciPy.
- Compare library results against a small independently implemented method.
- **Deliverable:** Tested comparison of an original numerical implementation with SciPy.
- **Check:** Identify error sources, convergence criteria, and failure cases.

### Week 4 — Algorithms, performance, and scientific Python design

- Algorithmic complexity, memory use, vectorization versus loops, basic profiling.
- Functions, types, modules, and unit tests for scientific code.
- **Deliverable:** Reusable, tested mini-package or module with a performance note.
- **Check:** Justify a design or optimization with measurements rather than intuition alone.

## Phase 2 — Scientific Data Engineering (Weeks 5–8)

### Week 5 — Data formats, ingestion, and provenance

- CSV, JSON, Parquet; schemas, timestamps, units, identifiers, and source metadata.
- API retrieval and parsing; errors, retries, validation, and provenance.
- **Deliverable:** Python ingestion routine for a real observation source (USGS recommended).
- **Check:** Trace each stored field to its source and explain handling of missing/invalid values.

### Week 6 — pandas and relational persistence

- DataFrames, grouping, reshaping, missing data, and resampling.
- **v1.1 addition:** Persist a small normalized observational dataset in PostgreSQL.
- **v1.1 addition:** Implement one meaningful transformation both in pandas and SQL; compare semantics and tradeoffs.
- **Deliverable:** Repeatable load and transformation with checks for counts and units.
- **Check:** Explain differences in null handling, grouping, and execution location.

### Week 7 — Joins, temporal aggregation, and idempotent ETL

- Analytical SQL: joins, CTEs, window functions, temporal grouping.
- **v1.1 addition:** Idempotent ingestion using appropriate uniqueness constraints or upserts.
- **v1.1 addition:** Run ingestion and validation from a Linux command-line entry point.
- **Deliverable:** Re-running the pipeline does not duplicate observations; produce one time-window analysis query.
- **Check:** Explain row multiplication, join cardinality, and temporal alignment.

### Week 8 — Data quality and reproducible datasets

- Completeness, outliers, duplicates, temporal gaps, provenance, and quality flags.
- **v1.1 addition:** SQL-backed quality checks and a reproducible dataset extraction query.
- **Deliverable:** Data quality report plus documented, repeatable dataset build.
- **Check:** Identify ways that a technically valid dataset can still be scientifically misleading.

## Phase 3 — Mathematical & Statistical Foundations (Weeks 9–13)

### Week 9 — Linear algebra for computation

- Vectors, matrices, norms, projections, eigen concepts, and least squares.
- **Deliverable:** Solve and interpret a small least-squares problem numerically.
- **Check:** Explain conditioning and why an algebraically correct method may be numerically unstable.

### Week 10 — Probability and simulation

- Random variables, common distributions, expectation, variance, sampling.
- Monte Carlo simulation and reproducible random-number generation.
- **Deliverable:** Simulation with empirical versus theoretical comparisons.
- **Check:** Explain sampling variability and the effect of sample size.

### Week 11 — Statistical inference and uncertainty

- Estimation, confidence intervals, bootstrap, hypothesis testing, assumptions.
- **Deliverable:** Bootstrap uncertainty analysis of an observational statistic.
- **Check:** Distinguish statistical significance from practical importance.

### Week 12 — Optimization and numerical methods

- Objective functions, gradients, iterative optimization, convergence and tolerances.
- **Deliverable:** Implement and test a simple optimization routine; compare with a library method.
- **Check:** Describe when optimization fails or converges to an unhelpful result.

### Week 13 — Time-series reasoning

- Autocorrelation, trend, seasonality, stationarity, resampling, temporal dependence.
- **Deliverable:** Time-series diagnostic analysis and a defensible naive forecast baseline.
- **Check:** Explain why random train/test splitting can invalidate temporal evaluation.

## Phase 4 — ML & Experimentation (Weeks 14–18)

### Week 14 — Supervised learning fundamentals

- Regression/classification, loss functions, train/validation/test splits, simple models.
- **Deliverable:** Baseline and trained model with clear evaluation metrics.
- **Check:** Explain what the model predicts and what assumptions the experiment makes.

### Week 15 — Features, preprocessing, and model comparison

- Feature engineering, scaling, pipelines, cross-validation, error analysis.
- **v1.1 addition:** Prepare one modeling dataset from a versioned SQL query.
- **Deliverable:** Repeatable feature pipeline and comparative experiment.
- **Check:** Explain preprocessing leakage and why model comparisons need consistent splits.

### Week 16 — Evaluation and leakage control

- Generalization, temporal validation, leakage, class imbalance where relevant.
- **v1.1 addition:** Explicit SQL time bounds and verification that no future observations enter training features.
- **Deliverable:** Evaluation protocol and leakage audit.
- **Check:** Defend the evaluation design against realistic deployment conditions.

### Week 17 — Forecasting and uncertainty

- Forecast baselines, rolling-origin evaluation, appropriate error metrics, residual analysis.
- **Deliverable:** Compare at least two forecasting approaches against a naive baseline.
- **Check:** Explain when an apparently better metric is misleading.

### Week 18 — Neural network / PyTorch introduction and experimentation

- Tensors, automatic differentiation, training loops, overfitting, experiment tracking.
- **Deliverable:** Small, reproducible PyTorch experiment with a non-neural baseline.
- **Check:** Explain whether the neural approach earns its complexity.

## Phase 5 — Scientific Software & Systems (Weeks 19–21)

### Week 19 — Package design, testing, and interfaces

- Modular scientific software, type hints, pytest, CLI design, configuration, error handling.
- **Deliverable:** Package a data or modeling component with a usable CLI and tests.
- **Check:** Another person can run the software from documented instructions.

### Week 20 — Profiling, resource use, and correctness

- CPU/memory profiling, bottlenecks, vectorization, algorithmic tradeoffs; optional compiled extensions.
- **Deliverable:** Benchmark and improve one measured bottleneck without changing results unexpectedly.
- **Check:** Explain the performance/correctness tradeoff and evidence.

### Week 21 — Linux workflows and reproducibility

- Bash entry points, processes, exit codes, logging, dependency/environment management.
- **v1.1 addition:** One command or short documented sequence to run ingestion, quality checks, dataset creation, and experiments on Linux.
- **Deliverable:** Reproducibility guide with execution logs and configuration documentation.
- **Check:** Re-run from a clean environment and compare results.

## Phase 6 — Integrated Scientific Capstone (Weeks 22–24)

**Recommended capstone:** Environmental observations and forecasting using USGS data. A different scientific dataset is acceptable if it supports the same objectives.

### Week 22 — Question, dataset, and baselines

- Define a precise research question, target variable, horizon, and evaluation criteria.
- **v1.1 addition:** Use PostgreSQL for observational persistence and versioned SQL for modeling dataset extraction.
- **Deliverable:** Research plan, provenance record, exploratory analysis, baseline model, and dataset build.

### Week 23 — Models, experiments, and interpretation

- Compare appropriate methods; document uncertainty, failure modes, and limitations.
- **Deliverable:** Reproducible experiments, plots, metrics, and error analysis.
- **Check:** Explain why conclusions are or are not supported by the evidence.

### Week 24 — Packaging, report, and bounded AWS deployment

- Finalize tests, CLI, reproducibility instructions, and technical report.
- **v1.1 addition:** Deploy **one small component** to AWS: e.g., an S3 dataset/artifact store plus a scheduled Lambda ingestion step, or an appropriately sized ECS task. Select the simplest viable option.
- **v1.1 addition:** Document IAM least privilege, logs/monitoring, expected cost, and shutdown/cleanup steps.
- **Deliverable:** Working repository, reproducible local workflow, report, and limited cloud demonstration.
- **Check:** Explain the scientific results independently of the cloud infrastructure, and justify why the AWS component exists.

## Cross-cutting stack requirements

| Technology | Minimum recurring use | Depth goal |
| --- | --- | --- |
| **Python** | All phases | Independent scientific implementation, testing, profiling, software design |
| **SQL / PostgreSQL** | Weeks 6–8, 15–16, 22–24 | Relational reasoning, idempotent ingestion, temporal analytics, data integrity |
| **Linux / Bash** | Development throughout; formalized weeks 7, 19–21, capstone | Repeatable CLI execution, troubleshooting, logging, resource inspection |
| **AWS** | One capstone component | Secure, cost-conscious deployment and operations, not service memorization |

## Assessment rubric

For each phase, verify:

- **Understanding:** Can explain assumptions, algorithms, and tradeoffs without leaning on generated summaries.
- **Correctness:** Tests, sanity checks, and comparisons support the result.
- **Reproducibility:** Commands, dependencies, configuration, and data provenance are recorded.
- **Interpretation:** Can identify uncertainty, limitations, and plausible alternative explanations.
- **Scope:** Work stays aligned with the learning objective instead of accumulating unnecessary tooling.

## What changed from v1.0

```diff
+ PostgreSQL persistence and pandas-versus-SQL comparison in the data phase.
+ Idempotent SQL-backed ingestion and data quality checks.
+ Versioned SQL modeling datasets and explicit temporal leakage checks.
+ Linux/Bash reproducible entry points and execution logs.
+ One deliberately small AWS deployment in the capstone.
= Keep the 24-week, 5–7 hour/week, mastery-based structure.
= Keep mathematical reasoning, independent implementation, ML evaluation,
  and scientific interpretation as the primary goals.
- No additional mandatory cloud-native technologies or expanded cloud phase.
```

## Scope and provenance note

This v1.1 document consolidates the **working phase structure discussed in chat** and the subsequently approved-for-drafting proposed additions. It is not a line-for-line reconstruction of an original uploaded syllabus. Week-level descriptions are organized here into a usable standalone roadmap; if the original curriculum document is provided, a literal source-preserving diff can be produced.
