# Heating-Analysation
This project helps to collect load profiles of heating systems in Germany and analyses it. 


The main function uses pyxlsDownloader to search for Download-elements of a homepage. 
Then it downloads the link in a second step.
In a third step it uses the Analyser to analyse the Data and plot a part of the data.
In a third step the Analyser uploads the Data to Google Drive using an API client. The google upload bases on the module of
google_drive_util.py on github:https://gist.github.com/lheric/876a924c5d77bde0f62526c7fa6ad846 .
To use the API client the users has to generate 'client_secrets.json' from https://console.developers.google.com/ . 

The code of the main function is only rudimental. In further steps a gui will be provided. 
So, the user can enter a homepage of his wish and can choose more than von download link.
After that he can choose the columns for the data-analysis and which data he wants to plot.
But this will be in a further step

