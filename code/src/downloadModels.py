from huggingface_hub import snapshot_download
# modelName='T5-small'
# modelDirectory='./Localmodels/T5_small'

# snapshot_download(
#     repo_id="t5-small",
#     local_dir=modelDirectory,
#     allow_patterns=["pytorch_model.bin", "config.json", "tokenizer.json", "spiece.model", "generation_config.json"],
#     local_dir_use_symlinks=False
# )




# snapshot_download(
#     repo_id="distilgpt2",
#     local_dir="./Localmodels/DistilGPT_2",
#     local_dir_use_symlinks=False,
#     allow_patterns=[
#         "pytorch_model.bin",
#         "config.json",
#         "tokenizer.json",
#         "vocab.json",
#         "merges.txt",
#         "generation_config.json"
#     ]
# )
