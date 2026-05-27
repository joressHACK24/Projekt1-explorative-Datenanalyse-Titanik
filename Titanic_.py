import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# die letzte Version herunterladen:
path = kagglehub.dataset_download("yasserh/titanic-dataset")

print("Path to dataset files:", path)

dataset_titanik = pd.read_csv("C:/Users/jores/.cache/kagglehub/datasets/yasserh/titanic-dataset/versions/1/Titanic-Dataset.csv")

#print(dataset_titanik.head())

# Hier würde ich gern wissen, welche Columns gibt es in der Dataset
print(dataset_titanik.columns)

# Danach muss ich die generelle Statistik sehen, um zu wissen, was in der Dataset fehlt.
print(dataset_titanik.describe())

# Mit diesen Analysen weiß ich jetzt, dass es die Alter von anderen Leuten fehlt.
# Dann habe ich den Auswahl zwischen die löschung von "N/a" Daten oder ich ersetze mit dem Median
# ich habe mich entschieden , die fehlende Daten zu löschen
# und eine Andere Spalte zu erstellen( name : verwandte( EN: Relative))
print(dataset_titanik["Survived"].value_counts(normalize=True))
dataset_titanik["Relative"] = dataset_titanik["SibSp"] + dataset_titanik["Parch"]

dataset_titanik_clean = dataset_titanik.dropna(subset=["Age"])
print(dataset_titanik_clean["Survived"].value_counts(normalize=True))
# Die Rate von "survived" ist um 2% gestiegen , nachdem ich die fehlende Alter gelöscht habe.

# jetzt habe ich eine Analyse gemacht : würde ich die Geschlecht, und die Klasse der Gäste, von denen
# die Altengruppen nicht registriert werden
print(dataset_titanik[dataset_titanik["Age"].isna()].groupby(["Sex", "Pclass"]).size())
# sex       Pclass      count
# W         1           9
#           2           2
#           3           42
# ---------------------------------
# M         1           21
#           2           9
#           3           94

# Abschließnd würde ich sagen, dass die Dataset fehlen die Altergruppen von Leuten, die in Klasse 3
# waren.( insbesonderes Männer) und auch Männer von Klasse 1. 

# Wie diese Daten die Rate von überlebenden erhöhen haben , könnten wir sagen, dass viele männer von Klasse 3, die wir
# der Alter nicht wissen , hatten nicht überleben.
print(dataset_titanik_clean["Cabin"].head())



fig,axes = plt.subplots(3,4, figsize=(16,10), layout="constrained")
plt.rcParams.update({
    'font.size': 10,          
    'axes.titlesize': 12,     
    'axes.labelsize': 10,    
    'xtick.labelsize': 9,   
    'ytick.labelsize': 9,   
    'legend.fontsize': 8,    
    'legend.title_fontsize': 9
})
axes[2,2].axis("off")
axes[2,3].axis("off")

# Viz1 : visualisieren wir Anzahl der überlebenden nach Geschlecht

sns.barplot( data = dataset_titanik_clean, x ="Sex", y ="Survived", hue="Sex", ax= axes[0,0])
axes[0,0].set_title("Anzahl der Überlebenden pro Geschlecht", fontsize=5)

# Viz2 : vizualisieren wir die Anzahl der überlebenden pro Klasse( Eine Graphik für weiblich und eine
#andere für Männlich)

sns.barplot( data = dataset_titanik_clean, x ="Pclass", y ="Survived", hue="Sex",ax= axes[0,1])
axes[0,1].set_title("Anzahl der Überlebenden pro Klasse mit Farbton über das Geschlecht", fontsize=5)



# Viz3 : vizualisierung von der Verteilung des Alters von Nicht-Überlebenden im  der Vergleich zum Alter 
# der Überlebenden

sns.kdeplot( data = dataset_titanik_clean, x="Survived", y="Age", ax= axes[0,2])
axes[0,2].set_title("Verteilung des Alters der Unüberlebenden vs des Alters der Nicht-Überlebenden", fontsize=5)




#Viz 4: vizualisieren wir die Auswirkungen der Größe der Familien auf das Überleben
data_titanik_heatmap = dataset_titanik_clean.drop(columns=["Name", "Embarked","Ticket", "PassengerId", "Cabin"] )
sns.countplot(data= dataset_titanik_clean, x="Relative", hue="Survived", ax= axes[0,3])
axes[0,3].set_title("Auswirkung der Größe der Familie auf das Überleben", fontsize=5)




#Viz5: Die überlebensbezogene Varaiable
data_titanik_heatmap["Sex"] = data_titanik_heatmap["Sex"].map({"male":1, "female":0})
sns.heatmap(data= data_titanik_heatmap.corr(), ax= axes[1,0])
axes[1,0].set_title("Die überlebensbezogene Varaiable", fontsize=5)



data_titanik_clean_embarked = dataset_titanik_clean.dropna(subset="Embarked")
#viz6: eine Beziehung zwischen Embarked, Survived und Pclass
sns.barplot(data_titanik_clean_embarked, x="Embarked", y= "Survived", hue="Pclass", ax= axes[1,1])
axes[1,1].set_title("Beziehung zwischen: Embarked, Survived und Pclass", fontsize=5)



#viz7: Alter nach Geschlecht
sns.histplot(dataset_titanik_clean, x="Age", hue="Sex", ax= axes[1,2])
axes[1,2].set_title("Alter nach geschlecht", fontsize=5)



#viz8: verifizierung die Koherenz zwischen Preise und Klasse
sns.boxplot(dataset_titanik_clean, x="Pclass", y="Fare", ax= axes[1,3])
axes[1,3].set_title("verifizierung die Koherenz zwischen Preise und Klasse", fontsize=5)


#viz9: Überlebenden nach Ticketpreis
sns.kdeplot(dataset_titanik_clean, x="Fare", hue="Survived", ax= axes[2,0])
axes[2,0].set_title("Überlebenden nach Ticketpreis", fontsize=5)


#viz5: Fare pro einschiffung
sns.boxplot(data_titanik_clean_embarked, x="Embarked", y="Fare", ax= axes[2,1])
axes[2,1].set_title("Fare pro Embarked", fontsize=5)
plt.savefig("visualisierung_dataset_titanik.png")
plt.show()







