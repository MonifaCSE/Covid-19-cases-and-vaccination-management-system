



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
