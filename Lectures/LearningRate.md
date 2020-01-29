# Learning rate
Learning rate defines the size of the step the gradient descent does on every iteration. There are several strategies how to define learning rate:

1. The first and the simplest strategy is to assign a single value to the learning rate which means that all layers will be trained with the same learning rate value.

2. The second one is to use discrimative learning rate. The idea is originally taken from [the FastAI lectures](https://course.fast.ai/videos/?lesson=5) (17:00). It is mostly used in combination with the transfer learning. When the transfer learning is used it is assumed that the first layers of the model are trained well and require less training. Therefore, we can use smaller learning rate in the first layer of the model and increaze the learning rate as we go deeper in the model.


# Learning rate in FastAI
1. `<learner>.fit(1, 1e-3)` - every layer gets the same lr of `1e-3`.
2. `<learner>.fit(1, slice(1e-3))` - the final layers get the specified lr `(1e-3)` where all the other layers get the specified lr divided by `3` so `1e-3/3`.
3. `<learner>.fit(1, slice(1e-5, 1e-3))` - the final layers will get `1e-3`, the first layers will get `1e-5` and the other layers will get `lrs` which are multiplicatively equally spread between the two.