import neptune
import os

run = neptune.init_run(
    project="jalil-kartal/test",
    api_token=os.environ.get("API_TOKEN_NEP"),
)  # your credentials

params = {"learning_rate": 0.001, "optimizer": "Adam"}
run["parameters"] = params

for epoch in range(10):
    run["train/loss"].append(0.9 ** epoch)

run["eval/f1_score"] = 0.66

run.stop()