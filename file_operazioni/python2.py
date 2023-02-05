from flask import Flask, request

app = Flask(__name__)
@app.route("/somma", methods=["POST"])

def sommaPost():

    try:
        txtA = int(request.form.get("txtA"))
        txtB = int(request.form.get("txtB"))
        c = txtA + txtB
        return str(c)

    except:
        return "Errore xD"

@app.route("/", methods=["GET"])

def homePage():
    return """
    <html>
     <body>
      <form action="/somma" method="POST">
       <label for = "primoNumero"> Primo numero </label>
       <input type="text" id="primoNumero" name="txtA">
       <br>
       <label for = "secondoNumero"> Secondo numero </label>
       <input type="text" id="secondoNumero" name="txtB">
       <br>
       <input type="submit" value="somma">
      </form>
     </body>
    </html>
    """

if __name__ == "__main__":
    app.run()