
"""
Playing around with some visualization
"""

# Plot_anat
# https://nilearn.github.io/modules/generated/nilearn.plotting.plot_anat.html#nilearn.plotting.plot_anat

nilearn.plotting.plot_anat(anat_img=<nilearn.plotting.img_plotting._MNI152Template object>, 
	cut_coords=None, 
	output_file=None, 
	display_mode='ortho', 
	figure=None, 
	axes=None, 
	title=None, 
	annotate=True, 
	threshold=None, 
	draw_cross=True, 
	black_bg='auto', 
	dim=False, 
	cmap=<matplotlib.colors.LinearSegmentedColormap object>, 
	vmin=None, 
	vmax=None, 
	**kwargs)