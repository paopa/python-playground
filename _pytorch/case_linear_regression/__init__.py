import torch
import matplotlib.pyplot as plt


# Create input data x as a sequence from -5 to 5 with step size 0.1
# view(-1, 1) reshapes the 1D tensor into a 2D tensor with one column
# -1 tells PyTorch to automatically calculate the first dimension based on the total size
# This creates a matrix of shape (n_samples, 1) which is the standard format for linear regression
x = torch.arange(-5, 5, 0.1).view(-1, 1)

# Generate y actual values
noise = torch.randn(x.size())
slope = -5
intercept = 4 * noise
y = slope * x + intercept
print(f"the slope is {slope} and the intercept is {intercept.mean()}")


def predict(x, w, b):
    return x * w + b


def criterion(y, y_pred):
    # Calculate the Mean Squared Error (MSE) between the actual and predicted values
    return torch.mean((y - y_pred) ** 2)


w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)


# Define the learning rate
lr = 0.1
epochs = 20

# For drawing the loss curve
losses = []


def forward_propagation(x, w, b):
    # Calculate the predicted values
    y_pred = predict(x, w, b)
    # Calculate the loss
    loss = criterion(y, y_pred)
    return loss


for i in range(epochs):
    # Forward Propagation
    loss = forward_propagation(x, w, b)
    losses.append(loss.item())

    # Backward Propagation
    loss.backward()

    # Update the weights and biases
    w.data -= lr * w.grad
    b.data -= lr * b.grad

    # Reset the gradients to zero
    w.grad.zero_()
    b.grad.zero_()

    print(
        f"Epoch {i + 1}/{epochs}, Loss: {loss.item():.4f}, w: {w.item():.4f}, b: {b.item():.4f}"
    )


# Plot the loss curve
def plot_loss_curve():
    plt.plot(losses, label="Batch Gradient Descent")
    plt.xlabel("Epoch")
    plt.ylabel("Cost/Total Loss")
    plt.legend()
    plt.show()


# Plot the data and the model's predictions
def plot_data_and_predictions():
    plt.scatter(x, y, label="Actual Data")
    plt.plot(x, predict(x, w, b).detach().numpy(), "-r", label="Model Predictions")
    plt.legend()
    plt.show()


# plot_loss_curve()
plot_data_and_predictions()
