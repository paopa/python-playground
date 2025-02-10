import torch
import time

# Get Started with PyTorch
start_time = time.time()

x = torch.rand(5, 3)
print(x)

elapsed_time = time.time() - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")
