import numpy as np
import torch
from torch.utils.data import Dataset


class BCIC4_2A(Dataset):
    def __init__(self, args, phase):
        self.args = args
        self.load_data(phase)
        self.torch_form()
        self.reshape_data()

    def load_data(self, phase):
        if self.args.get_prediction:
            self.X = np.load(f"./data_loader/dataset/bcic4-2a/{phase}/S{self.args.subject:02}_X.npy")
        elif self.args.evaluation:
            self.y = np.load(f"./data_loader/dataset/bcic4-2a/{phase}/S{self.args.subject:02}_y.npy")
        else:
            self.X = np.load(f"./data_loader/dataset/bcic4-2a/{phase}/S{self.args.subject:02}_X.npy")
            self.y = np.load(f"./data_loader/dataset/bcic4-2a/{phase}/S{self.args.subject:02}_y.npy")

    def torch_form(self):
        if self.args.get_prediction:
            self.X = torch.Tensor(self.X)
        elif self.args.evaluation:
            self.y = torch.LongTensor(self.y)
        else:
            self.X = torch.Tensor(self.X)
            self.y = torch.LongTensor(self.y)

    def reshape_data(self):
        if not self.args.evaluation:
            self.X = self.X.unsqueeze(dim=1)

    def __len__(self):
        if not self.args.evaluation:
            return len(self.X)
        else:
            return len(self.y)

    def __getitem__(self, idx):
        if self.args.get_prediction:
            sample = self.X[idx]
            return sample
        elif self.args.evaluation:
            sample = self.y[idx]
            return sample
        else:
            sample = [self.X[idx], self.y[idx]]
            return sample
