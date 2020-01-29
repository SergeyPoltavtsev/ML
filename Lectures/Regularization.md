# Regularization


## Weight decay
Weight decay is used to penalize complexity of the model and it is one of the techniques to prevent model overfitting.

Some parameters can be positive and some can be negative and they can compensate each other if we take simple sum of them. Therefore, we will use sum of squared or sum absolute values. 

The sum of squared of the parameters will be added to the loss function. The newly introduced term will increase the loss value on every iteration forcing gradient decent to optimize with respect to the added term. However, the value can be very big and in that case the only optimal solution for finding best parameters might be to set all of them to 0. Therefore, to control the magnitude of that value it will be multiplied by a hyperparameter `wd` (weight decay). Higher `wd` penalizes more which results in slower learning pace and under-fitting. Lower `wd` might not be able to penalize parameters enough which results in over-fitting.

A good starting value for `wd` is 0.1 which works well for a lot of cases.

TODO: explain how does the new term affects the gradient


## Dropout
The idea is to remove temporary a certain amount of activation at every layer one batch pass. The probabily to throw away an activation is defined by `p`. A common value for `p` is `0.5`.

## Batch normalization
