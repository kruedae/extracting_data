import pandas as pd

def plot_img(img)
    
    # Create a figure and subplot
    fig, ax = plt.subplots()

    # Plot the image
    image = ax.imshow(data_array, cmap='inferno', origin='lower')

    # Add a colorbar for the intensity scale
    cbar = ax.figure.colorbar(image, ax=ax)


    # Show the plot
    plt.show()
