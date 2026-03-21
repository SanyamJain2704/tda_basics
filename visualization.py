import matploblib.pyplot as plt

def plot_persistence_diagram(dim_times):

    plt.figure(figsize=(6,6))

    colors = {
        0: 'blue',
        1: 'red',
        2: 'green',
        3: 'purple' ## Most examples won't focus on dimensions above these
    }

    max_val = 0

    for dim in dim_times:
        for birth, death in dim_times[dim]:
            if death != float('inf'):
                max_val = max(max_val, birth, death)
            else:
                max_val = max(max_val, birth)

    inf_proxy = max_val * 1.1 + 0.1

    for dim in dim_times:
        label_added = False 
        for birth, death in dim_times[dim]:

            plot_death = inf_proxy if death == float('inf') else death
            is_inf = death == float('inf')

            plt.scatter(
                birth, plot_death,
                color=colors.get(dim, 'black'),
                label=f"H{dim}" if not label_added else "",
                marker='*' if is_inf else 'o',  s
                s=80,
                zorder=3
            )
            label_added = True

    plt.plot([0, inf_proxy], [0, inf_proxy], 'k--', linewidth=1)

    plt.axhline(y=inf_proxy, color='gray', linestyle=':', linewidth=1, label='∞ (never dies)')

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.xlabel("Birth")
    plt.ylabel("Death")
    plt.title("Persistence Diagram")`
    plt.grid(True)
    plt.show()

def plot_barcodes(dim_times):

    plt.figure(figsize=(8, 5))

    colors = {
        0: 'blue',
        1: 'red',
        2: 'green',
        3: 'purple'
    }
  
    max_val = 0
    for dim in dim_times:
        for birth, death in dim_times[dim]:
            if death != float('inf'):
                max_val = max(max_val, birth, death)
            else:
                max_val = max(max_val, birth)

    inf_proxy = max_val * 1.1 + 0.1

    y = 0  
    yticks = []
    yticklabels = []

    for dim in sorted(dim_times.keys()):
        for birth, death in dim_times[dim]:

            plot_death = inf_proxy if death == float('inf') else death
            is_inf = death == float('inf')

            plt.hlines(
                y=y,
                xmin=birth,
                xmax=plot_death,
                colors=colors.get(dim, 'black'),
                linewidth=2
            )

            if is_inf:
                plt.annotate(
                    '',
                    xy=(plot_death + 0.01, y),
                    xytext=(plot_death, y),
                    arrowprops=dict(arrowstyle='->', color=colors.get(dim, 'black'))
                )

            yticks.append(y)
            yticklabels.append(f"H{dim}")
            y += 1

        y += 1

    plt.axvline(x=0, color='black', linewidth=0.8, linestyle='--')

    plt.yticks(yticks, yticklabels, fontsize=7)
    plt.xlabel("Filtration Value")
    plt.title("Persistence Barcodes")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
