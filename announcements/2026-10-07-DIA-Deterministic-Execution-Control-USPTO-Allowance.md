# DIA: Deterministic Execution Control for Generative AI

**Grounded DI LLC · October 7, 2026**  
**U.S. Patent Application No. 19/716,065 · All 30 claims allowed · Patent not yet issued**

Generative AI produces candidate outputs. DIA governs whether a model-interface operation is authorized and whether a candidate output may transition to a committed output state.

Grounded DI’s Deterministic Intelligence Architecture places deterministic controls at two consequential points: before model-interface execution and before output commitment. Together, those controls form an execution-control layer around probabilistic generation.

## How the architecture works

DIA connects authorization, bounded execution, validation, and delivery through an ordered control architecture:

1. **Establish governing state.** Construct or select a deterministic logic-state object containing machine-readable rules, authorized logic paths, and a causal-path identifier.
2. **Authorize execution.** Evaluate causal rule gates. Generate model-interface authorization only when the required gates are satisfied; prevent the model-interface operation otherwise.
3. **Bound the model operation.** Associate the model-interface instruction with that authorization and constrain the operation according to the governing causal path.
4. **Validate the candidate.** Identify the candidate output, validate it, and assign a validation state.
5. **Control commitment.** Determine the delivery-control state. Permit transition from an uncommitted candidate to a committed output only when the predefined commitment condition is satisfied.
6. **Preserve traceability.** Generate trace, replay, or audit metadata linking the governing logic state, causal path, authorization, candidate output, validation state, and delivery-control state.

**Producing a candidate does not itself authorize its commitment.**

The architecture makes permission to execute and permission to commit explicit, state-bound decisions. Trace, replay, or audit metadata can preserve the relationship between those decisions and the resulting output.

## USPTO allowance

On October 7, 2026, the United States Patent and Trademark Office mailed a Notice of Allowance for Application No. 19/716,065.

The Examiner states:

> “Claims 1-30 are allowed over prior art of record.”

The Reasons for Allowance identify the ordered combinations in independent claims 1, 2, and 3—including gate-conditioned model authorization, bounded model operations, validation-dependent delivery control, and conditional output commitment—as not taught or fairly suggested by the prior art of record, considered with the remaining claim limitations.

The Examiner further states:

> “The claimed subject matters are novel and non-obvious in scope over the prior art of record”

These findings provide the examination basis for allowance of the claimed architecture.

## Application record

| Item | Detail |
| --- | --- |
| Application | 19/716,065 |
| Inventor | Mark S. Weinstein |
| Nonprovisional filed | June 22, 2026 |
| Earliest provisional priority claimed | June 19, 2025 — No. 63/826,922 |
| DIA provisional | June 30, 2025 — No. 63/832,494 |
| Notice of Allowance mailed | October 7, 2026 |
| Claims allowed | 1–30 |
| Status | Allowed; patent not yet issued |

**Priority note:** The application claims priority to provisional application No. 63/826,922, filed June 19, 2025. The provisional expressly titled for the Deterministic Intelligence Architecture (DIA) Engine was filed June 30, 2025 as No. 63/832,494. Entitlement to an earlier effective filing date remains dependent on support for the particular claimed subject matter; the existence of the June 19 priority claim should not be read as establishing that every later DIA limitation or combination is necessarily entitled to that date.

**Official invention title:** Deterministic Intelligence Systems and Methods for Pre-Commitment Logic-State Authorization, Model-Interface Governance, Audit-Traceable Validation, and Controlled Delivery of Generative Artificial Intelligence Outputs.

**Source:** USPTO Notice of Allowance, Notice of Allowability, and accompanying Reasons for Allowance dated October 7, 2026. The USPTO record identifies Application No. 19/716,065 as filed June 22, 2026 and identifies provisional No. 63/826,922, filed June 19, 2025, in the priority discussion. The separate DIA provisional identifies itself as filed June 30, 2025.

This overview summarizes the architecture. The complete claims supply its specific limitations.

---

## Grounded DI design principle

**Probabilistic generation operates within explicit authority. Execution requires authorization. Output commitment requires validation and a satisfied delivery-control condition.**

Grounded DI LLC  
Mark S. Weinstein, Founder and Inventor
