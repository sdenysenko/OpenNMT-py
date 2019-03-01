import matplotlib.pyplot as plt

def save_plot(data, src_list, pred_list, number):

	fig, ax = plt.subplots(figsize=(int(len(src_list) * 1.2 + 1), int(len(pred_list) + 1)))
	data = data[:len(pred_list)]
	for i in range(len(data)):
		data[i] = data[i][:len(src_list)]
	im = ax.imshow(data, aspect='auto', origin='lower', interpolation='none', vmin=0, vmax=1)
	fig.colorbar(im, ax=ax)
	xlabel = 'Source sentence'
	plt.gca().invert_yaxis()
	plt.xlabel(xlabel)
	plt.ylabel('Prediction sentence')
	plt.xticks(range(len(src_list)), src_list, rotation=-10)
	plt.yticks(range(len(pred_list)), pred_list)
	plt.tight_layout(pad=1)
	plt.rcParams['font.size'] = 12
	plt.savefig('/home/user/ClonedRepo/OpenNMT-py/plotter/data/' + str(number) + '.png')
