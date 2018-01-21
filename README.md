# Analysator
This project helps to collect load profiles of heating systems in Germany and analyses it. 
It is developed with Python 2.7 using Python(x,y) 2.7.10.0


The main function uses pyxlsDownloader to search for Download-elements of a homepage. 
Then it scrapes for downlinks in a second step. After it, it downloads the link chossed.
In a third step it uses the Analyser to analyse the Data and plots a part of the data.
After that the Analyser uploads the data to google Drive using an API client. The google upload bases on the module of
google_drive_util.py on github:https://gist.github.com/lheric/876a924c5d77bde0f62526c7fa6ad846 .
To use the API client the user has to generate the 'client_secrets.json' from https://console.developers.google.com/ . 

The code of the main function is only rudimental. In further steps a gui will be provided. 
So, the user can enter a homepage of his wish and can choose more than one download link.
After that he can choose the columns for the data-analysis and which data he wants to plot.
He can edit the plot and save the edited plot.
But this will be in a further step.

