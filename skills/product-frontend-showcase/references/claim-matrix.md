# Claim matrix

Use one row per externally meaningful claim.

| Claim | Evidence | Status | Missing condition | Risk if misunderstood | Safer wording |
| --- | --- | --- | --- | --- | --- |
| Audio stays on device | Runtime behavior or architecture reference | shipped/beta/planned/unknown | Which mode/provider? | User assumes all modes are local | “In local ASR mode, audio stays on the device.” |
| 4× faster | Reproducible benchmark | shipped/beta/planned/unknown | Sample, baseline, version, date | Unsupported performance promise | Remove until measurement is published |

## Evidence hierarchy

Prefer, in order:

1. reproducible test or benchmark with conditions;
2. shipped behavior confirmed in the interface or release artifact;
3. maintained technical documentation or source-level contract;
4. approved product brief with owner and date;
5. user feedback or anecdote, labeled as such.

Do not upgrade a lower-level signal into a factual guarantee. If a claim is important but evidence is missing, keep it in unresolved questions rather than filling the gap with confident copy.

## Lifecycle vocabulary

- `shipped`: available in the referenced release/configuration;
- `beta`: available with known limitations or for a limited test group;
- `planned`: intended but not available;
- `unknown`: cannot be verified from the supplied evidence.

“Coming soon”, “supported”, and “secure” are not lifecycle states by themselves; attach a concrete condition or rewrite them.
