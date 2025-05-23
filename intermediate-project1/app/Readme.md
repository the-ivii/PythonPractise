## Flask Plot Visualizer
This is a simple Flask web application that generates a random scatter plot using Matplotlib and displays it on a webpage. Useful for learning how to integrate data visualization with Python web apps.

## Features
	•	Dynamically generates a new scatter plot on each request
	•	Saves plots as images in the static/images directory
	•	Displays plots in HTML templates or directly in the browser
	•	Uses Agg backend to support headless environments
## Tech Stack
	•	Python 3
	•	Flask
	•	Matplotlib
	•	NumPy
## Example Output 
<img width="574" alt="Screenshot 2025-05-23 at 4 15 28 PM" src="https://github.com/user-attachments/assets/f8117b81-479f-4295-88e3-ed1967e4bef0" />

## Notes
	•	matplotlib.use("Agg") is used to support image rendering without GUI.
	•	The plot image is overwritten on each request, keeping only the latest version.
