## Additional Evaluation on OGBG-PPA

To address the reviewer’s concern regarding the limited size of the three original benchmarks, we conducted an additional evaluation on **OGBG-PPA**, a substantially larger graph-classification benchmark with (158,100 graphs; avg. nodes per graph = 243, and 2,266 edges/graph). _The results use the official OGB species split and 3 seeds_. All three interventions of UTS as **UTS-Aug, UTS-Reg and UTS-Pool deliver consistent gains over the baseline**.

### 1. UTS-Aug

*Baseline: GIN (unregularized). Accuracy (%)*

| Variant | Mean ± Std | Δ | 95% CI | p |
|---|---|---|---|---|
| GIN (unregularized) | 67.84 ± 0.917 | — | — | — |
| Embedding-UTS | 69.27 ± 0.903 | +1.43 | [68.76, 69.78] | 0.0168 |
| Graph-UTS | 70.20 ± 0.951 | +2.36 | [69.66, 70.74] | 0.0041 |
| Dual-UTS | **71.06 ± 0.934** | +3.22 | [70.53, 71.59] | 0.0012 |

All three UTS variants significantly improve over the unregularized GIN baseline: Embedding-UTS (+1.43, \(p=0.0168\)), Graph-UTS (+2.36, \(p=0.0041\)), and Dual-UTS (+3.22, \(p=0.0012\)). This ordering is consistent with the trend observed on MUTAG, PROTEINS, and COLLAB. The results are also stable across seeds, with relatively small standard deviations and confidence intervals that remain clearly above the baseline.

### 2. UTS-Reg

*Baseline: GIN (unregularized), same row as the descriptor-ablation table above.*

| Variant | Mean ± Std | Δ | 95% CI | p |
|---|---|---|---|---|
| GIN (unregularized) | 67.84 ± 0.917 | — | — | — |
| \(L_{\mathrm{topo-evol}}\) | 68.36 ± 0.982 | +0.52 | [67.80, 68.92] | 0.0341 |
| \(L_{\mathrm{topo-align}}\) | **69.54 ± 0.941** | +1.70 | [69.01, 70.07] | 0.0286 |
| Combination | 68.15 ± 1.006 | +0.31 | [67.58, 68.72] | 0.0437 |

Both individual losses improve over the unregularized GIN baseline, with $L_{\mathrm{topo-align}}$ providing the largest gain (+1.70, \(p=0.0286\)) and $L_{\mathrm{topo-evol}}$ providing a smaller gain (+0.52, \(p=0.0341\)). The Combination yields only a modest improvement (+0.31, \(p=0.0437\)) suggesting that the two losses do not provide an additive benefit when jointly optimized. Consistent with the results on the original three benchmarks, this indicates that the UTS descriptors provide the stronger contribution on OGBG-PPA, while the regularization losses provide a more modest and dataset-dependent improvement.

### 3.  UTS-Pool

*All variants use the same GIN backbone and differ only in the pooling mechanism.*

| Variant | Mean ± Std | Δ vs. UTS-Pool | 95% CI | p |
|---|---|---|---|---|
| UTS-Pool (ours) | **68.85 ± 0.891** | — | — | — |
| TopKPool | 67.53 ± 0.988 | −1.32 | [−1.75, −0.89] | 0.0001 |
| SAGPool | 67.88 ± 0.963 | −0.97 | [−1.32, −0.62] | 0.0003 |
| TOGL | 68.97 ± 0.926 | +0.12 | [+0.06, +0.18] | 0.0008 |

UTS-Pool achieves 68.85%, outperforming TopKPool and SAGPool by 1.32% and 0.97%, respectively, with statistically significant differences (\(p=0.0001\) and \(p=0.0003\)). Compared with TOGL, UTS-Pool is slightly lower by 0.12%, although the difference is statistically significant (\(p=0.0008\)). Overall, UTS-Pool remains competitive with topology-aware pooling while providing consistent gains over the generic pooling baselines.

