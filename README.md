## Additional Experiments

To demonstrate the robustness and versatility of the proposed Micro-Macro Link Model, we conducted several additional validation experiments.

### Experiment 1: Probability Fusion with Adjacent Targets
**File:** `micro_exp1_close_targets.py`

**Objective:** In the baseline simulation, the True State ('e') and Social Demand ('a') were completely polarized, resulting in a distinct Bimodal distribution during internal conflict. This experiment tests the model's behavior when the True State and Social Demand are adjacent or close to each other (e.g., True State = 'b', Social Demand = 'a').

**Results & Insights:**
When the conflicting targets are close, the model beautifully simulates **Probability Fusion**. Instead of polarizing into two distinct peaks, the probabilities fuse to create a **Skewed Unimodal Distribution**. 
- In Panel 4 (Internal Conflict), the agent's probability mass is smoothly distributed across 'a' and 'b', naturally expressing a "compromised choice slightly pulled by social atmosphere."
- This proves that our Distance-Decay AHP model correctly captures the gradient of human cognition, rather than treating choices as strictly discrete and independent
- categories.

- ### Experiment 2: Sensitivity Analysis of Distance-Decay Parameter (Alpha)
**File:** `micro_exp2_alpha_sensitivity.py`

**Objective:** The decay parameter $\alpha$ in our Distance-Decay AHP model represents an agent's "strictness" or "sensitivity" to differences among choices. This experiment fixes the agent's cognitive balance to an "Honest" state ($v_1=0.8$) and tests how varying $\alpha$ from $0.5$ to $5.0$ affects the spread of the probability distribution.

**Results & Insights:**
- **Low Sensitivity ($\alpha=0.5$):** The distribution shows a wide bell shape around the True State ('b'). This represents an "ambiguous or tolerant" culture where agents feel that adjacent choices (like 'a' or 'c') are also acceptable answers.
- **High Sensitivity ($\alpha=3.0$) to Absolute Strictness ($\alpha=5.0$):** The probability mass concentrates entirely on the True State ('b'), completely flattening all other options. This represents a "binary or strict" culture where individuals draw a clear, uncompromising line between their preferred choice and all others.
- **Academic Contribution:** This demonstrates that the Micro-Macro model can mathematically parameterize cultural or contextual differences in survey responses. A society that values nuance can be modeled with a low $\alpha$, while a highly polarized, black-and-white society can be modeled with a high $\alpha$.

### Experiment 3: Negative Correlation Between Cognitive Laziness and Confidence
**File:** `micro_exp3_v3_beta_correlation.py`

**Objective:** In reality, agents who choose to avoid cognitive load (high $v_3$) not only gravitate toward the central choice ('c') but also tend to have lower confidence in their answers, resulting in noisier choices (low $\beta$). This experiment models this human psychological trait by introducing a negative correlation function: $\beta = 15.0 - 13.0 \times v_3$.

**Results & Insights:**
- **Scenario 1 (Low $v_3$, High $\beta$):** The agent carefully considers their True State ('e') and answers with high confidence, resulting in a sharp, deterministic peak.
- **Scenario 4 (High $v_3$, Low $\beta$):** As cognitive laziness dominates, the primary probability mass shifts to the center ('c'). Crucially, because $\beta$ drops significantly, the Softmax function spreads the probability across adjacent choices ('b' and 'd'). 
- **Academic Contribution:** This perfectly replicates the "noisy centralization" frequently observed in poorly designed surveys. It proves that the "central tendency bias" is not a single deterministic attraction to 'c', but rather a combination of "AHP weight shifting to 'c'" and "Softmax noise flattening the distribution."
