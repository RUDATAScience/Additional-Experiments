"""
Micro-Level Experiment 2: Sensitivity Analysis of Distance-Decay Parameter (Alpha)
- 距離減衰パラメータ（α）を変化させ、選択肢間の違いに対する「こだわりの強さ（感度）」が
  回答確率の分布（裾野の広がり）にどう影響するかを検証します。
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

def run_exp2_simulation():
    # 【固定設定】本音を 'b'、社会的要請を 'd' とする
    target_true = 1   # 本音は 'b'
    target_social = 3 # 社会的要請は 'd'
    beta = 8.0
    
    # 認知バランスは「本音重視 (Honest)」に固定し、αの影響のみを抽出する
    v_weights = [0.8, 0.1, 0.1] 
    
    # 検証するαのパターン（社会全体の「白黒はっきりつける度合い」）
    alpha_scenarios = {
        "1. Low Sensitivity (α=0.5)\nAmbiguous / Tolerant": 0.5,
        "2. Baseline (α=1.5)\nNormal Human Cognition": 1.5,
        "3. High Sensitivity (α=3.0)\nStrict / Discerning": 3.0,
        "4. Absolute Strictness (α=5.0)\nBinary / Black-and-White": 5.0
    }
    
    choices = ['a', 'b', 'c', 'd', 'e']
    
    # グラフ描画
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharey=True)
    axes = axes.flatten()
    sns.set_theme(style="whitegrid")
    
    for i, (name, alpha_val) in enumerate(alpha_scenarios.items()):
        # 3つの基準すべてのαを統一して変化させる
        alphas = [alpha_val, alpha_val, alpha_val] 
        _, p = simulate_individual(v_weights, target_true, target_social, alphas, beta)
        
        ax = axes[i]
        sns.barplot(x=choices, y=p, ax=ax, palette="magma", alpha=0.8)
        
        ax.set_title(name, fontsize=12)
        ax.set_ylabel("Probability")
        ax.set_ylim(0, 1.0)
        
        # 本音のターゲット位置を明記
        ax.text(target_true, 0.85, 'True\nState', ha='center', color='red', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.suptitle("Experiment 2: Sensitivity of Choice Probabilities to Distance-Decay Parameter (\u03B1)", fontsize=16, y=1.05, weight='bold')
    
    # 画像として保存
    plt.savefig('micro_exp2_alpha_sensitivity.png', dpi=300, bbox_inches='tight')
    print("Saved visualization to 'micro_exp2_alpha_sensitivity.png'")
    plt.show()

if __name__ == "__main__":
    run_exp2_simulation()
