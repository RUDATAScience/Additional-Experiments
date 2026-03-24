## Additional Experiments

To demonstrate the robustness and versatility of the proposed Micro-Macro Link Model, we conducted several additional validation experiments.

### Experiment 1: Probability Fusion with Adjacent Targets
**File:** `micro_exp1_close_targets.py`

**Objective:** In the baseline simulation, the True State ('e') and Social Demand ('a') were completely polarized, resulting in a distinct Bimodal distribution during internal conflict. This experiment tests the model's behavior when the True State and Social Demand are adjacent or close to each other (e.g., True State = 'b', Social Demand = 'a').

**Results & Insights:**
When the conflicting targets are close, the model beautifully simulates **Probability Fusion**. Instead of polarizing into two distinct peaks, the probabilities fuse to create a **Skewed Unimodal Distribution**. 
- In Panel 4 (Internal Conflict), the agent's probability mass is smoothly distributed across 'a' and 'b', naturally expressing a "compromised choice slightly pulled by social atmosphere."
- This proves that our Distance-Decay AHP model correctly captures the gradient of human cognition, rather than treating choices as strictly discrete and independent categories.