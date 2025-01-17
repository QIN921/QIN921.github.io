# AlexNet: ImageNet Classification with Deep Convolutional Neural Networks

# **ReLU Nonlinearity**

$$
f(x)=max(0,x)
$$

# **传统的饱和非线性**

$$
f(x) = \frac{1}{1+e^{-x}}
$$

$$
tanh(x) = \frac{e^x+e^{-x}}{e^x+e^{-x}}
$$

优点：

- 解决梯度消失
- 加快收敛

缺点：

- 可能造成神经元死亡

# **Local Response Normalization**

$$
b_{x, y}^{i}=a_{x, y}^{i} /\left(k+\alpha \sum_{j=\max (0, i-n / 2)}^{\min (N-1, i+n / 2)}\left(a_{x, y}^{j}\right)^{2}\right)^{\beta}
$$

局部响应归一化，增大对比度，使大的相对小的更大，

lateral inhibition 横向抑制，抑制小的的影响

# **Reducing Overfitting**

由于参数过多，所以很容易对训练集过拟合

## **Data Argumentation**

人为增多数据集，下采样后256x256的图片选出224x224作为输入，因此可以图像平移与水平翻转，从而得到32x32x2=2048张图片

改变图像强度，进行主成分分析PCA，然后将主成分加倍

## **Dropout**

是神经网络中比较常用的抑制过拟合的方法。在神经网络中Dropout通过修改神经网络本身结构来实现，对于某一层的神经元，通过定义的概率将神经元置为0，这个神经元就不参与前向和后向传播，就如同在网络中被删除了一样，同时保持输入层与输出层神经元的个数不变，然后按照神经网络的学习方法进行参数更新。在下一次迭代中，又重新随机删除一些神经元（置为0），直至训练结束