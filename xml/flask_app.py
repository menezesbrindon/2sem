import os
from flask import Flask, request, json
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

secretKey = "12345" #os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="jeevanidhi",
    password=secretKey,
    hostname="jeevanidhi.mysql.pythonanywhere-services.com",
    databasename="jeevanidhi$default",
)

app = Flask(__name__)
app.config["DEBUG"] = True

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = secretKey
app_root = "/api/v1"

db = SQLAlchemy(app)

class Donor(db.Model):
    __tablename__ = "Donor"
    id = db.Column(db.BigInteger, primary_key=True)
    rollNumber = db.Column(db.String(100))
    name = db.Column(db.String(255))
    bloodType = db.Column(db.String(10))
    birthDate = db.Column(db.DateTime)
    lastDonationDate = db.Column(db.DateTime)
    panchayat = db.Column(db.String(255))
    weight = db.Column(db.String(100))
    timesDonated = db.Column(db.Integer)
    phoneNumber = db.Column(db.String(255))
    email = db.Column(db.String(255))
    address = db.Column(db.String(1000))
    plateletDonor = db.Column(db.Boolean)
    active = db.Column(db.Boolean)

class Donation(db.Model):
    __tablename__ = "Donation"
    id = db.Column(db.BigInteger, primary_key=True)
    donationDate = db.Column(db.DateTime)
    hospital = db.Column(db.String(255))
    notes = db.Column(db.String(1000))
    donors = db.relationship('Donor', secondary=Donates, backref='donations')

Donates = db.Table('Donates',
    db.Column('donorId', db.Integer, db.ForeignKey('Donor.id')),
    db.Column('donationId', db.Integer, db.ForeignKey('Donation.id'))
)

@app.route(app_root + '/donors/<id>', methods=['GET'])
def getDonor(id):
	#group = request.args.get('g')
	#panchayat = request.args.get('p')
	#name = request.args.get('n')
	#print(group)
	donor = db.session.query(Donor).filter(Donor.active==True).filter(Donor.id==id).first();
	if donor is not None:
		return json.dumps(donor.__dict__, indent=4, sort_keys=True, default=str)
	else:
		return('', 404)

@app.route(app_root + '/donors', methods=['GET'])
def getDonors():
	group = request.args.get('g')
	panchayat = request.args.get('p')
	name = request.args.get('n')
	#print(group)
	#donors = db.session.query(Donor).filter((Donor.active==True),(Donor.bloodType.in_(group.split(',')))).order_by(-Donor.lastDonationDate)
	if(name is not None):
		donors = db.session.query(Donor).filter(Donor.active==True, Donor.profile==user.profile).filter(Donor.name.like(name + "%")).order_by(-Donor.lastDonationDate).all();
		#donors = db.session.query(Donor).filter((Donor.active==True), Donor.name)
	else:
		query = db.session.query(Donor).filter(Donor.active==True)
		if(group is not None):
			query = query.filter(Donor.bloodType.in_(group.split(',')))
		if(panchayat is not None):
			query = query.filter(Donor.panchayat.in_(panchayat.split(',')))
		donors = query.order_by(-Donor.lastDonationDate).all();
		#rs = Donor.query.order_by(-Donor.lastDonationDate).limit(5).all()
	if(donors is not None):
		return json.dumps([d.__dict__ for d in donors], indent=4, sort_keys=True, default=str)
	else:
		return('', 404)

