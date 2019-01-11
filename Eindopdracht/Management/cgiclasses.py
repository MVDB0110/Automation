import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

class HorizontalBar:

    def __init__(self,title,xlabel,hosts,percentage,color):
        self.title = title # Titel voor horizontalbar
        self.hosts = hosts # Alle minions
        self.xlabel = xlabel # Het label voor de x-as
        self.percentage = percentage # Percentage van de minions over het aangegeven object
        self.color = color # Kleur van de staven

    def plotPNG(self,outputFile):
        plt.rcdefaults() # Initieer plot
        fig, ax = plt.subplots()  # Maak figuur
        ybar = np.arange(len(self.hosts))  # Vraag getal van objecten over y-as

        ax.barh(self.hosts, self.percentage, align='center', color=self.color, ecolor='black')  # Zet waarden figuur 1
        ax.set_yticks(ybar)  # Maak evenveel posities op y-as als objecten in minions
        ax.set_yticklabels(self.hosts)  # Zet hostnames op y-as
        ax.set(xlim=[0, 100])  # Zet x-as van 0 tm 100
        ax.invert_yaxis()
        ax.set_xlabel(self.xlabel) # Zet x-label op x-as
        ax.set_title(self.title) # Zet titel op plot

        plt.savefig(os.path.join(os.path.dirname(__file__), outputFile))  # Sla grafiek op