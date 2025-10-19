from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.schemas import product
from src.models.product import Brand,Category,Product,ProductSection
from src.models.rack_section import RackSection
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
        return HTTPException(400,detail= "Brand not found")
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
        raise HTTPException(status_code=400, detail="This category name is already exists")
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
        return HTTPException(status_code=400, detail=" Category not found")
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
            db_product = Product(name = product.name, category_id = db_category.id, brand_id = db_brand.id, price = product.price)
            db.add(db_product)
            db.commit()
            db.refresh(db_product)
            return db_product
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code = 500 , detail= f"Failed to create Product : {str(e)}")
    except Exception as e:
         print(f" not founded: {str(e)}")
         raise e

# get all product
def get_all_product(db: Session):
    try:
        return db.query(Product).all()
    except Exception as e:
        return HTTPException(status_code=500, detail="error:" f" Failed to Get all product : {str(e)}")
    

# get product by id 
def get_product_by_id(db: Session, product_id :int):
    try:
        
        
        db_product_id = db.query(Product).filter(Product.id == product_id).first()
        if not db_product_id:
            return HTTPException(status_code=400, detail="Product not found")
        return db_product_id
    except Exception as e :
        return HTTPException(status_code=500 ,detail="error : "f" Failed to get product by id :{str(e)}")


# update product
def update_product(db:Session,product_id :int , product_update : str):
    try:
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            return HTTPException(404 ,detail=" product not found")
        db_product.name = product_update
        db.commit()
        db.refresh(db_product)
        return db_product
    except Exception as e :
        return HTTPException(500 , detail="error : "f" Failed to update product : {str(e)}")
    

#Delete product
def delete_product(product_id : int, db: Session):
    try:
        db.query(Product).filter(Product.id == product_id).delete()
        db.commit()
    except Exception as e:
        print(f"Error in Delete product: {str(e)}")
        raise e


# ================= Product Section =================

# Create Product Section
def create_product_section(product_id : int, rack_section_id : int , product_section: ProductSection, db:Session):
    try:
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            raise HTTPException(status_code=400, detail="produc not found")
        db_rack_section = db.query(RackSection).filter(RackSection.id == rack_section_id).first()
        if not db_rack_section:
            raise HTTPException(status_code=400 , detail="Rack Section not found")
        try:
            db_product_section = ProductSection(product_id= db_product.id , racksection_id = db_rack_section.id ,quantity = product_section.quantity)
            db.add(db_product_section)
            db.commit()
            db.refresh(db_product_section)
            return db_product_section
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code = 500 , detail= f"Failed to create Product Section : {str(e)}")
    except Exception as e:
         print(f" not founded: {str(e)}")
         raise e

#get all product section
def get_product_section(db:Session):
    try:
        return db.query(ProductSection).all()
    except Exception as e:
        return HTTPException(500, detail="error: "f"Failed to get all product section {str(e)}")


#get product section by id 
def get_product_section_by_id(db:Session,id:int):
    try:
        product_section= db.query(ProductSection).filter(ProductSection.id == id).first()
        if not product_section:
            raise HTTPException(400,detail="Product section not found")
        return product_section
    except Exception as e :
        raise HTTPException(500 ,detail=f"Failed to get product section by if  {str(e)}")
    

#update product section
def update_product_section(db:Session,id: int, product_section: int):
    try:
        db_id = db.query(ProductSection).filter(ProductSection.id == id).first()
        if not db_id:
            raise HTTPException(400 , detail ="Product section not found")
        db_id.quantity = product_section
        db.commit()
        db.refresh(db_id)
        return db_id
    except Exception as e:
        raise HTTPException(500,detail=f"Failed to update product section  {str(e)}")
    
#delete product section
def delete_product_section(product_section: int,db:Session):
    try:
        db_product_section = db.query(ProductSection).filter(ProductSection.id == product_section).first()
        if not db_product_section:
            raise HTTPException(404,detail= "product section not found")
        db.delete(db_product_section)
        db.commit()
    except Exception as e:
        raise HTTPException(500,detail=f"Failed to deleting product section {str(e)}")
