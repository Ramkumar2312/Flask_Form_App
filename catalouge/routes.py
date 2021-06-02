
import re
from flask.helpers import url_for
from catalouge import app ,db
from flask import render_template,request,redirect,session,flash
from catalouge.models import products

@app.route('/', methods=['GET','POST'])
def home():
    #product_i = '' 
    product_name = ''
    description = ''
    #prod_list = []
    if request.method == 'POST' :

        ''' Fetching data from form using request library '''

        product_id = request.form.get('productid')
        print(product_id)
        product_name = request.form.get('product_name')
        Product_description = request.form.get('desc')

        Prod1 = products()
        Prod1.Product_id = product_id
        Prod1.product_name= product_name
        Prod1.Product_description = Product_description
        db.session.add(Prod1)
        db.session.commit()


        

        # session['prod_id'] = product_id
        # session['prod_name'] = product_name
        # session['prod_desc'] = Product_description

        # prod_list.append(product_id_from_form)
        # prod_list.append(product_name)
        # prod_list.append(description)
        # print(prod_list)

        ''' with sessions we dont have to pass the data to the other template'''
        
        flash('Data is passed','info')
        return redirect(url_for('product_details'))

        # return redirect(url_for('product_details', product_i = product_id_from_form , \
        #                                             product_name = product_name, \
        #                                             description = description   ))


        # return redirect(url_for('product_details', arg_list = prod_list))

        
    else:
        return render_template('home_form.html')



@app.route('/details', methods=['GET','POST'])
def details_page():

    return render_template('details.html')

@app.route('/formdetails', methods=['GET','POST'])
def product_details():

    ''' to work with request args .. i.e passing the data from form to details page by request module. '''
    if request.method == 'POST' :
        entry_id = request.form.get('entry')
        del_entry = products.query.filter_by(id=entry_id).first()
        db.session.delete(del_entry)
        db.session.commit()

        return redirect(url_for('product_details'))
    # product_i = request.args.get('product_i')
    # prod_nm = request.args.get('product_name')
    # desc = request.args.get('description')

    # arg_list = request.args.get('arg_list')
    # print(arg_list)
    else:
        ''' using session to pass data '''
        product_i = products.query.all()
    #prod_id = session['prod_id']
    #prod_name = session['prod_name']
    #prod_desc = session['prod_desc']

    #print(prod_id)
    #return render_template('form_details.html' , product_i = prod_id , desc = prod_desc , \
    
    #                                          prod_nm = prod_name)

        return render_template('form_details.html' , prod = product_i )


