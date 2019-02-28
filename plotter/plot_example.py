import matplotlib.pyplot as plt

def save_plot(data, original_text, prediction_text, number):

	plt.pcolormesh(data)
	plt.ylabel(prediction_text)
	plt.xlabel(original_text)
	plt.plot()
	plt.savefig('/home/user/ClonedRepo/OpenNMT-py/plotter/data/spectr' + number + '.png')