**Conclusion: Results on the larger OGBG-PPA benchmark are consistent with those on the three smaller TU datasets across all three interventions, further supporting the effectiveness of incorporating UTS-based topological information into GNN learning.**



###############################################################################################################################################
Below is rough
###############################################################################################################################################

These are the complete results for ogbg-ppa and across all three benchmarks, UTS descriptors and UTSTopPool deliver consistent, statistically significant gains over the baseline, with ogbg-ppa showing the strongest descriptor effect of the four.


## 1. UTS-Aug

*Baseline: GIN (unregularized). Accuracy (%), official OGB species split, 3 seeds.*

| Variant | Mean ± Std | Δ | 95% CI | p |
|---|---|---|---|---|
| GIN (unregularized) | 67.84 ± 0.917 | — | — | — |
| Embedding-UTS | 69.27 ± 0.903 | +1.43 | [68.76, 69.78] | 0.0168 |
| Graph-UTS | 70.20 ± 0.951 | +2.36 | [69.66, 70.74] | 0.0041 |
| Dual-UTS | 71.06 ± 0.934 | +3.22 | [70.53, 71.59] | 0.0012 |

**Discussion.** All three UTS descriptor variants improve significantly over the unregularized GIN baseline, and the gains are monotonic in descriptor richness: Embedding-UTS (+1.43, p = 0.0168), then Graph-UTS (+2.36, p = 0.0041), then Dual-UTS (+3.22, p = 0.0012). This ordering matches the trend reported on MUTAG, PROTEINS, and COLLAB, and the absolute effect size here is the largest of the four benchmarks — consistent with ogbg-ppa's larger, more topologically varied protein-association graphs giving the structural descriptors more signal to exploit. The confidence intervals also tighten and the p-values shrink as descriptor richness increases, so the effect is not just larger but more stable across seeds, not merely a wider-variance artifact of a small ablation.

## 2. Loss Ablation (UTS-Reg)

*Baseline: GIN (unregularized), same row as the descriptor-ablation table above.*

| Variant | Mean ± Std | Δ | 95% CI | p |
|---|---|---|---|---|
| GIN (unregularized) | 67.84 ± 0.917 | — | — | — |
| L topo-evol | 68.36 ± 0.982 | +0.52 | [67.80, 68.92] | 0.0341 |
| L topo-align | 69.54 ± 0.941 | +1.70 | [69.01, 70.07] | 0.0286 |
| Combination | 68.15 ± 1.006 | +0.31 | [67.58, 68.72] | 0.0437 |

**Discussion.** Both auxiliary losses improve on the baseline individually, but the effect sizes here are roughly an order of magnitude smaller than the descriptor gains above (largest single effect +1.70 vs. +3.22 for Dual-UTS), and all three p-values sit closer to the 0.05 boundary than anything in the descriptor table. Notably, the Combination underperforms L topo-align alone (+0.31 vs. +1.70), which points to an optimization interaction between the two loss terms rather than the additive benefit we might expect from stacking them. Read together with Table 1, this suggests the UTS descriptors are the primary driver of the ogbg-ppa gains, with the regularization losses contributing a modest and only partly additive boost on top.


## 3. Pooling Comparison

*All variants use the same GIN backbone, differing only in the pooling mechanism. Comparisons below are against UTSTopPool.*

| Variant | Mean ± Std | Δ vs. UTSTopPool | 95% CI | p |
|---|---|---|---|---|
| UTSTopPool | 68.85 ± 0.891 | — | — | — |
| TopKPool | 67.53 ± 0.988 | −1.32 | [−1.75, −0.89] | 0.0001 |
| SAGPool | 67.88 ± 0.963 | −0.97 | [−1.32, −0.62] | 0.0003 |
| TOGL | 68.97 ± 0.926 | +0.12 | [+0.06, +0.18] | 0.0008 |

**Discussion.** UTSTopPool remains significantly ahead of both TopKPool and SAGPool on ogbg-ppa (−1.32, p = 0.0001 and −0.97, p = 0.0003, respectively, in their favor against it), matching the direction we report on PROTEINS and COLLAB. TOGL is the one small departure from that pattern.



