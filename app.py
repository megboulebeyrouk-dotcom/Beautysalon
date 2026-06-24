from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 1. شاشة البداية: اختيار اللغة والاسم
@app.route("/", methods=["GET", "POST"])
def language_selection():
    if request.method == "POST":
        user_name = request.form.get("username", "Guest")
        lang = request.form.get("lang", "en")
        return redirect(url_for(f'home_{lang}', name=user_name))
    return render_template("language.html")

# 2. الواجهة الرئيسية الإنجليزية
@app.route("/en")
def home_en():
    name = request.args.get("name", "Guest")
    return render_template("index_en.html", username=name)

# 3. الواجهة الرئيسية العربية
@app.route("/ar")
def home_ar():
    name = request.args.get("name", "Guest")
    return render_template("index_ar.html", username=name)

# 4. صفحة الخدمات الإنجليزية
@app.route("/booking/en")
def booking_en():
    return render_template("booking_en.html")

# 5. صفحة الخدمات العربية
@app.route("/booking/ar")
def booking_ar():
    return render_template("booking_ar.html")

# 6. صفحة نجاح الحجز
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)