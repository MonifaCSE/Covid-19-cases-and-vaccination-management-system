from flask import Flask,render_template,request,redirect,flash,session
from werkzeug.utils import secure_filename


import mysql.connector
import os

app=Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'static/upload/'

conn=mysql.connector.connect(host="localhost",user="root",password="",database="covid management")
cursor=conn.cursor()


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


@app.route('/ahome')
def ahome():
    return render_template('ahome.html')
@app.route('/uhome')
def uhome():
    return render_template('uhome.html')

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

@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/')


#..............................Superadmin panel............................................

#..................superadmin login........

@app.route('/slogin')
def slogin():
    if 'id' in session:
        return redirect('/shome')
    else:
        return render_template('slogin.html')


@app.route('/shome')
def shome():
    if 'id' in session:
        return render_template('shome.html')
    else:
        return redirect('/')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute(
        """SELECT * FROM `superadmin` WHERE `Email` LIKE '{}' AND `Password` LIKE '{}'"""
        .format(email, password))
    sadmin = cursor.fetchall()

    if (sadmin):
        if len(sadmin) > 0:
            session['id'] = sadmin[0][0]
            return redirect('/shome')

    return redirect('/')

#........hospital registration.................

@app.route('/shospital')
def shospital():
    if 'id' in session:
         cursor.execute("SELECT* FROM `hospital`")
         myshospital=cursor.fetchall()
         return  render_template('shospital.html',shospital=myshospital)
    else:
        return redirect('/')


@app.route('/view_image', methods=['GET', 'POST'])
def view_image():
        return redirect('/shospital')

@app.route('/insert', methods=['POST'])
def insert():
        if request.method == "POST":
            flash("Data Inserted Successfully")
            hospitalname = request.form['Hospital_name']
            district = request.form['District']
            address = request.form['Address']
            email = request.form['Email']
            password = request.form['Password']
            phone = request.form['Phone']

            file1 = request.files['file1']
            filename1 = secure_filename(file1.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))


            cursor.execute(
                "INSERT INTO HOSPITAL (Hospital_name,District,Address,Email,Password,Phone,image) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (hospitalname,district,address,email,password,phone,filename1))
            conn.commit()
            return redirect('/shospital')

@app.route('/update', methods=['GET', 'POST'])
def update():
        if request.method == "POST":

            hospitalid = request.form['Hospital_id']
            hospitalname = request.form['Hospital_name']
            district = request.form['District']
            address = request.form['Address']
            email = request.form['Email']
            password = request.form['Password']
            phone = request.form['Phone']

            file1 = request.files['file1']
            filename1 = secure_filename(file1.filename)
            if filename1 == '':
                filename1 = request.form['file11']
            else:
                file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))



            cursor.execute("""UPDATE hospital 
            SET  Hospital_name=%s, District=%s ,Address=%s ,Email=%s ,Password=%s ,Phone=%s ,image=%s WHERE Hospital_id=%s""", (hospitalname, district, address,email,password,phone,filename1,hospitalid))
            flash("Data Updated Successfully")
            conn.commit()

            return redirect('/shospital')

@app.route('/deletee/<string:hospitalid>', methods=['POST', 'GET'])
def delete(hospitalid):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM hospital WHERE Hospital_id=%s", (hospitalid,))
        conn.commit()
        return redirect('/shospital')



@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":

        hospital = request.form['Hospital']
        cursor.execute("SELECT * FROM hospital WHERE Hospital_name LIKE %s OR District LIKE %s OR Address LIKE %s", (hospital,hospital,hospital))
        myhospital = cursor.fetchall()

        if (len(myhospital) == 0 and hospital == 'all') or len(hospital)==0:
            cursor.execute("SELECT * FROM hospital")

            myhospital = cursor.fetchall()
        return render_template('shospital.html', shospital=myhospital)
    return redirect('/shospital')



#.............Hospital Request.............




@app.route('/hospitalrequest')
def hospitalrequest():
    if 'id' in session:
         cursor.execute("SELECT* FROM `hospital_request`")
         hospitalr=cursor.fetchall()
         return render_template('hospitalrequest.html',hospitalrequest=hospitalr)
    else:
        return redirect('/')



@app.route('/insertr', methods=['POST'])
def insertr():
        if request.method == "POST":
            flash("Data Inserted Successfully")
            hospitalname = request.form['Hospital_name']
            district = request.form['District']
            address = request.form['Address']
            email = request.form['Email']
            password = request.form['Password']
            phone = request.form['Phone']

            file1 = request.files['file1']
            filename1 = secure_filename(file1.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))


            cursor.execute(
                "INSERT INTO HOSPITAL_REQUEST (Hospital_name,District,Address,Email,Password,Phone,image) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (hospitalname,district,address,email,password,phone,filename1))

            conn.commit()
            return redirect('/hospitalrequest')

@app.route('/approver', methods=['POST'])
def approver():
        if request.method == "POST":

            requestid = request.form['Request_id']
            hospitalname = request.form['Hospital_name']
            district = request.form['District']
            address = request.form['Address']
            email = request.form['Email']
            password = request.form['Password']
            phone = request.form['Phone']

            file1 = request.files['file1']
            filename1 = secure_filename(file1.filename)
            if filename1 == '':
                filename1 = request.form['file11']
            else:
                file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))

            cursor.execute(
                "INSERT INTO HOSPITAL (Hospital_name,District,Address,Email,Password,Phone,image) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (hospitalname, district, address, email, password, phone, filename1))
            cursor.execute("""UPDATE hospital_request 
                                    SET  Hospital_name=%s, District=%s ,Address=%s ,Email=%s ,Password=%s ,Phone=%s ,image=%s ,Approval="Approved" WHERE Request_id=%s""",
                           (hospitalname, district, address, email, password, phone, filename1, requestid))

            flash("Accepted")
            conn.commit()

            return redirect('/hospitalrequest')

@app.route('/deleter/<string:requestid>', methods=['POST', 'GET'])
def deleter(requestid):
        flash("Request has been Rejected")

        cursor.execute("""UPDATE hospital_request  SET  Approval="Rejected" WHERE Request_id=%s""",(requestid,))

        conn.commit()
        return redirect('/hospitalrequest')


#.....................................superadmin profile............

@app.route('/sprofile')
def sprofile():
    if 'id' in session:
       s=session['id']
       cursor.execute("SELECT * FROM superadmin WHERE id = '"+str(s)+"'")
       p = cursor.fetchone()

       return render_template('sprofile.html', p=p)

    else:
        return redirect('/')


@app.route('/seprofile', methods=['POST', 'GET'])
def seprofile():
    if request.method == "POST":

        id = request.form['id']
        email = request.form['Email']
        password = request.form['Password']
        phone = request.form['Phone']

        file1 = request.files['file1']
        filename1 = secure_filename(file1.filename)
        if filename1 == '':
            filename1 = request.form['file11']
        else:
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))

        cursor.execute("""UPDATE superadmin 
        SET   Email=%s ,Password=%s ,Phone=%s ,image=%s WHERE  id=%s""",
                       (email, password, phone, filename1, id))
        flash("Data Updated Successfully")
        conn.commit()

        return redirect('/sprofile')


if __name__=="__main__":
    app.run(debug=True)