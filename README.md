# Source: https://medium.com/@groundeddi/synthetic-ai-data-is-not-reality-how-deterministic-intelligence-can-preserve-auditable-and-35413fbe3f6a?postPublishedType=initial

# Synthetic AI Data is Not Reality — How Deterministic Intelligence can Preserve Auditable and Verifiable Practices as Synthetic Information Enters Consequential Systems

# GroundedDI

Synthetic AI data is now part of the operating machinery of AI development. Meta reports that synthetic generation produced the vast majority of the supervised fine-tuning examples used in Llama 3.1 post-training.[1] Apple identifies synthetic data as one component of the training mixture for its 2026 foundation models and separately describes using synthetic messages within a differential-privacy architecture to understand aggregate trends without collecting users’ underlying email content.[2][3] Google DeepMind trained AlphaGeometry using 100 million unique synthetic examples.[4] NVIDIA describes synthetic-data generation, curation, reinforcement learning, and evaluation as components of its infrastructure for physical AI.[5]
Those uses are not equivalent. Neither are their epistemic status or their risks.
A formally generated geometry proof can be checked against explicit rules. A simulated future climate state can be understood as a conditional projection under identified assumptions. A synthetic patient history, social interaction, economic record, or piece of generated prose may contain assumptions whose validity is considerably harder to establish.
The deeper problem may therefore be larger than synthetic-data quality.
The problem of the next data era may not be scarcity of data. It may be scarcity of provenance-preserved reality.
For purposes of this essay, provenance-preserved reality means maintaining a machine-readable distinction among what was observed, what was human-authored, what was formally derived, what was transformed, what was simulated, what was model-generated, and what remains unknown.
Those categories do not rank truth automatically. Human-authored material can be wrong. Observations can contain measurement error. Simulations can be highly informative. Formal derivations can be more readily verifiable than many forms of prose.
The point is that they are different kinds of evidence, and systems should not silently erase those differences.
Grounded DI’s proposed role is not to generate synthetic data. It is to govern the boundary between constructed information and consequential downstream use.
The receipt records the decision. The control boundary is the product.
The governing principle is simple:
Auditability does not make synthetic data true. It makes its origin attributable, its generation reproducible where possible, its use bounded, and its release rejectable.
The Data Pressure of 2026
The attraction of synthetic data is easy to understand.
Real observations can be expensive, private, dangerous to collect, poorly labeled, legally restricted, geographically incomplete, or rare.
The FDA’s medical-AI research program, for example, identifies high acquisition costs, safety limitations, privacy restrictions, annotation burdens, and low disease prevalence as obstacles to obtaining representative patient datasets. The agency is studying both the possibilities and limitations of supplementing patient datasets with synthetic data.[6]
That is materially different from declaring synthetic records equivalent to patient observations.
Modern foundation-model development creates another source of pressure. Meta reports using synthetic generation for the vast majority of Llama 3.1 supervised fine-tuning examples, while also describing rejection sampling, filtering, iterative generation, and data balancing.[1] Apple states that its third-generation foundation models are trained using a mixture that includes publicly available, licensed or purchased, open-source, study-derived, and synthetic data.[2]
Physical AI creates a different problem.
NVIDIA’s March 2026 Physical AI Data Factory Blueprint combines data processing and curation, synthetic generation, reinforcement learning, and evaluation for robotics, autonomous vehicles, and vision systems.[5] NVIDIA presents this as a way to address scale and difficult-to-acquire scenarios.
Those are company technical claims, not independent proof that any particular simulation adequately represents the world.
Synthetic data is therefore not a hypothetical future issue.
It is already being used.
The harder questions are whether it should be used for a particular purpose, what epistemic status should travel with it, and what controls should determine where it is allowed to go.
The Scarce Resource May Be Reality With Its Lineage Intact
Generative systems change the economics of data creation.
Once an organization can produce thousands or millions of examples cheaply, sheer volume becomes less impressive.
What may become more valuable is knowing what remains anchored to observation, human scholarship, verified derivation, or independently collected evidence.
The Nature model-collapse study by Shumailov and colleagues makes part of this issue concrete. The researchers found that indiscriminate recursive training on model-generated data can progressively distort the learned distribution, with low-probability portions of the original distribution disappearing first.[7]
Their experiments do not establish that all synthetic-data use produces collapse. Preserving original data mitigated degradation in their language-model experiments.
But the study underscores the value of maintaining access to original human-produced material and the difficulty of distinguishing generated from non-generated material at scale.
That suggests a principle broader than simply labeling data as synthetic.
An organization may need to preserve distinctions such as:
Observation → human interpretation → formal derivation → transformation → simulation → model generation → subsequent generation
Those relationships are provenance, but they are also epistemic information.
The architecture should know what kind of thing it is standing on.
Where Grounded DI Fits
Important parts of this problem are already being addressed.
W3C PROV-O provides concepts for entities, activities, agents, generation, attribution, and derivation.[8]
Croissant 1.1 goes considerably further than ordinary dataset documentation. MLCommons describes machine-actionable provenance and governance, including DUO- and ODRL-based usage restrictions that automated systems can inspect when evaluating proposed uses.[9][10]
Data-validation infrastructure, policy engines, catalogs, registries, access controls, and admission controls also already exist.
Synthetic-data-specific workflow controls exist in narrower contexts as well. AWS Clean Rooms ML, for example, can evaluate generated data against configured privacy criteria and prevent the resulting synthetic dataset from proceeding into a model-training input channel when a configured threshold is not satisfied.[11]
The point is therefore not to claim that Grounded DI invented provenance, policy expression, validation, state machines, admission control, or synthetic data.
Existing standards increasingly make provenance and usage policies machine-actionable.
Grounded DI’s proposed role is to resolve those signals together with constructed-object ancestry, purpose-specific validation, unresolved conditions, and destination context into an operational admission state.
That creates two distinct gates.
Gate 1
Should construction happen for this information problem at all?
Gate 2
If constructed information exists, should this particular object enter this particular destination?
That distinction matters commercially because Grounded DI does not need to displace generators, synthetic-data vendors, catalogs, model registries, provenance standards, or policy systems.
It can operate between them and the systems that actually use the information.
A simplified enterprise path looks like this:
Generator / simulator / source system
↓
Provenance + ancestry evidence
↓
Purpose-specific validation
↓
Use + destination request
↓
Machine-readable admission state
↓
Allow / restrict / review / block
↓
Receipt + audit evidence
For an enterprise, the advantage is not another metadata format.
It is one configurable admission layer that can apply the organization’s evidence, validation, use, and destination rules consistently across otherwise heterogeneous data pipelines.
From Provenance to State
The progression is:
Documentation → provenance → validation → state → destination decision
Documentation explains an artifact.
Provenance records origin and derivation.
Validation measures identified properties.
State expresses what those results mean for a specified purpose.
A destination decision determines whether the artifact may enter a particular workflow.
Croissant, PROV-O, ODRL, and related infrastructure already provide important portions of this foundation.
The distinction should therefore not be reduced to “metadata versus enforcement.” Modern standards increasingly support machine-readable governance.
The additional question is whether constructed-information-specific evidence is resolved together:
Where did the object come from?
Is its ancestry sufficiently known?
Did it inherit restrictions?
Which validation dimensions were tested?
Which remain unresolved?
What use is requested?
What destination is involved?
What state do those facts produce for that specific use?
The proposed receipt is therefore not merely evidence that something happened.
It records the result of a control decision that affects what the system may do next.
Where a required provenance, validation, integrity, or authorization condition remains unresolved, a controlled workflow can preserve that unresolved state rather than silently converting uncertainty into permission.
Admission can remain blocked until the condition is satisfied or an authorized exception is recorded.
Auditability Can Still Certify the Wrong Thing
There is an obvious objection to any architecture built around receipts and audit evidence:
A perfectly auditable system can still be wrong.
Auditability is not truth.
A hash can prove that a defective artifact was preserved perfectly.
Replay can reproduce the same error.
A provenance graph can describe biased ancestry with complete accuracy.
A receipt therefore cannot be treated as a certificate of truth.
Its value is narrower and more operational: it makes origin, process, validation state, limitations, authorization, and downstream disposition inspectable.
The hard question remains whether the system asked the right questions before it authorized use.
Synthetic Data Is Not One Thing
A language-model-generated instruction pair is not the same technical object as a statistically synthesized table.
Neither is equivalent to rendered lidar, a simulated collision, a digital twin, a generated molecular structure, a synthetic medical image, or a formal geometry proof.
AlphaGeometry illustrates an unusually favorable case.
DeepMind reports generating one billion geometry diagrams, deriving relationships within them, and filtering the resulting material into 100 million unique training examples. Its solutions could then be checked by computer against explicit deductive rules.[4]
That is very different from generating a synthetic profile of a human being.
Formally constrained synthetic material may be directly verifiable.
Physical simulation may be tested against observations and physical constraints while still exhibiting a simulation-to-reality gap.
Statistical synthesis may preserve selected distributions while distorting relationships that were not modeled.
Generated text may be fluent while containing unsupported propositions.
Privacy-enhanced synthesis may reduce particular risks only when the actual privacy mechanism supplies those protections.
A boolean such as:
{
  "synthetic": true
}
does not tell a downstream system enough.
Suitability Comes Before Generation
There are cases where constructed information is not merely a cheap substitute for observations.
Future-state climate modeling is a clean example.
An organization operating in 2026 cannot collect observations from 2036.
Climate researchers instead use physical models, historical observations, boundary conditions, and explicit future scenarios to produce projections. NOAA describes future climate projections as model simulations under possible forcing scenarios, while CMIP6 ScenarioMIP coordinates future projections under specified scenarios.[12]
That should not be confused with claiming to know the exact weather on a particular day ten years from now.
It is conditional modeling of future climate states.
The strongest case for constructed data is often one in which the output is valuable precisely because it is identified as a hypothetical generated under known assumptions.
But construction is not always the right response.
The February 2026 preprint Should I Use Synthetic Data for That? analyzes synthetic data as a proxy for proprietary datasets, as machine-learning augmentation, and as statistical sample augmentation. Its authors identify circumstances in which synthetic data can be a poor fit for the underlying information problem.[13]
The paper remains a preprint and should be treated accordingly.
If an organization’s deficiency is missing observation, a generator trained on the deficient evidence cannot manufacture independent observations of what was never there.
Additional rows may simply encode the same assumptions more densely.
That is why control can begin before a synthetic object exists.
A system may resolve the request to:
Construction authorized
Or instead:
observed evidence required
human evidence required
real-world collection required
review required
The first gate asks whether construction is a suitable response.
The second asks what may happen to the constructed object afterward.
Synthetic Is Not a Privacy Guarantee
Synthetic data and anonymous data are not synonyms.
The UK Information Commissioner’s Office defines synthetic data as material generated from one or more models of original data and states that it may or may not be anonymous.[14]
NIST likewise warns that many synthetic-data techniques do not satisfy differential privacy — or any formal privacy property.
Differentially private synthesis can provide mathematical privacy guarantees, but those guarantees derive from the privacy mechanism, not merely from calling the result synthetic.[15]
NIST’s PETs Testbed also warns that synthesis and other de-identification methods can introduce artifacts, bias, and distributional distortion that are not necessarily easy to diagnose.[16]
Synthetic describes how an artifact was produced. It does not, by itself, establish a privacy guarantee.
A receipt intended for privacy-sensitive workflows should identify the relevant privacy mechanism, evaluation method, results, and limitations rather than relying on the synthetic label itself.
Origin and Genealogy Matter
Synthetic provenance is not binary.
It is genealogical.
And the genealogy should preserve the boundary between observation and construction.
Possible origin classes include:
Observed / human-authored / formally derived / transformed / simulated / model-generated / mixed / unknown
These classifications do not themselves establish correctness.
“Human-authored” is not a truth certificate.
“Observed” data may contain measurement error.
“Simulated” does not mean worthless.
A formally derived artifact may sometimes be more readily verifiable than human prose.
The purpose is not to create an epistemic caste system.
It is to prevent unlike forms of evidence from becoming indistinguishable simply because they were serialized into the same corpus.
A constructed artifact may have a genealogy such as:
Observed
→ transformed
→ model-generated
→ filtered
→ regenerated
→ selected
Or:
Human-authored scholarship
→ extracted proposition
→ model-generated paraphrase
→ synthetic evaluation item
Or:
Observed sensor data
→ calibrated physical model
→ simulated future state
A CVPR 2025 paper demonstrates that synthetic-data provenance itself is becoming a technical research problem.
Xie and colleagues developed a method for determining, within their experimental setting, whether a downstream model had been trained using synthetic images produced by a particular generative model.[17]
The work does not provide a universal ancestry detector, but it reinforces the importance of provenance verification.
That also requires distinguishing declared ancestry from verified ancestry.
Useful states might include:
Declared / verified / partial / unresolved
Transformation should not automatically launder provenance.
Nor should uncertainty about ancestry automatically become permission.
Benchmark Contamination as an Admission Problem
Benchmark contamination makes the architecture concrete.
ICML 2025 research describes evaluation-data contamination as overlap between evaluation data and training corpora that can inflate performance estimates and undermine the reliability of model evaluation.[18]
An evaluation artifact could therefore carry:
authorized_use:
  - evaluation
