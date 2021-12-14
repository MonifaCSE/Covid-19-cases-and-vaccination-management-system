from flask import Flask,render_template,request,redirect,flash,session
from werkzeug.utils import secure_filename


import mysql.connector
import os

app=Flask(__name__)
app.secret_key = os.urandom(94)
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



@app.route('/ulogin')
def ulogin():
    return render_template('ulogin.html')
@app.route('/uregister')
def uregister():
    return render_template('uregister.html')
@app.route('/services')
def services():
    return render_template('service.html')


@app.route('/uhome')
def uhome():
    return render_template('uhome.html')



@app.route('/acovid')
def acovid():
    return render_template('acovid.html')


@app.route('/dsalary')
def dsalary():
    return render_template('dsalary.html')
@app.route('/rsalary')
def rsalary():
    return render_template('rsalary.html')

@app.route('/abedrequest')
def abedrequest():
    return render_template('abedrequest.html')



@app.route('/ubed')
def ubed():
    return render_template('ubed.html')
@app.route('/uprofile')
def uprofile():
    return render_template('uprofile.html')





#..............................Superadmin panel............................................

#..................superadmin login........

@app.route('/slogout')
def slogout():
    session.pop('id')
    return redirect('/')

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


#..............................admin panel............................................

#..................admin login........


@app.route('/logout')
def logout():
    session.pop('Hospital_id')
    return redirect('/')


@app.route('/alogin')
def alogin():
    if 'Hospital_id' in session:
        return redirect('/ahome')
    else:
        return render_template('alogin.html')

@app.route('/ahome')
def ahome():
    if 'Hospital_id' in session:
        s = session['Hospital_id']
        cursor.execute("SELECT * FROM HOSPITAL WHERE Hospital_id = '" + str(s) + "'")
        p = cursor.fetchone()
        return render_template('ahome.html',p=p)
    else:
        return redirect('/')

@app.route('/login_admin', methods=['POST'])
def login_admin():
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute(
        """SELECT * FROM `hospital` WHERE `Email` LIKE '{}' AND `Password` LIKE '{}'"""
        .format(email, password))
    admin = cursor.fetchall()

    if (admin):
        if len(admin) > 0:
            session['Hospital_id'] = admin[0][0]
            return redirect('/ahome')

    return redirect('/')

#.....................................admin profile............

@app.route('/adminprofile')
def adminprofile():
    if 'Hospital_id' in session:
       s=session['Hospital_id']
       cursor.execute("SELECT * FROM HOSPITAL WHERE Hospital_id = '"+str(s)+"'")
       p = cursor.fetchone()

       return render_template('adminprofile.html', p=p)

    else:
        return redirect('/')


@app.route('/aprofile', methods=['POST', 'GET'])
def aprofile():
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

        cursor.execute("""UPDATE hospital
        SET   Email=%s ,Password=%s ,Phone=%s ,image=%s WHERE  Hospital_id=%s""",
                       (email, password, phone, filename1, id))
        flash("Data Updated Successfully")
        conn.commit()

        return redirect('/adminprofile')



#............................Add Doctor.............................



@app.route('/adoctor')
def adoctor():
    if 'Hospital_id' in session:
         s = session['Hospital_id']
         cursor.execute("SELECT* FROM `doctor` WHERE Hospital_id = '" + str(s) + "'")
         adoctor=cursor.fetchall()
         return  render_template('adoctor.html',adoctor=adoctor)
    else:
        return redirect('/')


@app.route('/view_doctor', methods=['GET', 'POST'])
def view_doctor():
        return redirect('/adoctor')

@app.route('/insertd', methods=['POST'])
def insertd():
        if request.method == "POST":
            flash("Data Inserted Successfully")
            doctorname = request.form['Doctor_name']
            address = request.form['Address']
            email = request.form['Email']
            phone = request.form['Phone']
            shift = request.form['Shift']
            status = request.form['Status']
            file1 = request.files['file1']
            filename1 = secure_filename(file1.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            hospitalid=session['Hospital_id']

            cursor.execute(
                "INSERT INTO DOCTOR (Doctor_name,Address,Email,Phone,Shift,Status,image,Hospital_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (doctorname,address,email,phone,shift,status,filename1,hospitalid))
            conn.commit()
            return redirect('/adoctor')

@app.route('/updated', methods=['GET', 'POST'])
def updated():
        if request.method == "POST":

            doctorid = request.form['Doctor_id']
            doctorname = request.form['Doctor_name']
            address = request.form['Address']
            email = request.form['Email']

            phone = request.form['Phone']

            shift = request.form['Shift']
            if shift == 'Shift':
                shift = request.form['shif']
            else:
                shift = request.form['Shift']

            status = request.form['Status']
            if status == 'Status':
                status = request.form['stat']
            else:
                status = request.form['Status']

            file1 = request.files['file1']
            filename1 = secure_filename(file1.filename)
            if filename1 == '':
                filename1 = request.form['file11']
            else:
                file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))



            cursor.execute("""UPDATE doctor 
            SET  Doctor_name=%s,Address=%s,Email=%s,Phone=%s,Shift=%s,Status=%s,image=%s WHERE Doctor_id=%s""", (doctorname,address,email,phone,shift,status,filename1,doctorid))
            flash("Data Updated Successfully")
            conn.commit()

            return redirect('/adoctor')

@app.route('/deleted/<string:doctorid>', methods=['POST', 'GET'])
def deleted(doctorid):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM doctor WHERE Doctor_id=%s", (doctorid,))
        conn.commit()
        return redirect('/adoctor')



@app.route('/searchd', methods=['GET', 'POST'])
def searchd():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        doctor = request.form['Doctor']
        cursor.execute("SELECT * FROM doctor WHERE (Doctor_name LIKE %s OR Address LIKE %s OR Shift LIKE %s OR Status LIKE %s) and Hospital_id='"+str(s)+"'", (doctor,doctor,doctor,doctor))
        adoctor = cursor.fetchall()

        if (len(adoctor) == 0 and doctor == 'all') or len(doctor)==0:
            cursor.execute("SELECT * FROM doctor WHERE Hospital_id='"+str(s)+"'")

            adoctor = cursor.fetchall()
        return render_template('adoctor.html', adoctor=adoctor)
    return redirect('/adoctor')


#............................Add Bed.............................

@app.route('/abed')
def abed():
    if 'Hospital_id' in session:
         s = session['Hospital_id']
         cursor.execute("SELECT* FROM `bed_list` WHERE Hospital_id = '" + str(s) + "'")
         abed=cursor.fetchall()
         return  render_template('abed.html',abed=abed)
    else:
        return redirect('/')



@app.route('/insertb', methods=['POST'])
def insertb():
        if request.method == "POST":
            flash("Data Inserted Successfully")

            bedcategory = request.form['Bed_category']
            cost = request.form['Cost']
            status = request.form['Status']
            hospitalid=session['Hospital_id']

            cursor.execute("INSERT INTO bed_list (Bed_category,cost,Status,Hospital_id) VALUES (%s,%s,%s,%s)",
                (bedcategory,cost,status,hospitalid))
            conn.commit()
        return redirect('/abed')

