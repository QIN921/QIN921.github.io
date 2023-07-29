# MoblieNets: Efficient Convolutional Neural Networks for Mobile Vision Applications

![Untitled](Untitled%203.png)

通过将M个 $D_k \times D_k$ 的卷积核分别作用于输入的各个通道一次，再用 1x1 的卷积核将M个通道的运算结果以一定的权重加起来

传统的神经网络回将N组M个 $D_k \times D_k$ 卷积核作用于输入的M个通道一次，然后直接将M个卷积结果加起来

Mobilenets的处理方式相当于让N组的卷积核从没啥关系变成了成比例的了，但考虑到非线性层，输出并不会线性相关

![Untitled](Untitled%204.png)