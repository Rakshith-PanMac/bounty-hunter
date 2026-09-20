# Project Governance: The Loop Engineering Manifest

This document defines the mandatory workflow for all changes to the Career OS. No task is considered "Done" until this sequence is completed and verified.

## 1. The Delivery Sequence (The Law)

Every implementation must follow this linear path:

1. **Proposal**: Define the change and the success criteria.
2. **Implementation**: Write the code.
3. **The Self-Healing Loop**:
    - **Universal Gate**: Run `app/verification/gate.py` (Checks API health & Theme compliance).
    - **Functional Testing**: For new features, execute a specific test script (e.g., `test_feature_x.py`) to prove the logic works.
    - **Verifier Audit**: Run `app/agents/verifier.py` (Adversarial check against Project Manifest and Test results).
    - **Refinement**: If the Verifier rejects the change, the Builder must fix the issue and repeat this loop until a `PASSED` verdict is issued.
4. **Evidence Capture**: 
    - Create a dedicated evidence folder: `static/evidence/<short-update-name>/`
    - Capture high-fidelity screenshots of the change using `app/evidence/capture.py`.
    - Save logs/traces if the change is backend-only.
5. **Human Approval**: Present the results and evidence to the user. **STOP HERE until approved.**
6. **Documentation Loop**:
    - Update technical architecture docs (how it works, why it was done, concepts used and like explaining to a beginner).
    - Update the GitHub `README.md` to reflect new features/capabilities.
7. **Git Finalization**:
    - Commit changes with a detailed message.
    - Push to the repository.

## 2. The "Zero Trust" Policy

- **No Assumptions**: I will not say "it works"; I will provide a raw HTTP response or a screenshot.
- **Actual Audit**: The Verifier Agent must audit the actual files on disk, not the summaries provided by the builder.
- **Evidence First**: Evidence is not optional; it is the primary artifact of completion.

## 3. Documentation Standards

- **Architecture Docs**: Must explain the "Why" and "How". Use diagrams or clear step-by-step flows.
- **README**: Must be a professional, high-fidelity representation of the project (inspired by `career-ops`).
       