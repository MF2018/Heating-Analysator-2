# Analysator
This project helps to collect load profiles of heating energy systems in Germany and analyse them. 
It is developed with Python 2.7 using Python(x,y) 2.7.10.0.
This application requires a google account including google drive. 


The main function use the function downloader to search for downloadable elements of a homepage. 
Then it scrapes for download links in a second step. After it, it downloads the link chose.
In a third step the main function uses the function Analyser to analyse the data and generates a plot of the selected data.
After that the Analyser uploads the data to google Drive using an API client. The google upload bases on the module of
google_drive_util.py on github:https://gist.github.com/lheric/876a924c5d77bde0f62526c7fa6ad846 .
For using the API client the user has to generate the 'client_secrets.json' from https://console.developers.google.com/ . 

The code of the main function is only rudimental. In further steps a GUI will be provided. 
So, the user can enter a homepage of his choice and can choose more than one download link.
After that he can choose the columns for the data-analysis and which data he wants to plot.
He can edit the plot and save the edited plot.
But this will be in a further step.

