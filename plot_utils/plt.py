import matplotlib.pyplot as plt 


def custom_plt_plot(fig, title, grid, title_fontsize, xlabel, xlabel_fontsize, ylabel, ylabel_fontsize):
    fig.suptitle(title, fontsize=title_fontsize)
    plt.xlabel(xlabel, fontsize=xlabel_fontsize)
    plt.ylabel(ylabel, fontsize=ylabel_fontsize)
    plt.grid(grid)


