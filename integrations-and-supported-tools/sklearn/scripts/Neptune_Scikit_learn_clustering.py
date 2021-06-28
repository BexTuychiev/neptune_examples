from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import neptune.new as neptune
import neptune.new.integrations.sklearn as npt_utils

run = neptune.init(
    project="common/sklearn-integration",
    api_token="ANONYMOUS",
    name="clustering-example",
    tags=["KMeans", "clustering"],
)

parameters = {"n_init": 11, "max_iter": 270}

km = KMeans(**parameters)

X, y = make_blobs(n_samples=579, n_features=17, centers=7, random_state=28743)

run["kmeans_summary"] = npt_utils.create_kmeans_summary(km, X, n_clusters=17)