@app.route('/updateb', methods=['GET', 'POST'])
def updateb():
        if request.method == "POST":

            bedid = request.form['Bed_id']
            bedcategory = request.form['Bed_category']
            if bedcategory == 'Bed_category':
                bedcategory = request.form['Bedcat']
            else:
                bedcategory = request.form['Bed_category']
            cost = request.form['Cost']
            status = request.form['Status']
            if status == 'Status':
                status = request.form['stat']
            else:
                status = request.form['Status']

            cursor.execute("""UPDATE bed_list 
            SET  Bed_category=%s,Cost=%s,Status=%s  WHERE Bed_id=%s""", (bedcategory,cost,status,bedid))
            flash("Data Updated Successfully")
            conn.commit()

            return redirect('/abed')

@app.route('/deleteb/<string:bedid>', methods=['POST', 'GET'])
def deleteb(bedid):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM bed_list WHERE Bed_id=%s", (bedid,))
        conn.commit()
        return redirect('/abed')



@app.route('/searchb', methods=['GET', 'POST'])
def searchb():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        bed = request.form['Bed']
        cursor.execute("SELECT * FROM bed_list WHERE (Bed_category LIKE %s OR Cost LIKE %s OR Status LIKE %s) and Hospital_id='"+str(s)+"'", (bed,bed,bed))
        abed = cursor.fetchall()

        if (len(abed) == 0 and bed == 'all') or len(bed)==0:
            cursor.execute("SELECT * FROM bed_list WHERE Hospital_id='"+str(s)+"'")

            abed = cursor.fetchall()
        return render_template('abed.html', abed=abed)
    return redirect('/abed')


#.......................bed allotment.......................


@app.route('/abedallotment')
def abedallotment():
    if 'Hospital_id' in session:
         s = session['Hospital_id']
         cursor.execute("SELECT* FROM `bed_allotment` WHERE Hospital_id = '" + str(s) + "'")
         abedallotment=cursor.fetchall()
         return  render_template('abedallotment.html',abedallotment=abedallotment)
    else:
        return redirect('/')



@app.route('/insertba', methods=['POST'])
def insertba():
        if request.method == "POST":
            flash("Data Inserted Successfully")

            patientid = request.form['Patient_id']
            bedid = request.form['Bed_id']
            allotmentdate = request.form['Allotment_date']
            dischargedate=request.form['Discharge_date']
            hospitalid=session['Hospital_id']

            cursor.execute("INSERT INTO bed_allotment (Patient_id,Bed_id,Allotment_date,Discharge_date,Hospital_id) VALUES (%s,%s,%s,%s,%s)",
                (patientid,bedid,allotmentdate,dischargedate,hospitalid))
            conn.commit()
        return redirect('/abedallotment')

@app.route('/updateba', methods=['GET', 'POST'])
def updateba():
        if request.method == "POST":
            allotid=request.form['Allotment_no']
            patientid = request.form['Patient_id']
            bedid = request.form['Bed_id']
            allotmentdate = request.form['Allotment_date']
            dischargedate = request.form['Discharge_date']
            cursor.execute("""UPDATE bed_allotment 
            SET  Patient_id=%s,Bed_id=%s,Allotment_date=%s,Discharge_date=%s  WHERE Allotment_no=%s""", (patientid,bedid,allotmentdate,dischargedate,allotid))
            flash("Data Updated Successfully")
            conn.commit()

            return redirect('/abedallotment')

@app.route('/deleteba/<string:allotid>', methods=['POST', 'GET'])
def deleteba(allotid):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM bed_allotment WHERE Allotment_no=%s", (allotid,))
        conn.commit()
        return redirect('/abedallotment')



@app.route('/searchba', methods=['GET', 'POST'])
def searchba():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        allot = request.form['allot']
        cursor.execute("SELECT * FROM bed_allotment WHERE (Patient_id LIKE %s OR Bed_id LIKE %s OR Allotment_date LIKE %s OR Discharge_date LIKE %s) and Hospital_id='"+str(s)+"'", (allot,allot,allot,allot))
        abedallotment = cursor.fetchall()

        if (len(abedallotment) == 0 and allot == 'all') or len(allot)==0:
            cursor.execute("SELECT * FROM bed_allotment WHERE Hospital_id='"+str(s)+"'")

            abedallotment = cursor.fetchall()
        return render_template('abedallotment.html',abedallotment=abedallotment)
    return redirect('/abedallotment')




#............................Add Patients.............................



@app.route('/apatient')
def apatient():
    if 'Hospital_id' in session:
         s = session['Hospital_id']
         cursor.execute("SELECT* FROM `patient` WHERE Hospital_id = '" + str(s) + "'")
         apatient=cursor.fetchall()
         return  render_template('apatient.html',apatient=apatient)
    else:
        return redirect('/')


