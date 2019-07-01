from modules.kmeans import go_cluster

settings = {
    "input_path": "./data/input.txt",
    "output_path": "./data/output.txt",
}

go_cluster(settings["input_path"], settings["output_path"])
