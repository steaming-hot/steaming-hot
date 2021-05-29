import pickle
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')


with open('umap_kmeans.model', 'rb') as f:
    models = pickle.load(f)


"""
Range of values in our data (the code will work outside these bounds)
                    Min  Max (Inclusive)
PackageCount        [1, 18]
MovieCount          [0, 20]
ScreenshotCount     [0, 180]
AchievementCount    [0, 9821]
PriceMean           [0.5, 449.99]
"""

def predict_owners(PackageCount = 1, MovieCount=3, ScreenshotCount=5, AchievementCount=10,  PriceMean=9.99):

    x = models['umap'].transform(models['scaler'].transform(np.atleast_2d([1, 3, 5, 10, 9.99, 0, 0, 0]))[:, :5])

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    fig.subplots_adjust(0, 0, 1, 1, 0, 0)

    ax = axes[0]
    s = ax.scatter(models['embeddings'][:, 0], models['embeddings'][:, 1], c=np.log10(models['owners']), cmap='YlOrRd',
                   s=2)

    ax.axis('off')
    fig.colorbar(s, ax=ax)

    s = ax.scatter(x[0, 0], x[0, 1], color='white', marker='o', s=100, facecolors='none', linewidth=2)

    ax.set_title('Predicted Monthly Sales : %i' % models['cluster_means'][models['kmeans'].predict(x)[0]], )

    ax = axes[1]
    s = ax.scatter(models['embeddings'][:, 0], models['embeddings'][:, 1],
                   c=np.log10(models['cluster_means'][models['cluster_nos']]),
                   cmap='YlOrRd', s=2)

    ax.axis('off')
    fig.colorbar(s, ax=ax)
    s = ax.scatter(x[0, 0], x[0, 1], color='white', marker='o', s=100, facecolors='none', linewidth=2)
    plt.show()
    return


predict_owners()