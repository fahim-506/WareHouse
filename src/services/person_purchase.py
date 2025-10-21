from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.schemas.purchase import SalePersonBase,PurchaseBase,PurchaseCreate
from src.models.purchase import Sale_Person,Purchase
from src.models.product import Product,ProductSection
from typing import List, Dict


# ================= Sale Person =================

#create sale person
def Create_Saleperson(db : Session , person : SalePersonBase):

    # existing = db.query(Sale_Person).filter((Sale_Person.contact==person.contact) & (Sale_Person.name==person.name)).first()
    existing =db.query(Sale_Person).filter(Sale_Person.contact == person.contact).first()
    print(f"Existing: {existing}")
    if existing:
        raise HTTPException(status_code=400, detail="This Sale person already exists")
    if len(str(person.contact)) == 10:
        db_saleperson = Sale_Person(name = person.name , contact = person.contact)
        try:
            db.add(db_saleperson)
            db.commit()
            db.refresh(db_saleperson)
            return db_saleperson
        except Exception as e:
            db.rollback()
            return HTTPException(status_code=500, detail= f"Failed to Add Sale Person :{str(e)}")
        
    else:
        raise HTTPException(status_code=422, detail="Please enter a valid 10-digit contact number.")
    

#get all sale person
def get_sale_person(db: Session):
    try:
        return db.query(Sale_Person).all()
    except Exception as e:
        return HTTPException(status_code=500, detail="error: "f"Failed to get all sale person : {str(e)}")
    
# get sale person by id 
def get_sale_person_by_id(sale_person : int ,db : Session):
    try:
        db_person = db.query(Sale_Person).filter(Sale_Person.id == sale_person).first()
        if not db_person:
            raise HTTPException(status_code=400, detail="Sale Person not found")
        return db_person
    except Exception as e:
        raise HTTPException(status_code=500, detail="error : " f"Failed to get sale person by id : {str(e)}")
    

#update sale person
def update_person(person_id : int, person: str,person_contact:str, db : Session):
    try:
        db_person = db.query(Sale_Person).filter(Sale_Person.id == person_id).first()
        if not db_person:
            raise HTTPException(status_code=400, detail="sale person not found")

        db_person.name = person
        db_person.contact = person_contact
        if len(db_person.contact)==10:

            db.commit()
            db.refresh(db_person)
            return db_person
        else:
            raise HTTPException(status_code =400, detail="please enter valid number")
    except Exception as e:
        raise HTTPException(status_code=500, detail="error : "f"Failed to update sale person: {str(e)}")
    

#Delete sale person
def delete_person(person_id : int , db: Session):
    try:
        db_person=db.query(Sale_Person).filter(Sale_Person.id == person_id).first()
        if not db_person:
            raise HTTPException(404,detail="person not found")
        db.commit()
    except Exception as e:
        print(f"Error in Delete sale person: {str(e)}")
        raise e


# ================= Purchase =================
def create_purchase(person : int, product : int , product_section : int ,purchase : PurchaseCreate,db : Session):
    try:
        db_person = db.query(Sale_Person).filter(Sale_Person.id == person).first()
        if not db_person:
            raise HTTPException(404, detail= "Sale Person not found")
        db_product = db.query(Product).filter(Product.id == product).first()
        if not db_product:
            raise HTTPException(404,detail= "Product not found")
        db_product_section = db.query(ProductSection).filter(ProductSection.id == product_section).first()
        if not db_product_section:
            raise HTTPException(404,detail= "Product Section not found")
        #create purchase
        db_purchase = Purchase(sale_person_id = db_person.id , product_id = db_product.id,
                                   product_section_id= db_product_section.id, quantity = purchase.quantity,date = purchase.date)
        if db_product_section.quantity < db_purchase.quantity:
            raise HTTPException(400 ,detail=f"Only {db_product_section.quantity} items are availabe")
            #Update quantity
        db_product_section.quantity -= purchase.quantity
        db.commit()
        db.refresh(db_product_section)
            #calculate price
        total_price = db_product.price * purchase.quantity
            

        db.add(db_purchase)
        db.commit()
        db.refresh(db_purchase) 
        return {"person_name": db_person.name,"product_name": db_product.name,
                "quantity": db_purchase.quantity, "date":db_purchase.date, "total_price":total_price,"product_section":db_product_section.racksection_id}
    except Exception as e:
        db.rollback()
        raise HTTPException (500, detail = f"Failed to create Purchase : {str(e)}")


#Get all purchase
def get_purchase(db:Session):
    try:
        return db.query(Purchase).all()
    except Exception as e:
        return HTTPException(status_code=500, detail="error: "f"Failed to get all purchase : {str(e)}")
    
#get purchase by id 
def get_purchase_id(purchase : int, db: Session):
    try:
        db_purchase =db.query(Purchase).filter(Purchase.id == purchase).first()
        if not db_purchase:
            raise HTTPException(404,detail="purchase not found")
        return db_purchase
    except Exception as e:
        raise HTTPException(500,detail="error: "f"Failed to get purchase by id : {str(e)}")
    

#Update purchase
def update_purchase(purchase_id : int , purchase : PurchaseCreate, db:Session):
    try:
        db_purchase = db.query(Purchase).filter(Purchase.id == purchase_id).first()
        productsection=db.query(ProductSection).filter(ProductSection.id == db_purchase.product_section_id).first()
        if not db_purchase:
            raise HTTPException(404,detail="purchase not found")
        db_purchase.quantity=purchase.quantity
        db_purchase.date=purchase.date

        db_person=db_purchase.sale_person
        db_product=db_purchase.product
        if productsection.quantity < db_purchase.quantity:
            raise HTTPException(400 ,detail=f"Only {productsection.quantity} items are availabe")
        productsection.quantity -= purchase.quantity
        db.commit()
        db.refresh(productsection)

        total_price =db_purchase.quantity * db_product.price


        db.commit()
        db.refresh(db_purchase)


        return {"person_name":db_person.name,"product_name":db_product.name,"quantity":db_purchase.quantity,
                "date":db_purchase.date,"total_price":total_price,"product_section":productsection.racksection_id}
    
    except Exception as e:
        raise HTTPException(500,detail="error: "f"Failed to update purchase : {str(e)}")


#delete purchase
def delete_purchase(id : int ,db:Session):
    purchase= db.query(Purchase).filter(Purchase.id == id).first()
    if not purchase:
        raise HTTPException(404,detail="purchase not found")
    db.delete(purchase)
    db.commit()
    return {"message":"Purchase deleted"}
        
