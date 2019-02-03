import numpy as np
import matplotlib.pyplot as plt

def __softmax(x):
	exp = np.exp(x)
	return exp/np.sum(exp, axis=1, keepdims=True)

def __compute_meshgrid(x, y):
	x_min, x_max, y_min, y_max = x[:, 0].min(), x[:, 0].max(), x[:, 1].min(), x[:, 1].max()
	x1, x2 = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
	x_mesh = np.array([x1.ravel(), x2.ravel()]).T
	return x1, x2, x_mesh

def plot_data_and_predictions_3d_in_2d(x, y, is_binary, nn=None, threshold=0.0, figsize=(12,6), s=15, cmap=plt.cm.viridis):
	plt.figure(figsize=figsize)
	ax = plt.subplot(1, 2, 1)
	plt.scatter(x[:,0], x[:,1], c=list(np.array(y).ravel()), s=s, cmap=cmap)

	if nn is not None:
		plt.subplot(1, 2, 2, sharex=ax, sharey=ax)

		x1, x2, x_mesh = __compute_meshgrid(x, y)
		y_mesh = nn.predict(x_mesh)
		y_mesh = np.where(y_mesh <= threshold, 0, 1) if is_binary else np.argmax(__softmax(y_mesh), axis=1)

		plt.scatter(x[:,0], x[:,1], c=list(np.array(y).ravel()), s=s, cmap=cmap)
		plt.contourf(x1, x2, y_mesh.reshape(x1.shape), cmap=cmap, alpha=0.5)