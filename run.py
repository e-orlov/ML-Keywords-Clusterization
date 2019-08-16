# Fast but low quality
# from modules.kmeans import go_cluster

# Slow and takes a lot of resources, but provides high quality
# from modules.affinity_propagation import go_cluster

# Testing
from modules.agglomerative_clustering import go_cluster

settings = {
    "input_path": "./data/input.txt",
    "output_path": "./data/output.txt",
}

go_cluster(settings["input_path"], settings["output_path"])