@app.route('/insertp', methods=['POST'])
def insertp():
        if request.method == "POST":
            flash("Data Inserted Successfully")
            hospitalid=session['Hospital_id']
            patientname = request.form['Patient_name']
            phone = request.form['Phone']
            relativename=request.form['Relative_name']
            rphone = request.form['Relative_Phone']
            address = request.form['Address']
            pailments=request.form['ailment']
            date=request.form['date']
            bedno = request.form['Bed_id']
            condition = request.form['Condition']
            dname = request.form['Doctor_name']

            cursor.execute(
                "INSERT INTO PATIENT (Patient_name,Phone,Relative_name,Relative_Phone,Address,Ailment,Date,Bed_id,Pcondition,Doctor_name,Hospital_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (patientname,phone,relativename,rphone,address,pailments,date,bedno,condition,dname,hospitalid))
            conn.commit()
            return redirect('/apatient')

@app.route('/updatep', methods=['GET', 'POST'])
def updatep():
        if request.method == "POST":
            patientid=request.form['Patient_id']
            patientname = request.form['Patient_name']
            phone = request.form['Phone']
            relativename = request.form['Relative_name']
            rphone = request.form['Relative_Phone']
            address = request.form['Address']
            pailments = request.form['ailment']
            date = request.form['date']
            bedno = request.form['Bed_id']
            condition = request.form['Condition']
            if condition == 'Condition':
                condition = request.form['con']
            else:
                condition = request.form['Condition']
            dname = request.form['Doctor_name']

            cursor.execute("""UPDATE patient 
            SET  Patient_name=%s,Phone=%s,Relative_name=%s,Relative_Phone=%s,Address=%s,Ailment=%s,Date=%s,Bed_id=%s,Pcondition=%s,Doctor_name=%s WHERE Patient_id=%s""", (patientname,phone,relativename,rphone,address,pailments,date,bedno,condition,dname,patientid))
            flash("Data Updated Successfully")
            conn.commit()

            return redirect('/apatient')

@app.route('/deletep/<string:patientid>', methods=['POST', 'GET'])
def deletep(patientid):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM patient WHERE Patient_id=%s", (patientid,))
        conn.commit()
        return redirect('/apatient')



@app.route('/searchp', methods=['GET', 'POST'])
def searchp():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        patient = request.form['Patient']
        cursor.execute("SELECT * FROM patient WHERE (Patient_name LIKE %s OR Bed_id LIKE %s OR Pcondition LIKE %s) and Hospital_id='"+str(s)+"'", (patient,patient,patient))
        apatient = cursor.fetchall()

        if (len(apatient) == 0 and patient == 'all') or len(patient)==0:
            cursor.execute("SELECT * FROM patient WHERE Hospital_id='"+str(s)+"'")

            apatient = cursor.fetchall()
        return render_template('apatient.html', apatient=apatient)
    return redirect('/apatient')



#............................Add Patients Payment.............................



@app.route('/apayment')
def apayment():
    if 'Hospital_id' in session:
         s = session['Hospital_id']
         cursor.execute("SELECT* FROM `patient_payment` WHERE Hospital_id = '" + str(s) + "'")
         apayment=cursor.fetchall()
         return  render_template('apayment.html',apayment=apayment)
    else:
        return redirect('/')


@app.route('/insertpp', methods=['POST'])
def insertpp():
        if request.method == "POST":
            flash("Data Inserted Successfully")
            hospitalid=session['Hospital_id']
            patientid = request.form['Patient_id']
            patientname = request.form['Patient_name']
            totalamount = request.form['Total_amount']
            deposit=request.form['Deposit']
            dueamount = request.form['Due_amount']

            cursor.execute(
                "INSERT INTO PATIENT_PAYMENT (Patient_id,Patient_name,Total_amount,Deposit,Due_amount,Hospital_id) VALUES (%s,%s,%s,%s,%s,%s)",
                (patientid,patientname,totalamount,deposit,dueamount,hospitalid))
            conn.commit()
            return redirect('/apayment')

@app.route('/updatepp', methods=['GET', 'POST'])
def updatepp():
        if request.method == "POST":

            paymentno = request.form['Payment_no']
            patientid=request.form['Patient_id']
            patientname = request.form['Patient_name']
            totalamount = request.form['Total_amount']
            deposit = request.form['Deposit']
            dueamount = request.form['Due_amount']

            cursor.execute("""UPDATE patient_payment 
            SET  Patient_id=%s,Patient_name=%s,Total_amount=%s,Deposit=%s,Due_amount=%s  WHERE Payment_no=%s""", (patientid,patientname,totalamount,deposit,dueamount,paymentno))
            flash("Data Updated Successfully")
            conn.commit()

            return redirect('/apayment')

@app.route('/deletepp/<string:paymentid>', methods=['POST', 'GET'])
def deletepp(paymentid):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM patient_payment WHERE Payment_no=%s", (paymentid,))
        conn.commit()
        return redirect('/apayment')



@app.route('/searchpp', methods=['GET', 'POST'])
def searchpp():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        payment = request.form['Payment']
        cursor.execute("SELECT * FROM patient_payment WHERE (Patient_id LIKE %s OR Patient_name LIKE %s) and Hospital_id='"+str(s)+"'", (payment,payment))
        apayment = cursor.fetchall()

        if (len(apayment) == 0 and payment == 'all') or len(payment)==0:
            cursor.execute("SELECT * FROM patient_payment WHERE Hospital_id='"+str(s)+"'")

            apayment = cursor.fetchall()
        return render_template('apayment.html',apayment=apayment)
    return redirect('/apayment')


#.........................Add Receptionist.................................

@app.route('/areceptionist')
def areceptionist():
    if 'Hospital_id' in session:
         s = session['Hospital_id']
         cursor.execute("SELECT* FROM `receptionist` WHERE Hospital_id = '" + str(s) + "'")
         areceptionist=cursor.fetchall()
         return  render_template('areceptionist.html',areceptionist=areceptionist)
    else:
        return redirect('/')


@app.route('/view_receptionist', methods=['GET', 'POST'])
def view_receptionist():
        return redirect('/areceptionist')

@app.route('/insertre', methods=['POST'])
def insertre():
        if request.method == "POST":
            flash("Data Inserted Successfully")
            receptionistname = request.form['Receptionist_name']
            address = request.form['Address']
            email = request.form['Email']
            password=request.form['Password']
            phone = request.form['Phone']
            shift = request.form['Shift']
            status = request.form['Status']
            file1 = request.files['file1']
            filename1 = secure_filename(file1.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))

            hospitalid=session['Hospital_id']

            cursor.execute(
                "INSERT INTO RECEPTIONIST (Receptionist_name,Address,Email,Password,Phone,Shift,Status,image,Hospital_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (receptionistname,address,email,password,phone,shift,status,filename1,hospitalid))
            conn.commit()
            return redirect('/areceptionist')

@app.route('/updatere', methods=['GET', 'POST'])
def updatedre():
        if request.method == "POST":

            receptionistid = request.form['Receptionist_id']
            receptionistname = request.form['Receptionist_name']
            address = request.form['Address']
            email = request.form['Email']
            password = request.form['Password']
            phone = request.form['Phone']

            shift = request.form['Shift']
            if shift == 'Shift':
                shift = request.form['shif']
            else:
                shift = request.form['Shift']

            status = request.form['Status']
            if status == 'Status':
                status = request.form['stat']
            else:
                status = request.form['Status']

            file1 = request.files['file1']
            filename1 = secure_filename(file1.filename)
            if filename1 == '':
                filename1 = request.form['file11']
            else:
                file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            cursor.execute("""UPDATE receptionist 
            SET  Receptionist_name=%s,Address=%s,Email=%s,Password=%s,Phone=%s,Shift=%s,Status=%s,image=%s WHERE Receptionist_id=%s""", (receptionistname,address,email,password,phone,shift,status,filename1,receptionistid))
            flash("Data Updated Successfully")
            conn.commit()

            return redirect('/areceptionist')

@app.route('/deletere/<string:receptionistid>', methods=['POST', 'GET'])
def deletere(receptionistid):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM receptionist WHERE Receptionist_id=%s", (receptionistid,))
        conn.commit()
        return redirect('/areceptionist')



@app.route('/searchre', methods=['GET', 'POST'])
def searchre():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        receptionist = request.form['Receptionist']
        cursor.execute("SELECT * FROM receptionist WHERE (Receptionist_name LIKE %s OR Address LIKE %s OR Shift LIKE %s OR Status LIKE %s) and Hospital_id='"+str(s)+"'", (receptionist,receptionist,receptionist,receptionist))
        areceptionist = cursor.fetchall()

        if (len(areceptionist) == 0 and receptionist == 'all') or len(receptionist)==0:
            cursor.execute("SELECT * FROM receptionist WHERE Hospital_id='"+str(s)+"'")

            areceptionist = cursor.fetchall()
        return render_template('areceptionist.html', areceptionist=areceptionist)
    return redirect('/areceptionist')



#...................Add Doze 1........................


@app.route('/adoze1')
def adoze1():
    if 'Hospital_id' in session:
        s = session['Hospital_id']
        cursor.execute("SELECT* FROM `doze1` WHERE Hospital_id = '" + str(s) + "'")
        adoze1=cursor.fetchall()
        return  render_template('adoze1.html',adoze1=adoze1)
    else:
        return redirect('/')


@app.route('/insertdoze1', methods=['POST'])
def insertdoze1():
        if request.method == "POST":
            flash("Data Inserted Successfully")
            name = request.form['Name']
            address = request.form['Address']
            nid = request.form['nid']
            phone = request.form['Phone']
            agegroup = request.form['Age_group']
            allergies = request.form['Allergies']
            ailments = request.form['Ailments']
            doze = request.form['Doze']
            appointment=request.form['Date']
            hospitalid=session['Hospital_id']

            cursor.execute(
                "INSERT INTO DOZE1 (Name,Address,NID,Phone_number,Age_group,Allergies,Prior_ailments,Doze_name,Appointment_date,Hospital_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (name,address,nid,phone,agegroup,allergies,ailments,doze,appointment,hospitalid))
            conn.commit()
            return redirect('/adoze1')

@app.route('/updatedoze1', methods=['GET', 'POST'])
def updatedoze1():
        if request.method == "POST":

            id = request.form['id']
            name = request.form['Name']
            address = request.form['Address']
            nid = request.form['nid']
            phone = request.form['Phone']
            agegroup = request.form['Age_group']
            if agegroup == 'Age Group':
                agegroup = request.form['age_group']
            else:
                agegroup = request.form['Age_group']

            allergies = request.form['Allergies']
            if allergies == 'Allergies':
                allergies = request.form['allergies']
            else:
                allergies = request.form['Allergies']

            ailments = request.form['Ailments']
            if ailments == 'Prior Ailments':
                ailments = request.form['ailments']
            else:
                ailments = request.form['Ailments']

            doze = request.form['Doze']
            if doze == 'Doze Name':
                doze = request.form['doze']
            else:
                doze = request.form['Doze']

            appointment = request.form['Date']

            doze1 = request.form['Doze1']
            if doze1 == 'Doze1':
                doze1 = request.form['doze1']
            else:
                doze1 = request.form['Doze1']
            hospitalid = session['Hospital_id']

            id1 = request.form.get('id')
            cursor.execute(
                """SELECT * FROM `doze2` WHERE `id` LIKE '{}'"""
                    .format(id1))
            duau = cursor.fetchall()

            if (duau):
                cursor.execute("""UPDATE doze1
                            SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment_date=%s,Doze1=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1, id))

                conn.commit()

                cursor.execute("""UPDATE doze2
                                            SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment1=%s,Doze1=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1, id))
                flash("Data Updated Successfully")
                conn.commit()

            else:
                cursor.execute("""UPDATE doze1
                                            SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment_date=%s,Doze1=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1, id))
                flash("Data Updated and Added to Doze2 Successfully")
                conn.commit()

                cursor.execute(
                    "INSERT INTO DOZE2 (id,Name,Address,NID,Phone_number,Age_group,Allergies,Prior_ailments,Doze_name,Appointment1,Doze1,Hospital_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (id,name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1, hospitalid))
                conn.commit()




            return redirect('/adoze1')



@app.route('/deletedoze1/<string:doze1id>', methods=['POST', 'GET'])
def deletedoze1(doze1id):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM doze1 WHERE ID=%s", (doze1id,))
        conn.commit()
        return redirect('/adoze1')



@app.route('/searchdoze1', methods=['GET', 'POST'])
def searchdoze1():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        doze1 = request.form['doze1']
        cursor.execute("SELECT * FROM doze1 WHERE (Name LIKE %s  OR Address LIKE %s OR NID LIKE %s OR Doze_name LIKE %s OR Prior_ailments LIKE %s OR Allergies LIKE %s OR Appointment_date LIKE %s OR Doze1 LIKE %s) and Hospital_id='" + str(s) + "'", (doze1,doze1,doze1,doze1,doze1,doze1,doze1,doze1))
        adoze1= cursor.fetchall()

        if (len(adoze1) == 0 and doze1 == 'all') or len(doze1)==0:
            cursor.execute("SELECT * FROM doze1 WHERE Hospital_id='" + str(s) + "'")

            adoze1 = cursor.fetchall()
        return render_template('adoze1.html', adoze1=adoze1)
    return redirect('/adoze1')




#...................Add Doze 2........................


@app.route('/adoze2')
def adoze2():
    if 'Hospital_id' in session:
        s = session['Hospital_id']
        cursor.execute("SELECT* FROM `doze2` WHERE Hospital_id = '" + str(s) + "'")
        adoze2=cursor.fetchall()
        return  render_template('adoze2.html',adoze2=adoze2)
    else:
        return redirect('/')


@app.route('/updatedoze2', methods=['GET', 'POST'])
def updatedoze2():
        if request.method == "POST":

            id = request.form['id']
            name = request.form['Name']
            address = request.form['Address']
            nid = request.form['nid']
            phone = request.form['Phone']
            agegroup = request.form['Age_group']
            if agegroup == 'Age Group':
                agegroup = request.form['age_group']
            else:
                agegroup = request.form['Age_group']

            allergies = request.form['Allergies']
            if allergies == 'Allergies':
                allergies = request.form['allergies']
            else:
                allergies = request.form['Allergies']

            ailments = request.form['Ailments']
            if ailments == 'Prior Ailments':
                ailments = request.form['ailments']
            else:
                ailments = request.form['Ailments']

            doze = request.form['Doze']
            if doze == 'Doze Name':
                doze = request.form['doze']
            else:
                doze = request.form['Doze']

            appointment = request.form['Date']

            doze1 = request.form['Doze1']
            if doze1 == 'Doze1':
                doze1 = request.form['doze1']
            else:
                doze1 = request.form['Doze1']

            appointment2 = request.form['Date2']

            doze2 = request.form['Doze2']
            if doze2 == 'Doze2':
                doze2 = request.form['doze2']
            else:
                doze2 = request.form['Doze2']
            hospitalid = session['Hospital_id']
            var = 'Vaccinated'
            id1 = request.form.get('id')
            cursor.execute(
                """SELECT * FROM `vaccinated` WHERE `id` LIKE '{}'"""
                    .format(id1))
            d2uau = cursor.fetchall()

            if (d2uau):
                cursor.execute("""UPDATE doze2
                            SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment1=%s,Doze1=%s,Appointment2=%s,Doze2=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1,appointment2, doze2, id))

                conn.commit()

                cursor.execute("""UPDATE vaccinated
                                            SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment1=%s,Doze1=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1, id))
                flash("Data Updated Successfully")
                conn.commit()

            else:
                cursor.execute("""UPDATE doze2
                                            SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment1=%s,Doze1=%s,Appointment2=%s,Doze2=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1,appointment2, doze2, id))

                flash("Data Updated and Added to Vaccinated Successfully")
                conn.commit()

                cursor.execute(
                    "INSERT INTO VACCINATED (id,Name,Address,NID,Phone_number,Age_group,Allergies,Prior_ailments,Doze_name,Appointment1,Doze1,Appointment2,Doze2,Vaccinated,Hospital_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (id,name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1,appointment2, doze2,var, hospitalid))
                conn.commit()




            return redirect('/adoze2')




@app.route('/deletedoze2/<string:doze2id>', methods=['POST', 'GET'])
def deletedoze2(doze2id):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM doze2 WHERE ID=%s", (doze2id,))
        conn.commit()
        return redirect('/adoze2')



@app.route('/searchdoze2', methods=['GET', 'POST'])
def searchdoze2():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        doze2 = request.form['doze2']
        cursor.execute("SELECT * FROM doze2 WHERE (Name LIKE %s  OR Address LIKE %s OR NID LIKE %s OR Doze_name LIKE %s OR Prior_ailments LIKE %s OR Allergies LIKE %s OR Appointment1 LIKE %s OR Doze1 LIKE %s OR Doze2 LIKE %s OR Appointment2 LIKE %s) and Hospital_id='" + str(s) + "'", (doze2,doze2,doze2,doze2,doze2,doze2,doze2,doze2,doze2,doze2))
        adoze2= cursor.fetchall()

        if (len(adoze2) == 0 and doze2 == 'all') or len(doze2)==0:
            cursor.execute("SELECT * FROM doze2 WHERE Hospital_id='" + str(s) + "'")

            adoze2 = cursor.fetchall()
        return render_template('adoze2.html', adoze2=adoze2)
    return redirect('/adoze2')



#...................Vaccinated........................


@app.route('/vaccinated')
def vaccinated():
    if 'Hospital_id' in session:
        s = session['Hospital_id']
        cursor.execute("SELECT* FROM `vaccinated` WHERE Hospital_id = '" + str(s) + "'")
        vaccinated=cursor.fetchall()
        return  render_template('vaccinated.html',vaccinated=vaccinated)
    else:
        return redirect('/')





@app.route('/deletev/<string:vid>', methods=['POST', 'GET'])
def deletev(vid):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM vaccinated WHERE ID=%s", (vid,))
        conn.commit()
        return redirect('/vaccinated')



@app.route('/searchv', methods=['GET', 'POST'])
def searchv():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        vax = request.form['vax']
        cursor.execute("SELECT * FROM vaccinated WHERE (Name LIKE %s  OR Address LIKE %s OR NID LIKE %s OR Doze_name LIKE %s OR Prior_ailments LIKE %s OR Allergies LIKE %s OR Appointment1 LIKE %s OR Doze1 LIKE %s OR Doze2 LIKE %s OR Appointment2 LIKE %s) and Hospital_id='" + str(s) + "'", (vax,vax,vax,vax,vax,vax,vax,vax,vax,vax))
        vaccinated= cursor.fetchall()

        if (len(vaccinated) == 0 and vax == 'all') or len(vax)==0:
            cursor.execute("SELECT * FROM vaccinated WHERE Hospital_id='" + str(s) + "'")

            vaccinated = cursor.fetchall()
        return render_template('vaccinated.html', vaccinated=vaccinated)
    return redirect('/vaccinated')




#..............................Receptionist panel............................................

#..................Receptionist login........


@app.route('/rlogout')
def rlogout():
    session.pop('Receptionist_id')
    return redirect('/')


@app.route('/rlogin')
def rlogin():
    if 'Receptionist_id' in session:
        return redirect('/rhome')
    else:
        return render_template('rlogin.html')

@app.route('/rhome')
def rhome():
    if 'Receptionist_id' in session:
        s = session['Hospital_id']
        cursor.execute("SELECT * FROM HOSPITAL WHERE Hospital_id = '" + str(s) + "'")
        p = cursor.fetchone()
        return render_template('rhome.html',p=p)
    else:
        return redirect('/')

@app.route('/login_rec', methods=['POST'])
def login_rec():
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute(
        """SELECT * FROM `receptionist` WHERE `Email` LIKE '{}' AND `Password` LIKE '{}'"""
        .format(email, password))
    rec = cursor.fetchall()

    if (rec):
        if len(rec) > 0:
            session['Hospital_id'] = rec[0][9]
            session['Receptionist_id']=rec[0][0]
            return redirect('/rhome')

    return redirect('/')

#.....................................Receptionist profile............

@app.route('/rprofile')
def rprofile():
    if 'Receptionist_id' in session:
       s=session['Receptionist_id']
       cursor.execute("SELECT * FROM RECEPTIONIST WHERE Receptionist_id = '"+str(s)+"'")
       p = cursor.fetchone()

       return render_template('rprofile.html', p=p)

    else:
        return redirect('/')


@app.route('/recprofile', methods=['POST', 'GET'])
def recprofile():
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

        cursor.execute("""UPDATE receptionist
        SET   Email=%s ,Password=%s ,Phone=%s ,image=%s WHERE  Receptionist_id=%s""",
                       (email, password, phone, filename1, id))
        flash("Data Updated Successfully")
        conn.commit()

        return redirect('/rprofile')


#.....................Receptionist Doctor...................

@app.route('/rdoctor')
def rdoctor():
    if 'Receptionist_id' in session:
         s = session['Hospital_id']
         cursor.execute("SELECT* FROM `doctor` WHERE Hospital_id = '" + str(s) + "'")
         rdoctor=cursor.fetchall()
         return  render_template('rdoctor.html',rdoctor=rdoctor)
    else:
        return redirect('/')

@app.route('/updaterecd', methods=['GET', 'POST'])
def updaterecd():
        if request.method == "POST":

            doctorid = request.form['Doctor_id']

            shift = request.form['Shift']
            if shift == 'Shift':
                shift = request.form['shif']
            else:
                shift = request.form['Shift']

            status = request.form['Status']
            if status == 'Status':
                status = request.form['stat']
            else:
                status = request.form['Status']


            cursor.execute("""UPDATE doctor 
            SET  Shift=%s,Status=%s WHERE Doctor_id=%s""", (shift,status,doctorid))
            flash("Data Updated Successfully")
            conn.commit()

            return redirect('/rdoctor')


@app.route('/searchrecd', methods=['GET', 'POST'])
def searchrecd():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        doctor = request.form['Doctor']
        cursor.execute("SELECT * FROM doctor WHERE (Doctor_name LIKE %s OR Address LIKE %s OR Shift LIKE %s OR Status LIKE %s) and Hospital_id='"+str(s)+"'", (doctor,doctor,doctor,doctor))
        rdoctor = cursor.fetchall()

        if (len(rdoctor) == 0 and doctor == 'all') or len(doctor)==0:
            cursor.execute("SELECT * FROM doctor WHERE Hospital_id='"+str(s)+"'")

            rdoctor = cursor.fetchall()
        return render_template('rdoctor.html', rdoctor=rdoctor)
    return redirect('/rdoctor')


#...................Receptionist Bed.....................

@app.route('/rbed')
def rbed():
    if 'Receptionist_id' in session:
         s = session['Hospital_id']
         cursor.execute("SELECT* FROM `bed_list` WHERE Hospital_id = '" + str(s) + "'")
         rbed=cursor.fetchall()
         return  render_template('rbed.html',rbed=rbed)
    else:
        return redirect('/')


@app.route('/updaterecb', methods=['GET', 'POST'])
def updaterecb():
        if request.method == "POST":

            bedid = request.form['Bed_id']

            status = request.form['Status']
            if status == 'Status':
                status = request.form['stat']
            else:
                status = request.form['Status']

            cursor.execute("""UPDATE bed_list 
            SET  Status=%s  WHERE Bed_id=%s""", (status,bedid))
            flash("Data Updated Successfully")
            conn.commit()
            return redirect('/rbed')


@app.route('/searchrecb', methods=['GET', 'POST'])
def searchrecb():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        bed = request.form['Bed']
        cursor.execute("SELECT * FROM bed_list WHERE (Bed_category LIKE %s OR Cost LIKE %s OR Status LIKE %s) and Hospital_id='"+str(s)+"'", (bed,bed,bed))
        rbed = cursor.fetchall()

        if (len(rbed) == 0 and bed == 'all') or len(bed)==0:
            cursor.execute("SELECT * FROM bed_list WHERE Hospital_id='"+str(s)+"'")

            rbed = cursor.fetchall()
        return render_template('rbed.html', rbed=rbed)
    return redirect('/rbed')


#.......................Receptionist Bed Allotment.......................

@app.route('/rbedallotment')
def rbedallotment():
    if 'Receptionist_id' in session:
         s = session['Hospital_id']
         cursor.execute("SELECT* FROM `bed_allotment` WHERE Hospital_id = '" + str(s) + "'")
         rbedallotment=cursor.fetchall()
         return  render_template('rbedallotment.html',rbedallotment=rbedallotment)
    else:
        return redirect('/')



@app.route('/insertrecba', methods=['POST'])
def insertrecba():
        if request.method == "POST":
            flash("Data Inserted Successfully")

            patientid = request.form['Patient_id']
            bedid = request.form['Bed_id']
            allotmentdate = request.form['Allotment_date']
            dischargedate=request.form['Discharge_date']
            hospitalid=session['Hospital_id']

            cursor.execute("INSERT INTO bed_allotment (Patient_id,Bed_id,Allotment_date,Discharge_date,Hospital_id) VALUES (%s,%s,%s,%s,%s)",
                (patientid,bedid,allotmentdate,dischargedate,hospitalid))
            conn.commit()
        return redirect('/rbedallotment')

@app.route('/updaterecba', methods=['GET', 'POST'])
def updaterecba():
        if request.method == "POST":
            allotid=request.form['Allotment_no']
            patientid = request.form['Patient_id']
            bedid = request.form['Bed_id']
            allotmentdate = request.form['Allotment_date']
            dischargedate = request.form['Discharge_date']
            cursor.execute("""UPDATE bed_allotment 
            SET  Patient_id=%s,Bed_id=%s,Allotment_date=%s,Discharge_date=%s  WHERE Allotment_no=%s""", (patientid,bedid,allotmentdate,dischargedate,allotid))
            flash("Data Updated Successfully")
            conn.commit()

            return redirect('/rbedallotment')

@app.route('/deleterecba/<string:rallotid>', methods=['POST', 'GET'])
def deleterecba(rallotid):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM bed_allotment WHERE Allotment_no=%s", (rallotid,))
        conn.commit()
        return redirect('/rbedallotment')



@app.route('/searchrecba', methods=['GET', 'POST'])
def searchrecba():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        allot = request.form['allot']
        cursor.execute("SELECT * FROM bed_allotment WHERE (Patient_id LIKE %s OR Bed_id LIKE %s OR Allotment_date LIKE %s OR Discharge_date LIKE %s) and Hospital_id='"+str(s)+"'", (allot,allot,allot,allot))
        rbedallotment = cursor.fetchall()

        if (len(rbedallotment) == 0 and allot == 'all') or len(allot)==0:
            cursor.execute("SELECT * FROM bed_allotment WHERE Hospital_id='"+str(s)+"'")

            rbedallotment = cursor.fetchall()
        return render_template('rbedallotment.html',rbedallotment=rbedallotment)
    return redirect('/rbedallotment')


#.....................Receptionist Add Patient...............
@app.route('/rpatient')
def rpatient():
    if 'Receptionist_id' in session:
         s = session['Hospital_id']
         cursor.execute("SELECT* FROM `patient` WHERE Hospital_id = '" + str(s) + "'")
         rpatient=cursor.fetchall()
         return  render_template('rpatient.html',rpatient=rpatient)
    else:
        return redirect('/')


@app.route('/insertrecp', methods=['POST'])
def insertrecp():
        if request.method == "POST":
            flash("Data Inserted Successfully")
            hospitalid=session['Hospital_id']
            patientname = request.form['Patient_name']
            phone = request.form['Phone']
            relativename=request.form['Relative_name']
            rphone = request.form['Relative_Phone']
            address = request.form['Address']
            pailments=request.form['ailment']
            date=request.form['date']
            bedno = request.form['Bed_id']
            condition = request.form['Condition']
            dname = request.form['Doctor_name']

            cursor.execute(
                "INSERT INTO PATIENT (Patient_name,Phone,Relative_name,Relative_Phone,Address,Ailment,Date,Bed_id,Pcondition,Doctor_name,Hospital_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (patientname,phone,relativename,rphone,address,pailments,date,bedno,condition,dname,hospitalid))
            conn.commit()
            return redirect('/rpatient')

@app.route('/updaterecp', methods=['GET', 'POST'])
def updaterecp():
        if request.method == "POST":
            patientid=request.form['Patient_id']
            patientname = request.form['Patient_name']
            phone = request.form['Phone']
            relativename = request.form['Relative_name']
            rphone = request.form['Relative_Phone']
            address = request.form['Address']
            pailments = request.form['ailment']
            date = request.form['date']
            bedno = request.form['Bed_id']
            condition = request.form['Condition']
            if condition == 'Condition':
                condition = request.form['con']
            else:
                condition = request.form['Condition']
            dname = request.form['Doctor_name']

            cursor.execute("""UPDATE patient 
            SET  Patient_name=%s,Phone=%s,Relative_name=%s,Relative_Phone=%s,Address=%s,Ailment=%s,Date=%s,Bed_id=%s,Pcondition=%s,Doctor_name=%s WHERE Patient_id=%s""", (patientname,phone,relativename,rphone,address,pailments,date,bedno,condition,dname,patientid))
            flash("Data Updated Successfully")
            conn.commit()

            return redirect('/rpatient')

@app.route('/deleterecp/<string:rpatientid>', methods=['POST', 'GET'])
def deleterecp(rpatientid):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM patient WHERE Patient_id=%s", (rpatientid,))
        conn.commit()
        return redirect('/rpatient')



@app.route('/searchrecp', methods=['GET', 'POST'])
def searchrecp():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        patient = request.form['Patient']
        cursor.execute("SELECT * FROM patient WHERE (Patient_name LIKE %s OR Bed_id LIKE %s OR Pcondition LIKE %s) and Hospital_id='"+str(s)+"'", (patient,patient,patient))
        rpatient = cursor.fetchall()

        if (len(rpatient) == 0 and patient == 'all') or len(patient)==0:
            cursor.execute("SELECT * FROM patient WHERE Hospital_id='"+str(s)+"'")

            rpatient = cursor.fetchall()
        return render_template('rpatient.html', rpatient=rpatient)
    return redirect('/rpatient')



#............................Receptionist Add Patients Payment.............................



@app.route('/rpayment')
def rpayment():
    if 'Receptionist_id' in session:
         s = session['Hospital_id']
         cursor.execute("SELECT* FROM `patient_payment` WHERE Hospital_id = '" + str(s) + "'")
         rpayment=cursor.fetchall()
         return  render_template('rpayment.html',rpayment=rpayment)
    else:
        return redirect('/')


@app.route('/insertrecpp', methods=['POST'])
def insertrecpp():
        if request.method == "POST":
            flash("Data Inserted Successfully")
            hospitalid=session['Hospital_id']
            patientid = request.form['Patient_id']
            patientname = request.form['Patient_name']
            totalamount = request.form['Total_amount']
            deposit=request.form['Deposit']
            dueamount = request.form['Due_amount']

            cursor.execute(
                "INSERT INTO PATIENT_PAYMENT (Patient_id,Patient_name,Total_amount,Deposit,Due_amount,Hospital_id) VALUES (%s,%s,%s,%s,%s,%s)",
                (patientid,patientname,totalamount,deposit,dueamount,hospitalid))
            conn.commit()
            return redirect('/rpayment')

@app.route('/updaterecpp', methods=['GET', 'POST'])
def updaterecpp():
        if request.method == "POST":

            paymentno = request.form['Payment_no']
            patientid=request.form['Patient_id']
            patientname = request.form['Patient_name']
            totalamount = request.form['Total_amount']
            deposit = request.form['Deposit']
            dueamount = request.form['Due_amount']

            cursor.execute("""UPDATE patient_payment 
            SET  Patient_id=%s,Patient_name=%s,Total_amount=%s,Deposit=%s,Due_amount=%s  WHERE Payment_no=%s""", (patientid,patientname,totalamount,deposit,dueamount,paymentno))
            flash("Data Updated Successfully")
            conn.commit()

            return redirect('/rpayment')

@app.route('/deleterecpp/<string:rpaymentid>', methods=['POST', 'GET'])
def deleterecpp(rpaymentid):
        flash("Record has been deleted successfully")

        cursor.execute("DELETE FROM patient_payment WHERE Payment_no=%s", (rpaymentid,))
        conn.commit()
        return redirect('/rpayment')



@app.route('/searchrecpp', methods=['GET', 'POST'])
def searchrecpp():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        payment = request.form['Payment']
        cursor.execute("SELECT * FROM patient_payment WHERE (Patient_id LIKE %s OR Patient_name LIKE %s) and Hospital_id='"+str(s)+"'", (payment,payment))
        rpayment = cursor.fetchall()

        if (len(rpayment) == 0 and payment == 'all') or len(payment)==0:
            cursor.execute("SELECT * FROM patient_payment WHERE Hospital_id='"+str(s)+"'")

            rpayment = cursor.fetchall()
        return render_template('rpayment.html',rpayment=rpayment)
    return redirect('/rpayment')


#...................Receptionist Add Doze 1........................


@app.route('/rdoze1')
def rdoze1():
    if 'Receptionist_id' in session:
        s = session['Hospital_id']
        cursor.execute("SELECT* FROM `doze1` WHERE Hospital_id = '" + str(s) + "'")
        rdoze1=cursor.fetchall()
        return  render_template('rdoze1.html',rdoze1=rdoze1)
    else:
        return redirect('/')




@app.route('/updaterecdoze1', methods=['GET', 'POST'])
def updaterecdoze1():
        if request.method == "POST":

            id = request.form['id']
            name = request.form['Name']
            address = request.form['Address']
            nid = request.form['nid']
            phone = request.form['Phone']
            agegroup = request.form['Age_group']
            if agegroup == 'Age Group':
                agegroup = request.form['age_group']
            else:
                agegroup = request.form['Age_group']

            allergies = request.form['Allergies']
            if allergies == 'Allergies':
                allergies = request.form['allergies']
            else:
                allergies = request.form['Allergies']

            ailments = request.form['Ailments']
            if ailments == 'Prior Ailments':
                ailments = request.form['ailments']
            else:
                ailments = request.form['Ailments']

            doze = request.form['Doze']
            if doze == 'Doze Name':
                doze = request.form['doze']
            else:
                doze = request.form['Doze']

            appointment = request.form['Date']

            doze1 = request.form['Doze1']
            if doze1 == 'Doze1':
                doze1 = request.form['doze1']
            else:
                doze1 = request.form['Doze1']
            hospitalid = session['Hospital_id']

            id1 = request.form.get('id')
            cursor.execute(
                """SELECT * FROM `doze2` WHERE `id` LIKE '{}'"""
                    .format(id1))
            duau = cursor.fetchall()

            if (duau):
                cursor.execute("""UPDATE doze1
                                        SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment_date=%s,Doze1=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1, id))

                conn.commit()

                cursor.execute("""UPDATE doze2
                                                        SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment1=%s,Doze1=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1, id))
                flash("Data Updated Successfully")
                conn.commit()

            else:
                cursor.execute("""UPDATE doze1
                                                        SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment_date=%s,Doze1=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1, id))
                flash("Data Updated and Added to Doze2 Successfully")
                conn.commit()

                cursor.execute(
                    "INSERT INTO DOZE2 (id,Name,Address,NID,Phone_number,Age_group,Allergies,Prior_ailments,Doze_name,Appointment1,Doze1,Hospital_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                    id, name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1, hospitalid))
                conn.commit()

        return redirect('/rdoze1')




@app.route('/searchrecdoze1', methods=['GET', 'POST'])
def searchrecdoze1():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        doze1 = request.form['doze1']
        cursor.execute("SELECT * FROM doze1 WHERE (Name LIKE %s  OR Address LIKE %s OR NID LIKE %s OR Doze_name LIKE %s OR Prior_ailments LIKE %s OR Allergies LIKE %s OR Appointment_date LIKE %s OR Doze1 LIKE %s) and Hospital_id='" + str(s) + "'", (doze1,doze1,doze1,doze1,doze1,doze1,doze1,doze1))
        rdoze1= cursor.fetchall()

        if (len(rdoze1) == 0 and doze1 == 'all') or len(doze1)==0:
            cursor.execute("SELECT * FROM doze1 WHERE Hospital_id='" + str(s) + "'")

            rdoze1 = cursor.fetchall()
        return render_template('rdoze1.html', rdoze1=rdoze1)
    return redirect('/rdoze1')




#...................Receptionist Add Doze 2........................


@app.route('/rdoze2')
def rdoze2():
    if 'Hospital_id' in session:
        s = session['Hospital_id']
        cursor.execute("SELECT* FROM `doze2` WHERE Hospital_id = '" + str(s) + "'")
        rdoze2=cursor.fetchall()
        return  render_template('rdoze2.html',rdoze2=rdoze2)
    else:
        return redirect('/')


@app.route('/updaterecdoze2', methods=['GET', 'POST'])
def updaterecdoze2():
        if request.method == "POST":

            id = request.form['id']
            name = request.form['Name']
            address = request.form['Address']
            nid = request.form['nid']
            phone = request.form['Phone']
            agegroup = request.form['Age_group']
            if agegroup == 'Age Group':
                agegroup = request.form['age_group']
            else:
                agegroup = request.form['Age_group']

            allergies = request.form['Allergies']
            if allergies == 'Allergies':
                allergies = request.form['allergies']
            else:
                allergies = request.form['Allergies']

            ailments = request.form['Ailments']
            if ailments == 'Prior Ailments':
                ailments = request.form['ailments']
            else:
                ailments = request.form['Ailments']

            doze = request.form['Doze']
            if doze == 'Doze Name':
                doze = request.form['doze']
            else:
                doze = request.form['Doze']

            appointment = request.form['Date']

            doze1 = request.form['Doze1']
            if doze1 == 'Doze1':
                doze1 = request.form['doze1']
            else:
                doze1 = request.form['Doze1']

            appointment2 = request.form['Date2']

            doze2 = request.form['Doze2']
            if doze2 == 'Doze2':
                doze2 = request.form['doze2']
            else:
                doze2 = request.form['Doze2']
            hospitalid = session['Hospital_id']
            var = 'Vaccinated'
            id1 = request.form.get('id')
            cursor.execute(
                """SELECT * FROM `vaccinated` WHERE `id` LIKE '{}'"""
                    .format(id1))
            d2uau = cursor.fetchall()

            if (d2uau):
                cursor.execute("""UPDATE doze2
                                        SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment1=%s,Doze1=%s,Appointment2=%s,Doze2=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1,
                                appointment2, doze2, id))

                conn.commit()

                cursor.execute("""UPDATE vaccinated
                                                        SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment1=%s,Doze1=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1, id))
                flash("Data Updated Successfully")
                conn.commit()

            else:
                cursor.execute("""UPDATE doze2
                                                        SET  Name=%s ,Address=%s ,NID=%s,Phone_number=%s ,Age_group=%s,Allergies=%s,Prior_ailments=%s,Doze_name=%s ,Appointment1=%s,Doze1=%s,Appointment2=%s,Doze2=%s  WHERE ID=%s""",
                               (name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1,
                                appointment2, doze2, id))

                flash("Data Updated and Added to Vaccinated Successfully")
                conn.commit()

                cursor.execute(
                    "INSERT INTO VACCINATED (id,Name,Address,NID,Phone_number,Age_group,Allergies,Prior_ailments,Doze_name,Appointment1,Doze1,Appointment2,Doze2,Vaccinated,Hospital_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (id, name, address, nid, phone, agegroup, allergies, ailments, doze, appointment, doze1,
                     appointment2, doze2, var, hospitalid))
                conn.commit()




            return redirect('/rdoze2')






@app.route('/searchrecdoze2', methods=['GET', 'POST'])
def searchrecdoze2():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        doze2 = request.form['doze2']
        cursor.execute("SELECT * FROM doze2 WHERE (Name LIKE %s  OR Address LIKE %s OR NID LIKE %s OR Doze_name LIKE %s OR Prior_ailments LIKE %s OR Allergies LIKE %s OR Appointment1 LIKE %s OR Doze1 LIKE %s OR Doze2 LIKE %s OR Appointment2 LIKE %s) and Hospital_id='" + str(s) + "'", (doze2,doze2,doze2,doze2,doze2,doze2,doze2,doze2,doze2,doze2))
        rdoze2= cursor.fetchall()

        if (len(rdoze2) == 0 and doze2 == 'all') or len(doze2)==0:
            cursor.execute("SELECT * FROM doze2 WHERE Hospital_id='" + str(s) + "'")

            rdoze2 = cursor.fetchall()
        return render_template('rdoze2.html', rdoze2=rdoze2)
    return redirect('/rdoze2')



#...................Vaccinated........................


@app.route('/rvaccinated')
def rvaccinated():
    if 'Receptionist_id' in session:
        s = session['Hospital_id']
        cursor.execute("SELECT* FROM `vaccinated` WHERE Hospital_id = '" + str(s) + "'")
        rvaccinated=cursor.fetchall()
        return  render_template('rvaccinated.html',rvaccinated=rvaccinated)
    else:
        return redirect('/')




@app.route('/searchrecv', methods=['GET', 'POST'])
def searchrecv():
    if request.method == "POST" and  'Hospital_id' in session:
        s = session['Hospital_id']
        vax = request.form['vax']
        cursor.execute("SELECT * FROM vaccinated WHERE (Name LIKE %s  OR Address LIKE %s OR NID LIKE %s OR Doze_name LIKE %s OR Prior_ailments LIKE %s OR Allergies LIKE %s OR Appointment1 LIKE %s OR Doze1 LIKE %s OR Doze2 LIKE %s OR Appointment2 LIKE %s) and Hospital_id='" + str(s) + "'", (vax,vax,vax,vax,vax,vax,vax,vax,vax,vax))
        rvaccinated= cursor.fetchall()

        if (len(rvaccinated) == 0 and vax == 'all') or len(vax)==0:
            cursor.execute("SELECT * FROM vaccinated WHERE Hospital_id='" + str(s) + "'")

            rvaccinated = cursor.fetchall()
        return render_template('rvaccinated.html', rvaccinated=rvaccinated)
    return redirect('/rvaccinated')

if __name__=="__main__":
    app.run(debug=True)