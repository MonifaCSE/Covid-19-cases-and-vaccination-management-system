from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/slogin')
def slogin():
    return render_template('slogin.html')

@app.route('/alogin')
def alogin():
    return render_template('alogin.html')

@app.route('/rlogin')
def rlogin():
    return render_template('rlogin.html')
@app.route('/ulogin')
def ulogin():
    return render_template('ulogin.html')
@app.route('/uregister')
def uregister():
    return render_template('uregister.html')
@app.route('/services')
def services():
    return render_template('service.html')
@app.route('/rhome')
def rhome():
    return render_template('rhome.html')
@app.route('/shome')
def shome():
    return render_template('shome.html')

@app.route('/ahome')
def ahome():
    return render_template('ahome.html')
@app.route('/uhome')
def uhome():
    return render_template('uhome.html')
@app.route('/shospital')
def shospital():
    return render_template('shospital.html')
@app.route('/hospitalrequest')
def hospitalrequest():
    return render_template('hospitalrequest.html')
@app.route('/sprofile')
def sprofile():
    return render_template('sprofile.html')
@app.route('/adoctor')
def adoctor():
    return render_template('adoctor.html')
@app.route('/abed')
def abed():
    return render_template('abed.html')
@app.route('/apatient')
def apatient():
    return render_template('apatient.html')

@app.route('/acovid')
def acovid():
    return render_template('acovid.html')

@app.route('/areceptionist')
def areceptionist():
    return render_template('areceptionist.html')
@app.route('/dsalary')
def dsalary():
    return render_template('dsalary.html')
@app.route('/rsalary')
def rsalary():
    return render_template('rsalary.html')
@app.route('/abedallotment')
def abedallotment():
    return render_template('abedallotment.html')
@app.route('/abedrequest')
def abedrequest():
    return render_template('abedrequest.html')
@app.route('/apayment')
def apayment():
    return render_template('apayment.html')
@app.route('/adminprofile')
def adminprofile():
    return render_template('adminprofile.html')
@app.route('/adoze1')
def adoze1():
    return render_template('adoze1.html')
@app.route('/adoze2')
def adoze2():
    return render_template('adoze2.html')
@app.route('/vaccinated')
def vaccinated():
    return render_template('vaccinated.html')
@app.route('/rdoctor')
def rdoctor():
    return render_template('rdoctor.html')
@app.route('/rbed')
def rbed():
    return render_template('rbed.html')
@app.route('/rbedallotment')
def rbedallotment():
    return render_template('rbedallotment.html')
@app.route('/rpatient')
def rpatient():
    return render_template('rpatient.html')
@app.route('/rpayment')
def rpayment():
    return render_template('rpayment.html')
@app.route('/rdoze1')
def rdoze1():
    return render_template('rdoze1.html')
@app.route('/rdoze2')
def rdoze2():
    return render_template('rdoze2.html')
@app.route('/rvaccinated')
def rvaccinated():
    return render_template('rvaccinated.html')
@app.route('/rprofile')
def rprofile():
    return render_template('rprofile.html')
@app.route('/ubed')
def ubed():
    return render_template('ubed.html')
@app.route('/uprofile')
def uprofile():
    return render_template('uprofile.html')

if __name__=="__main__":
    app.run(debug=True)