prohibited_use:
  - production_training
Now imagine that artifact is paraphrased, reformatted, or incorporated into a synthetic augmentation process.
A controlled system should not assume the restriction vanished merely because the representation changed.
If the descendant relationship is known, the admission layer can inspect ancestry, identify the inherited restriction, deny entry to a production-training destination, and generate an audit event explaining the decision.
For an enterprise, that turns benchmark hygiene from a policy memo into an enforceable pipeline condition.
Exactly how restriction inheritance is implemented is outside the scope of this public conceptual description.
Validation Must Be Multidimensional
There should be no universal:
{
  "validation": "pass"
}
A synthetic artifact may pass schema validation while failing domain-gap evaluation.
It may satisfy a privacy threshold while having poor downstream utility.
It may be semantically correct but duplicated so heavily that it damages corpus diversity.
Subscribe to the Medium newsletter
Depending on purpose, validation may examine:
structural validity
formal correctness
semantic support
distributional fidelity
duplication
privacy
membership inference
bias
domain gap
safety
contamination
representativeness
downstream utility
EACL 2026 research on synthetic-data-generator selection is instructive.
In its tested setting involving multiple LLMs, languages, and tasks, intrinsic synthetic-data heuristics correlated poorly with downstream performance; the authors proposed another proxy method for generator selection.[19]
Accordingly:
A synthetic object is validated only against an identified profile, for an identified purpose, using identified tests and thresholds.
“Validated” by itself is too ambiguous to govern a consequential decision.
The relevant commercial question is whether those results actually change machine state.
If a failed or unresolved condition merely appears on a dashboard, the organization has documentation.
If it disables entry to the configured destination, the organization has control.
Synthetic Data With Receipts
A public-facing receipt need not be large.
For example:
{
  "object_id": "aco_...",
  "origin_class": "model-generated",
  "ancestry_status": "verified",
  "validation_profile": "profile_...",
  "authorized_use": ["evaluation"],
  "prohibited_use": ["production_training"],
  "requested_destination": "eval_pipeline_...",
  "admission_state": "authorized",
  "integrity": "sha256:..."
}
This is not intended to replace Croissant, PROV-O, ODRL, privacy standards, data catalogs, or enterprise policy systems.
A serious implementation should interoperate with them.
The receipt’s role is to allow a downstream system or reviewer to determine:
Where did this come from?
What kind of origin does it have?
Which ancestry is known?
What did it inherit?
What was tested?
What remains unresolved?
Which use is requested?
Which destination is involved?
Is admission presently authorized?
The schema is evidence.
The commercially important component is the controller that evaluates that evidence before downstream admission.
The receipt records the decision. The control boundary is the product.
The Enterprise Control Boundary
Grounded DI’s proposed commercial role is to provide a control architecture between constructed information and consequential use.
At the architecture level, Grounded DI can design validation frameworks, constructed-information states, receipt structures, enterprise policies, and admission logic that connect provenance evidence to downstream decisions.
At the integration level, an implementation can sit across existing catalogs, model registries, training orchestration, evaluation systems, data loaders, APIs, and governance infrastructure rather than requiring organizations to replace them.
At the control boundary, a candidate artifact or batch can resolve to states such as:
Admit / restrict / review / revise / withhold / block / retire / recall / revalidate
Those states can control configured destinations such as:
training ingestion
evaluation ingestion
registry eligibility
API transfer
downstream workflow entry
other designated data-processing interfaces
Grounded DI therefore does not need to compete with Meta, NVIDIA, Apple, simulation providers, or synthetic-data vendors on generation volume.
The commercial question is different:
Which constructed information may enter which consequential system, for which purpose, under whose authority, and based on what evidence?
For an enterprise buyer, the value is not additional metadata for its own sake.
It is the ability to produce and enforce a repeatable answer to that question across teams, generators, datasets, and downstream systems — and to preserve evidence of why each consequential admission or rejection occurred.
Potential delivery models include enterprise licensing, private deployment, systems integration, managed admission gateways, custom validation profiles, governance configuration, and ongoing support.
Grounded DI does not need to replace an organization’s provenance or policy infrastructure.
Generators construct. Standards and governance systems provide evidence and policy. Grounded DI’s proposed role is to resolve that evidence at the boundary where constructed information becomes operational.
A Reference Lifecycle
A practical lifecycle can be expressed as a sequence of control decisions.
1. Information need
The organization identifies the information problem.
2. Is construction suitable?
If no, the workflow routes toward observed or human-origin evidence.
If yes, a generation or simulation specification is created.
3. Constructed artifact
The resulting object enters provenance and ancestry review.
4. Origin + ancestry
The system identifies what is known, verified, inherited, partial, or unresolved.
5. Purpose-specific validation
The artifact is evaluated using the tests and thresholds relevant to its intended use.
6. Are required conditions satisfied?
If no, the artifact may move to:
Review / restrict / revise / withhold / block
If yes, it moves to destination authorization.
7. Is the destination authorized?
If no, admission is blocked.
If yes, the artifact enters the configured destination.
8. Monitoring + audit
Authorized use remains subject to evidence and state changes.
9. Material change or defect?
If yes, the artifact may be:
Recalled / retired / revalidated
If no, authorized use continues.
The first gate matters because the architecture does not begin by assuming synthetic generation is appropriate.
The second gate matters for a different reason.
Even a legitimately constructed object is not automatically suitable for every downstream use.
What a Receipt Can — and Cannot — Establish
A receipt can support evidence about whether an artifact was observed, simulated, transformed, generated, or mixed.
It cannot establish by itself that the artifact is true.
A receipt can record which generator or model version produced an artifact.
It cannot establish by itself that the generator was appropriate.
A receipt can identify known sources or parents that influenced an artifact.
It cannot establish that all ancestry has been discovered.
A receipt can record whether ancestry is declared, verified, partial, or unresolved.
It cannot establish that unknown external transformations did not occur.
A receipt can record which validations were executed.
It cannot establish that every relevant failure mode was tested.
A receipt can record which thresholds were applied.
It cannot establish that those thresholds were well chosen.
A receipt can record which uses were authorized or prohibited.
It cannot establish that the authorized use is scientifically or legally correct.
A receipt can record whether a content or manifest hash changed.
It cannot establish that unchanged content was valid.
A receipt can record whether replay is possible under stated conditions.
It cannot establish that a changing external service can be reproduced forever.
A receipt can record who authorized a state transition.
It cannot establish that the decision-maker was infallible.
A receipt preserves evidence about provenance, process, state, and authorization.
It does not turn construction into observation.
Practical Governance Challenges
A commercial implementation still faces difficult questions.
Granularity
Some systems may require record-level controls.
Others may use generation-run or batch manifests with object-specific exceptions.
Confidentiality
Complete provenance may expose trade secrets, personal information, prompts, source-dataset membership, model details, or security-sensitive configurations.
Commercial deployments may therefore require detailed internal records and more limited external receipts.
Replay
A local simulator with preserved binaries, seeds, inputs, and configuration may support strong replay.
An external model endpoint that changes over time may permit only partial or functional reproduction.
Enforcement
A restriction that no system checks is still only documentation.
Effective deployment may require policy-aware data loaders, signed manifests, registry checks, access controls, gateways, or equivalent enforcement interfaces.
Governance quality
Validation rules can themselves be weak.
A perfectly audited bad threshold is still a bad threshold.
For that reason, validation profiles and destination policies should be organization-configured or implementation-specific rather than presented as universal truth functions.
When material evidence changes, previously admitted material may also need to be recalled, retired, or revalidated.
Relationship to Existing Governance
The proposed architecture is consistent with broader data-governance direction, but it should not be described as legally required or automatically compliant.
The NIST AI Risk Management Framework and its Playbook are voluntary. NIST describes the Playbook as a companion resource for operationalizing risk-management practices and emphasizes intended purpose and context of use.[20]
Article 10 of the EU AI Act requires covered high-risk AI systems that use training, validation, and testing datasets to apply data-governance practices appropriate to their intended purpose, including attention to data origin and dataset suitability.[21]
That does not mean a Grounded DI receipt would itself establish compliance.
The broader direction is toward machine-readable lineage, policy, evaluation, and control.
Grounded DI’s proposed role is to resolve those inputs at the boundary where constructed information attempts to become operational data.
Governing the Hypothetical
Humanity has accumulated thousands of years of observation, scholarship, experimentation, argument, mathematics, measurement, literature, and technical knowledge.
AI systems should become better at using that inheritance.
Generating more material should not become an excuse for losing track of where knowledge came from.
At the same time, construction has legitimate uses.
We cannot observe 2036 in 2026.
We cannot safely stage every dangerous autonomous-vehicle event simply to collect examples.
Formal systems can generate mathematical cases at scales humans could never author individually.
Simulations can explore conditional worlds that do not yet exist.
The distinction is not real good, synthetic bad.
The distinction is whether the system preserves what kind of evidence it is using.
The more defensible approach is to preserve the boundary between observation and construction — and, where construction serves a legitimate purpose, govern it according to what it is:
A representation generated under identifiable assumptions, dependencies, and conditions.
Some information problems should not be solved by construction at all.
Sometimes the right answer is to collect better observations, seek better human expertise, or admit that the information does not yet exist.
For organizations that determine synthetic data is necessary, this creates a practical commercial question.
A receipt cannot make a hypothetical true.
It can make the hypothetical inspectable.
Synthetic data does not need a certificate of truth.
It may need a receipt.
▁▂▃▄▅▆▇█▇▆▅▄▃▂▁
About the Author
Mark S. Weinstein is a litigation attorney and the creator of Protocol A, the deterministic reasoning framework that became the foundation of Grounded DI LLC.
Sources and Notes
Meta, “Introducing Llama 3.1,” July 23, 2024.
Apple Machine Learning Research, “Introducing the Third Generation of Apple’s Foundation Models,” June 8, 2026.
Apple Machine Learning Research, “Understanding Aggregate Trends for Apple Intelligence Using Differential Privacy,” April 14, 2025.
Google DeepMind, “AlphaGeometry: An Olympiad-level AI system for geometry,” January 17, 2024.
NVIDIA, “NVIDIA Announces Open Physical AI Data Factory Blueprint,” March 16, 2026.
U.S. Food and Drug Administration, “Addressing the Limitations of Medical Data in AI.”
Shumailov et al., “AI models collapse when trained on recursively generated data,” Nature, July 24, 2024.
W3C, PROV-O: The PROV Ontology.
MLCommons, Croissant 1.1, February 12, 2026.
W3C, ODRL Information Model.
AWS, Clean Rooms synthetic-data generation and privacy-threshold documentation.
NOAA climate-model and future-projection materials; CMIP6 ScenarioMIP materials.
Kulynych, Stadler, Raisaro & Troncoso, “Should I Use Synthetic Data for That? An Analysis of the Suitability of Synthetic Data for Data Sharing and Augmentation,” February 3, 2026. Preprint.
UK Information Commissioner’s Office, Anonymisation Glossary — Synthetic Data.
NIST, “Differentially Private Synthetic Data,” May 3, 2021.
NIST, PETs Testbed, updated March 19, 2026.
Xie et al., “Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training?” CVPR 2025.
Choi et al., “How Contaminated Is Your Benchmark? Measuring Dataset Leakage in Large Language Models with Kernel Divergence,” ICML 2025.
Cegin et al., “RoSE: Round-robin Synthetic Data Evaluation for Selecting LLM Generators without Human Test Sets,” EACL 2026.
NIST, AI Risk Management Framework Playbook.
European Union, Regulation (EU) 2024/1689, Article 10.
Grounded DI Design Basis: Grounded DI’s internal architecture supplies the company design basis for the proposed control approach described here at a conceptual level. Application to synthetic-data-specific or constructed-information workflows is presented as a proposed commercial extension, not as evidence that a synthetic-data product is already deployed.
