from flask import Flask,render_template,request,redirect,url_for
from analysis import get_countries
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/country/")
def get_update():
    c = get_countries()
    return render_template("coun.html",country = c)  #country = key, c = value

@app.route("/pie_chart/")
def get_pie():
try:
    title_rating = df.groupby("Country/Region").sum().sort_values(by="Confirmed",ascending=False)['Confirmed'][:10]
    rating_labels = title_rating.sort_values().index 
    rating_counts = title_rating.sort_values()
    plt.figure(1, figsize=(10,20))
    cmap = plt.get_cmap('Spectral')
    colors = [cmap(i) for i in np.linspace(0, 1, 8)]
    plt.subplot( aspect=1, title='Total Confirmed cases by percentage')
    type_show_ids = plt.pie(rating_counts, labels=rating_labels, autopct='%1.1f%%', shadow=True, colors=colors)
    plt.legend(loc=2)
    plt.show()

except Exception as e:
    return "ERROR"




@app.route("/getdetails/",methods=['GET','POST'])
def get_details():
    if request.method == "POST":
        c = request.form.get("country")
        mont = request.form.get("month")
        t = request.form.get("type")
        df = pd.read_csv("/Users/navendrasingh/Documents/d/datasciece /covid_19_data.csv")
        fig = plt.figure(figsize=(11,5),facecolor="black")
        ax = fig.add_axes([0,0,1,1],facecolor="black")
        temp = df[df['Country/Region'] == c]
        v = temp[temp['ObservationDate'].apply(lambda x : True if x.split("/")[0] == (str(mont)) else False)][t].values
        i = temp[temp['ObservationDate'].apply(lambda x : True if x.split("/")[0] == (str(mont)) else False)]['ObservationDate'].values
        sns.barplot(i,v,ax=ax)
        for p,text in zip(ax.patches,v):
            x = p.get_x()
            h = p.get_height() + 0.5
            plt.text(x,h,text,fontsize=10,color="white",rotation=90)
        ax.set_xticklabels(i,rotation=90,color="white")
        ax.set_yticklabels(ax.get_yticks(),color="white")
        plt.savefig(f"static/images/{c}{mont}{t}.png",bbox_inches="tight",dpi=72,facecolor="black")
        return render_template("show.html",total=sum(v),c=c,m=mont,t=t)
    elif request.method == "GET":
        return redirect(url_for("index"))




app.run(host="localhost",port=1234,debug=True)