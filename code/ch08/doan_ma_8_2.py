# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 8
# Đoạn mã 8.2. Khung huấn luyện phân tán PyTorch với TorchDistributor (Spark 3.4 trở lên).
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.torch.distributor import TorchDistributor

def train_fn(lr, epochs):
    import os
    import torch
    import torch.distributed as dist
    from torch.nn.parallel import DistributedDataParallel as DDP

    dist.init_process_group(backend="nccl")
    rank = dist.get_rank()
    local_rank = int(os.environ["LOCAL_RANK"])  # GPU cuc bo
    device = torch.device(f"cuda:{local_rank}")

    model = build_model().to(device)  # do nguoi dung dinh nghia
    model = DDP(model, device_ids=[local_rank])
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        # moi rank doc mot shard du lieu rieng
        for X, y in make_dataloader(rank):
            optimizer.zero_grad()
            loss = torch.nn.functional.cross_entropy(
                model(X.to(device)), y.to(device))
            loss.backward()        # DDP tu dong all-reduce gradient
            optimizer.step()
    if rank == 0:
        torch.save(model.module.state_dict(), "/mnt/models/net.pt")

distributor = TorchDistributor(num_processes=8,
                               local_mode=False, use_gpu=True)
distributor.run(train_fn, lr=1e-3, epochs=10)
