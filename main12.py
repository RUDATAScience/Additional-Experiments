"""
Micro-Level Experiment 3: Negative Correlation between Cognitive Laziness (v3) and Confidence (Beta)
- 「考えるのが面倒くさい（v3が高い）」エージェントほど、回答に対する「確信度が低い（βが低い）」
  という現実的な相関関係を組み込み、分布がどのように変化するかを検証します。
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

def run_exp3_simulation():
    # 本音は 'e'(4)、社会的要請は 'a'(0)
    target_true = 4   
    target_social = 0 
    alphas = [1.5, 1.5, 2.0]
    
    # v3（認知的負荷の回避）の増加シナリオ
    v3_values = [0.1, 0.4, 0.7, 0.9]
    choices = ['a', 'b', 'c', 'd', 'e']

    # グラフ描画
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharey=True)
    axes = axes.flatten()
    sns.set_theme(style="whitegrid")

    for i, v3 in enumerate(v3_values):
        # 本音(v1)と妥協(v3)のトレードオフとする（v2=0で固定）
        v1 = 1.0 - v3
        v2 = 0.0
        v_weights = [v1, v2, v3]
        
        # 【中核ロジック】v3が高いほど、βが下がる関数（例: Max 15.0 から Min 2.0 へ減衰）
        # beta = 15.0 - 13.0 * v3
        beta = max(2.0, 15.0 - (13.0 * v3))
        
        _, p = simulate_individual(v_weights, target_true, target_social, alphas, beta)
        
        ax = axes[i]
        sns.barplot(x=choices, y=p, ax=ax, palette="coolwarm", alpha=0.8)
        
        ax.set_title(f"Scenario {i+1}: v3={v3:.1f}  ->  \u03B2={beta:.1f}", fontsize=13)
        ax.set_ylabel("Probability")
        ax.set_ylim(0, 1.0)
        
        # パラメータの状態をテキストで表示
        status_text = f"Honest (v1): {v1:.1f}\nLazy (v3): {v3:.1f}\nNoise level: {'High' if beta < 5 else 'Low'}"
        ax.text(0.5, 0.75, status_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.6))
        
        # ターゲット位置の明記
        ax.text(target_true, 0.85, 'True\nState', ha='center', color='red', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.suptitle("Experiment 3: Negative Correlation Between Cognitive Laziness (v3) and Confidence (\u03B2)", fontsize=16, y=1.05, weight='bold')
    
    # 画像として保存
    plt.savefig('micro_exp3_v3_beta_correlation.png', dpi=300, bbox_inches='tight')
    print("Saved visualization to 'micro_exp3_v3_beta_correlation.png'")
    plt.show()

if __name__ == "__main__":
    run_exp3_simulation()
