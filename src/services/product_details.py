from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.schemas import product
from src.models.product import Brand,Category,Product,ProductSection
from typing import List, Dict

# ================= Brand =================

#create Brand

def Create_Brand(db : Session, brand : product.BrandBase):
    existing = db.query(Brand).filter(Brand.name == brand.name).first()
    if existing:
        raise HTTPException(status_code=400, detail = "This Brand name is already exists")
     
    db_brand = Brand(name = brand.name)
    try:
        db.add(db_brand)
        db.commit()
        db.refresh(db_brand)
        return db_brand
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f" Failed to create Brand : {str(e)}")
    

#read all brands
def Get_brand(db : Session):
    return db.query(Brand).all()

# read brand by id 
def Get_brand_id(brand_id : int , db : Session):
    db_brand_id = db.query(Brand).filter(Brand.id == brand_id).first()
    if not db_brand_id:
        raise HTTPException(status_code=400, detail=" Brand not found")
    return db_brand_id

#Update brand
def Update_brand(db : Session, brand_id : int , brand_update : str):
    db_brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if not db_brand:
        return None
    print(f"db brand : {db_brand}")
    print(f"db name : {db_brand.name}")
    print(f"brand_update : {brand_update}")
    db_brand.name = brand_update
    db.commit()
    db.refresh(db_brand)
    return db_brand


#delete Brand
def Delete_brand(db : Session, brand_id : int ):
    db_brand = db.query(Brand).filter(Brand.id ==brand_id).first()
    if db_brand:
        db.delete(db_brand)
        db.commit()
        return True
    return False
    

# ================= Category =================

# create category
def Create_Category(db : Session, category : product.CategoryBase):
    existing = db.query(Category).filter(Category.name == category.name).first()
    if existing: 
        raise HTTPException(status_code=40, detail="This category name is already exists")
    db_category = Category(name= category.name)
    try:
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f" Failed to create Category : {str(e)}")
    

#read all category
def Get_category(db : Session):
    return db.query(Category).all()


# read category by id 
def Get_category_id(category_id : int , db : Session):
    db_category_id = db.query(Category).filter(Category.id == category_id).first()
    if not db_category_id:
        raise HTTPException(status_code=400, detail=" Category not found")
    return db_category_id


#Update category
def Update_category(db : Session, category_id : int , category_update : str):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        return None
    print(f"db brand : {db_category}")
    db_category.name = category_update
    db.commit()
    db.refresh(db_category)
    return db_category


#delete category
def Delete_category(db : Session, category_id : int ):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False


# ================= Product =================

#create Product
def create_product(brand_id: int, category_id: int, db: Session, product: product.ProductBase):
    try:
        db_brand = db.query(Brand).filter(Brand.id == brand_id).first()
        if not db_brand:
            raise HTTPException(status_code=400, detail="brand not found")
        
        db_category = db.query(Category).filter(Category.id == category_id).first()
        if not db_category:
            raise HTTPException(status_code=400, detail="category not found")
        
        existing = db.query(Product).filter(Product.name == product.name).first()
        if existing:
            raise HTTPException(status_code = 400, detail = " This Product name is already exists")
        
        try:
            db_product = Product(name = product.name, category_id = db_category.id,brand_id = db_brand.id, price = product.price)
            db.add(db_product)
            db.commit()
            db.refresh(db_product)
            return db_product
        except Exception as e:
            db.rollback()
            return HTTPException(status_code = 500 , detail= f"Failed to create Product : {str(e)}")
    except Exception as e:
         print(f" not founded: {str(e)}")
         raise e
