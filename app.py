from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv("covid_data.csv")
    df["Death_Rate"] = (df["Deaths"] / df["Confirmed"]) * 100
    df["Recovery_Rate"] = (df["Recovered"] / df["Confirmed"]) * 100

    
    top = df.sort_values(by="Confirmed", ascending=False).head(6)
    plt.figure()
    plt.bar(top["Country"], top["Confirmed"])
    plt.title("Top Countries - Confirmed Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/confirmed.png")
    plt.close()

    # ===== GRAPH 2: Death Rate =====
    plt.figure()
    plt.bar(top["Country"], top["Death_Rate"])
    plt.title("Death Rate (%) by Country")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/death_rate.png")
    plt.close()

    # ===== GRAPH 3: Recovery Rate =====
    plt.figure()
    plt.bar(top["Country"], top["Recovery_Rate"])
    plt.title("Recovery Rate (%) by Country")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/recovery_rate.png")
    plt.close()

    return render_template(
        "index.html",
        tables=top.to_dict(orient="records")
    )

if __name__ == "__main__":
    app.run(debug=True)