@app.route(app_root + '/donors', methods=['POST'])
def createDonors():
    #try:
	donor_request = request.get_json()
	#print(donor_request)
	donor = Donor.query.filter(Donor.active==True).filter(Donor.id==donor_request["id"]).first()
	if donor is not None:
		donor.rollNumber = donor_request['rollNumber']
		donor.name = donor_request['name']
		donor.bloodType = donor_request['bloodType']
		donor.birthDate = datetime.strptime(donor_request['birthDate'], '%Y-%m-%d')
		donor.lastDonationDate = datetime.strptime(donor_request['lastDonationDate'], '%Y-%m-%d')
		donor.panchayat = donor_request['panchayat']
		donor.weight = donor_request['weight']
		donor.timesDonated = donor_request['timesDonated']
		donor.phoneNumber = donor_request['phoneNumber']
		donor.email = donor_request['email']
		donor.address = donor_request['address']
		donor.plateletDonor = donor_request['plateletDonor']
		donor.profile = user.profile
		donor.active = donor_request['active']
		db.session.commit()
		return('',200)
	else:
		donor = Donor(rollNumber=donor_request['rollNumber'],name=donor_request['name'],bloodType=donor_request['bloodType'],
			birthDate=datetime.strptime(donor_request['birthDate'], '%Y-%m-%d'),
			lastDonationDate=datetime.strptime(donor_request['lastDonationDate'], '%Y-%m-%d'),
			panchayat=donor_request['panchayat'],weight=donor_request['weight'],timesDonated=donor_request['timesDonated'],
			phoneNumber=donor_request['phoneNumber'],email=donor_request['email'],address=donor_request['address'],
			plateletDonor=donor_request['plateletDonor'],profile=user.profile, active = donor_request['active'])
		db.session.add(donor)
		db.session.commit()
		return('',201)
	#   except:
	#       print(sys.exc_info())
	#       raise webapp2.exc.HTTPBadRequest()

@app.route(app_root + '/donations/<id>', methods=['GET'])
def getDonation(id):
	donation = db.session.query(Donation).filter(Donation.id==id).first();
	#print(donation.donors)
	if donation is not None:
		return json.dumps(donation.__dict__, indent=4, sort_keys=True, default=str)
	else:
		return('', 404)

@app.route(app_root + '/donations/<id>/donors', methods=['GET'])
def getDonationDonors(id):
	donation = db.session.query(Donation).filter(Donation.id==id).first();
	#print(donation.donors)
	if donation is not None and donation.donors is not None:
		return json.dumps([d.__dict__ for d in donation.donors], indent=4, sort_keys=True, default=str)
	else:
		return('', 404)

@app.route(app_root + '/donations', methods=['GET'])
def getDonations():
	donations = db.session.query(Donation).order_by(-Donation.donationDate).all()
	if(donations is not None):
		return json.dumps([d.__dict__ for d in donations], indent=4, sort_keys=True, default=str)
	else:
		return('', 404)

@app.route(app_root + '/donations', methods=['POST'])
def createDonation():
    #try:
	donation_request = request.get_json()
	#print(donation_request)
	donation = Donation.query.filter(Donation.profile==user.profile).filter(Donation.id==donation_request["id"]).first()
	if donation is not None:
		donation.donationDate = datetime.strptime(donation_request['donationDate'], '%Y-%m-%d')
		donation.hospital = donation_request['hospital']
		donation.notes = donation_request['notes']
		donation.profile = user.profile
		donorIds=donation_request['donorIds']
		donors = []
		for id in donorIds:
			#print(id)
			donor = Donor.query.filter(Donor.active==True, Donor.profile==user.profile).filter(Donor.id==id).first()
			if donor is not None:
			   donors.append(donor)
		donation.donors = donors
		db.session.commit()
		return('',200)
	else:
		donation = Donation(donationDate=datetime.strptime(donation_request['donationDate'], '%Y-%m-%d'),
			hospital=donation_request['hospital'], notes=donation_request['notes'], profile=user.profile)

		donorIds=donation_request['donorIds']
		for id in donorIds:
			#print(id)
			donor = Donor.query.filter(Donor.active==True, Donor.profile==user.profile).filter(Donor.id==id).first()
			if donor is not None:
				donation.donors.append(donor)
		db.session.add(donation)
		db.session.commit()
		return('',201)
	#   except:
	#       print(sys.exc_info())
	#       raise webapp2.exc.HTTPBadRequest()

