import os

BATCH_SIZES = [1, 2, 4, 8, 16]
NUM_THREADS = [1, 2, 4, 8, 16]
# Model configurations
model_configs = [
    {
        "path": "rostlab/prot_t5_xl_uniref50",
        "backend": "torch",
        "compile_model": 0
    },
    {
        "path": "rostlab/prot_t5_xl_uniref50",
        "backend": "torch",
        "compile_model": 1
    },
    {
        "path": "valentynbez/prot-t5-xl-uniref50-onnx",
        "backend": "onnx",
        "compile_model": 0
    },
]
tokenizer = "rostlab/prot_t5_xl_uniref50"
# for batch in tqdm(BATCH_SIZES):
#
#     for model_conf in model_configs:
#         # run script
#         os.system(f"python cpu.py --n_prots {n_prots} "
#                   f"--batch_size {batch} "
#                   f"--threads 1 --backend {model_conf['backend']} "
#                   f"--compile {model_conf['compile_model']} "
#                   f"--model_path {model_conf['path']} "
#                   f"--tokenizer_path {tokenizer}")
#         if batch == 16:
#             # run threading tests
#             for thread in NUM_THREADS:
#                 os.system(f"python cpu.py --n_prots {n_prots} "
#                           f"--batch_size {batch} "
#                           f"--threads {thread} --backend {model_conf['backend']} "
#                           f"--compile {model_conf['compile_model']} "
#                           f"--model_path {model_conf['path']} "
#                           f"--tokenizer_path {tokenizer}")

# use batch 64
batch = 256
n_prots = batch * 10
model_conf = model_configs[2]
for thread in NUM_THREADS:
    os.system(f"python benchmark.py --n_prots {n_prots} "
              f"--batch_size {batch} "
              f"--threads {thread} --backend {model_conf['backend']} "
              f"--compile {model_conf['compile_model']} "
              f"--model_path {model_conf['path']} "
              f"--tokenizer_path {tokenizer}")