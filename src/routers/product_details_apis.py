from fastapi import APIRouter, Request, Response , Depends, HTTPException
from fastapi.responses import JSONResponse
from src.config.database import get_db
from src.schemas.product import BrandBase,CategoryBase,ProductBase,ProductSectionBase
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

# get all product 
@router.get("/product",response_model=List[ProductBase])
def get_product(db: Session=Depends(get_db)):
    try:
        return product_details.get_all_product(db)
    except Exception as e:
        return HTTPException(400, detail={"error": f"Error in get all product {str(e)}"})


# get product by id
@router.get("/product/{product_id}", response_model=ProductBase)
def get_product_by_id(product_id : int , db : Session = Depends(get_db)):
    try:
        return product_details.get_product_by_id(db,product_id)
    except Exception as e:
        return HTTPException(400, detail={"error": f"Error in get product by id {str(e)}"})

# update product 
@router.put("/product{product_id}",response_model=ProductBase)
def update_product(product_id : int, product: ProductBase, db : Session = Depends(get_db)):
    try:
        db_product = product_details.update_product(db,product_id,product.name)
        if not db_product:
            return HTTPException(404, detail="product not found")
        return db_product
    except Exception as e:
        return HTTPException(500, detail="error: "f"Error in Update product : {str(e)}")
    
#Delete product
@router.delete("/product/{id}")
def delete_product(product_id : int ,db :Session=Depends(get_db),):
    try:
        product_details.delete_product(product_id,db)
        return JSONResponse({"message": "delete sucessfully"}, status_code=200)
    except Exception as e:
        return HTTPException(status_code=404,detail="error :" f"Error in deleting: {str(e)}")


# ================= Product Section =================

#create product section
@router.post("/product_section",response_model=ProductSectionBase)
def create_product_section(product_id : int, rack_section_id : int , product_section: ProductSectionBase, db:Session= Depends(get_db)):
    try:
        return product_details.create_product_section(product_id,rack_section_id,product_section,db)
    except Exception as e:
        return JSONResponse({"error": f"error in creating {str(e)}"})


#get all product section
@router.get("/product_section",response_model=List[ProductSectionBase])
def get_product_section(db:Session=Depends(get_db)):
    try:
        return product_details.get_product_section(db)
    except Exception as e:
        return HTTPException(400, detail={"error": f"Error in get all product section {str(e)}"})
    

#get product section by id 
@router.get("/product_section/{id}",response_model=ProductSectionBase)
def get_product_section_by_id(id : int ,db:Session=Depends(get_db)):
    try:
        return product_details.get_product_section_by_id(db,id)
    except Exception as e:
        return HTTPException (500 ,detail={"error ": f"Error in get product section by id {str(e)}"})
                              