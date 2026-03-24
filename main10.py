"""
Micro-Level Experiment 1: Close Targets (Probability Fusion)
- 本音（True State）と社会的要請（Social Demand）の距離が近い場合、
  確率分布がどのように融合し、非対称な単峰性分布（Skewed Distribution）になるかを検証します。
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def calc_evaluation_vector(target_idx, alpha, num_choices=5):
    """距離減衰モデルによるAHP評価ベクトルの導出"""
    indices = np.arange(num_choices)
    distances = np.abs(indices - target_idx)
    u = np.exp(-alpha * distances)
    return u / np.sum(u)

def simulate_individual(v_weights, t_true, t_social, alphas, beta):
    """個人の意思決定プロセス（AHP + Softmax）"""
    v1, v2, v3 = v_weights
    a1, a2, a3 = alphas
    
    u1 = calc_evaluation_vector(t_true, a1)
    u2 = calc_evaluation_vector(t_social, a2)
    u3 = calc_evaluation_vector(2, a3) # 2 is index for 'c'
    
    w = v1 * u1 + v2 * u2 + v3 * u3
    
    w_shifted = w - np.max(w)
    exp_w = np.exp(beta * w_shifted)
    p = exp_w / np.sum(exp_w)
    
    return w, p

def run_exp1_simulation():
    # 【変更点】本音を 'b'、社会的要請を 'a' に設定（距離が近い状態）
    target_true = 1   # 本音は 'b'
    target_social = 0 # 社会的要請は 'a'
    alphas = [1.5, 1.5, 2.0]
    beta = 8.0

    scenarios = {
        "1. Honest (True State Dominant)": [0.8, 0.1, 0.1],
        "2. Social Pressure (Conformity)": [0.1, 0.8, 0.1],
        "3. Cognitive Laziness (Centralization)": [0.1, 0.1, 0.8],
        "4. Internal Conflict (Probability Fusion)": [0.45, 0.45, 0.1] # 名前を変更
    }
    choices = ['a', 'b', 'c', 'd', 'e']

    # グラフ描画
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharey=True)
    axes = axes.flatten()
    sns.set_theme(style="whitegrid")

    for i, (name, v_weights) in enumerate(scenarios.items()):
        _, p = simulate_individual(v_weights, target_true, target_social, alphas, beta)
        
        ax = axes[i]
        sns.barplot(x=choices, y=p, ax=ax, palette="viridis", alpha=0.8)
        
        v_str = f"v1={v_weights[0]}, v2={v_weights[1]}, v3={v_weights[2]}"
        ax.set_title(f"{name}\n({v_str})", fontsize=12)
        ax.set_ylabel("Probability")
        ax.set_ylim(0, 1.0)
        
        # ターゲット位置のテキストを少しずらして見やすく配置
        ax.text(target_true, 0.85, 'True\nState', ha='center', color='red', fontsize=10, weight='bold')
        ax.text(target_social, 0.95, 'Social\nDemand', ha='center', color='blue', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.suptitle("Experiment 1: Probability Fusion with Adjacent Targets ('a' and 'b')", fontsize=16, y=1.05, weight='bold')
    
    # 画像として保存
    plt.savefig('micro_exp1_close_targets.png', dpi=300, bbox_inches='tight')
    print("Saved visualization to 'micro_exp1_close_targets.png'")
    plt.show()

if __name__ == "__main__":
    run_exp1_simulation()