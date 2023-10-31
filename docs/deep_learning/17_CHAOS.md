# 杂

# **Neural Network**

卷积池化前后大小对比

输入大小: $W\times W$, kernel_size=F, stride=S, padding=P

输出大小 $N = \frac{W-F+2P}{S}+1$

# Dropout

一种正则化方法，用于防止深度神经网络过拟合，其主要思想是在训练过程中随机选择神经元进行忽略，从而可以减少神经元之间的依赖性，强制使网络更多地依靠其他神经元来进行预测

# Problem

为什么感觉这些著名的神经网络的设计具有一定的主观性，想设计几个卷积层就设计几个，也没有什么依据

# Pytorch

卷积

```python
nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, 
          output_padding=0, groups=1, bias=True)
```

反卷积: dilation(int or tuple, optional) – 卷积核元素之间的间距

```python
nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride=1, padding=0, 
									 output_padding=0, groups=1, bias=True, dilation=1)
```

双线性插值

```python
def bilinear_kernel(in_channels, out_channels, kernel_size):
    factor = (kernel_size + 1) // 2
    if kernel_size % 2 == 1:
        center = factor - 1
    else:
        center = factor - 0.5
    og = (torch.arange(kernel_size).reshape(-1, 1),
          torch.arange(kernel_size).reshape(1, -1))
    filt = (1 - torch.abs(og[0] - center) / factor) * \
           (1 - torch.abs(og[1] - center) / factor)
    weight = torch.zeros((in_channels, out_channels,
                          kernel_size, kernel_size))
    weight[range(in_channels), range(out_channels), :, :] = filt
    return weight

conv_trans = nn.ConvTranspose2d(3, 3, kernel_size=4, padding=1, stride=2,
                                bias=False)
conv_trans.weight.data.copy_(bilinear_kernel(3, 3, 4));
```