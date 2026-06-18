from flask import Flask, request , url_for , render_template
import joblib
model = joblib.load(r'C:\Users\user\OneDrive\Desktop\Data Science\Bike-Price-Prediciton\model\model.lb')
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/project')
def project():
    return render_template('project.html')
@app.route('/history')
def history():
    return render_template('history.html')
@app.route('/project',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        brand_name =request.form['brand_name']
        owner =int(request.form['owner'])
        age =int(request.form['age'])
        power =int(request.form['power'])
        kms_driven =int(request.form['kms_driven'])
        brand_dict = {'TVS':1,'Royal Enfield':2,'Triumph':3,'Yamaha':4,'Honda':5,'Hero':6,'Bajaj':7,
              'Suzuki':8,'Benelli':9,'KTM':10,'Mahindra':11,'Kawasaki':12,'Ducati':13,'Hyosung':14,
              'Harley-Davidson':15,'Jawa':16,'BMW':17,'Indian':18,'Rajdoot':19,'LML':20,'Yezdi':21,'MV':22,'Ideal':23
}
        brand_name = brand_dict.get(brand_name)
        pred = model.predict([[kms_driven,	owner,	age,	power,	brand_name]])
        round_pred = int(round(pred[0]))
        print('prediction :->>>',round_pred)
    
    return render_template('project.html',prediction = round_pred)

if __name__ == '__main__':
    app.run(debug=True)