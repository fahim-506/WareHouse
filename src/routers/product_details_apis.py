from fastapi import APIRouter, Request, Response , Depends, HTTPException
from fastapi.responses import JSONResponse
from src.config.database import get_db
from src.schemas.product import BrandBase,CategoryBase,ProductBase,ProductSectionBase,BrandUpdate
from src.services import product_details
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

# ================= Brand =================

# create Brand
@router.post("/brand", response_model=BrandBase)
def add_Brand(brands : BrandBase, db : Session = Depends(get_db)):
    return product_details.Create_Brand(db ,brands)

#get all brands
@router.get("/brand", response_model=List[BrandBase])
def Get_Brand(db : Session = Depends(get_db)):
    return product_details.Get_brand(db)

# get brand by id 
@router.get("/brand{brand_id}", response_model=BrandBase)
def Get_brand_id(brand_id : int , db : Session =Depends(get_db)):
    return product_details.Get_brand_id(brand_id,db)


#update Brand
@router.put("/brand{brand_id}", response_model=BrandBase)
def Update_brand(brand_id : int ,name = str, db : Session = Depends(get_db)):
    db_brand = product_details.Update_brand(db,brand_id ,name)
    if not db_brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand


#delete Brand
@router.delete("/brand/{brand_id}")
def delete_section(brand_id : int , db : Session = Depends(get_db)):
    success = product_details.Delete_brand(db,brand_id)
    if not success:
        return {"error ": f"Section with id {brand_id} not found"}
    return {"message ": f"Section with id {brand_id} deleted successfully"}

# ================= Category =================

# create category 
@router.post("/category", response_model=CategoryBase)
def add_category(categories : CategoryBase, db : Session = Depends(get_db)):
    return product_details.Create_Category(db ,categories)

#get all category
@router.get("/category", response_model=List[CategoryBase])
def Get_category(db : Session = Depends(get_db)):
    return product_details.Get_category(db)

# get category by id 
@router.get("/category{category_id}", response_model=CategoryBase)
def Get_category_id(category_id : int , db : Session =Depends(get_db)):
    return product_details.Get_category_id(category_id,db)


#update category
@router.put("/category{category_id}",response_model= CategoryBase)
def Update_category(category_id : int ,category:CategoryBase, db : Session = Depends(get_db)):
    db_category = product_details.Update_category(db, category_id ,category.name)
    if not db_category:
        return HTTPException(status_code=404, detail="Category not found")
    return db_category



#delete category
@router.delete("/category/{category_id}")
def delete_category(category_id : int , db : Session = Depends(get_db)):
    success = product_details.Delete_category(db,category_id)
    if not success:
        return {"error ": f"Category with id {category_id} not found"}
    return {"message ": f"Category with id {category_id} deleted successfully"}


# ================= Product =================

#create Product
@router.post("/product",response_model=ProductBase)
def create_product(brand_id: int, category_id: int, product: ProductBase,db: Session= Depends(get_db)):
    try:
        return product_details.create_product(brand_id,category_id,db,product)
    except Exception as e:
        return JSONResponse({"error": f"error in creating {str(e)}"})

