import torch
import torch.nn as nn


class ResBlock(nn.Module):
    def __init__(self, in_channel, mid_channel, out_channel, p = 0.3):
        super(ResBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channel, mid_channel, kernel_size = 3, padding = 1)
        self.conv2 = nn.Conv2d(mid_channel, out_channel, kernel_size = 3, padding = 1)
        # self.nonlinear1 = nn.LeakyReLU(0.1)
        self.nonlinear1 = nn.ReLU()
        self.Dropout = nn.Dropout(p)
        self.BN1 = nn.BatchNorm2d(num_features=mid_channel)
        self.BN2= nn.BatchNorm2d(num_features=out_channel)
        
    def forward(self, x):
        out1 = self.BN1(self.conv1(x))
        out2 = self.nonlinear1(out1)
        out3 = self.BN2(self.conv2(self.Dropout(out2)))
        out = x + out3
        
        return out

class self2self(nn.Module):
    def __init__(self, in_channel,out_channel, p):
        super(self2self, self).__init__()
        
        self.n_blks = 10
        self.channel_size = 64
        layers = [ResBlock(self.channel_size, self.channel_size, self.channel_size,p=p)]
        for i in range(self.n_blks-1):
            layers.append(ResBlock(self.channel_size, self.channel_size, self.channel_size,p=p))
        
        self.convs = nn.Sequential(*layers)
        self.conv_first = nn.Conv2d(in_channel, self.channel_size, kernel_size = 3, padding = 1)
        self.conv_last = nn.Conv2d(self.channel_size, out_channel, kernel_size = 3, padding = 1)
        self.conv_last2 = nn.Conv2d(out_channel, out_channel, kernel_size = 1)
        self.sig = nn.Sigmoid()
        self.relu = nn.ReLU()

    def forward(self, x):
        
        out1 = self.conv_first(x)
        out2 = self.convs(out1)
        out2 += out1
        out3 = self.conv_last(out2)
        out = self.conv_last2(out3)

        out = self.relu(out)
                
        return out
