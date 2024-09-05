# import streamlit as st
# import requests
# import json

# # FastAPI endpoint URL
# API_URL = "http://localhost:8001/api/v1/predict"

# st.title("House Price Prediction")

# # Input fields
# mssubclass = st.number_input("MS SubClass", min_value=20, max_value=190, value=20)
# mszoning = st.selectbox("MS Zoning", ["C", "FV", "RH", "RL", "RM"])
# lotfrontage = st.number_input("Lot Frontage", min_value=0, max_value=500, value=80)
# lotarea = st.number_input("Lot Area", min_value=1000, max_value=200000, value=11622)
# street = st.selectbox("Street", ["Grvl", "Pave"])
# lotshape = st.selectbox("Lot Shape", ["Reg", "IR1", "IR2", "IR3"])
# landcontour = st.selectbox("Land Contour", ["Lvl", "Bnk", "HLS", "Low"])
# utilities = st.selectbox("Utilities", ["AllPub", "NoSeWa"])
# lotconfig = st.selectbox("Lot Config", ["Inside", "Corner", "CulDSac", "FR2", "FR3"])
# landslope = st.selectbox("Land Slope", ["Gtl", "Mod", "Sev"])
# neighborhood = st.selectbox("Neighborhood", ["Blmngtn", "Blueste", "BrDale", "BrkSide", "ClearCr", "CollgCr", "Crawfor", "Edwards", "Gilbert", "IDOTRR", "MeadowV", "Mitchel", "NAmes", "NoRidge", "NPkVill", "NridgHt", "NWAmes", "OldTown", "SWISU", "Sawyer", "SawyerW", "Somerst", "StoneBr", "Timber", "Veenker"])
# condition1 = st.selectbox("Condition 1", ["Artery", "Feedr", "Norm", "RRNn", "RRAn", "PosN", "PosA", "RRNe", "RRAe"])
# condition2 = st.selectbox("Condition 2", ["Artery", "Feedr", "Norm", "RRNn", "RRAn", "PosN", "PosA", "RRNe", "RRAe"])
# bldgtype = st.selectbox("Building Type", ["1Fam", "2FmCon", "Duplx", "TwnhsE", "TwnhsI"])
# housestyle = st.selectbox("House Style", ["1Story", "1.5Fin", "1.5Unf", "2Story", "2.5Fin", "2.5Unf", "SFoyer", "SLvl"])
# overallqual = st.slider("Overall Quality", min_value=1, max_value=10, value=5)
# overallcond = st.slider("Overall Condition", min_value=1, max_value=10, value=6)
# yearbuilt = st.number_input("Year Built", min_value=1872, max_value=2022, value=1961)
# yearremodadd = st.number_input("Year Remodeled", min_value=1950, max_value=2022, value=1961)
# roofstyle = st.selectbox("Roof Style", ["Flat", "Gable", "Gambrel", "Hip", "Mansard", "Shed"])
# roofmatl = st.selectbox("Roof Material", ["ClyTile", "CompShg", "Membran", "Metal", "Roll", "Tar&Grv", "WdShake", "WdShngl"])
# exterior1st = st.selectbox("Exterior 1st", ["AsbShng", "AsphShn", "BrkComm", "BrkFace", "CBlock", "CemntBd", "HdBoard", "ImStucc", "MetalSd", "Other", "Plywood", "PreCast", "Stone", "Stucco", "VinylSd", "Wd Sdng", "WdShing"])
# exterior2nd = st.selectbox("Exterior 2nd", ["AsbShng", "AsphShn", "BrkComm", "BrkFace", "CBlock", "CemntBd", "HdBoard", "ImStucc", "MetalSd", "Other", "Plywood", "PreCast", "Stone", "Stucco", "VinylSd", "Wd Sdng", "WdShing"])
# masvnrtype = st.selectbox("Masonry Veneer Type", ["BrkCmn", "BrkFace", "CBlock", "None", "Stone"])
# masvnrarea = st.number_input("Masonry Veneer Area", min_value=0, max_value=1600, value=0)
# exterqual = st.selectbox("Exterior Quality", ["Ex", "Gd", "TA", "Fa", "Po"])
# extercond = st.selectbox("Exterior Condition", ["Ex", "Gd", "TA", "Fa", "Po"])
# foundation = st.selectbox("Foundation", ["BrkTil", "CBlock", "PConc", "Slab", "Stone", "Wood"])
# bsmtqual = st.selectbox("Basement Quality", ["Ex", "Gd", "TA", "Fa", "Po", "NA"])
# bsmtcond = st.selectbox("Basement Condition", ["Ex", "Gd", "TA", "Fa", "Po", "NA"])
# bsmtexposure = st.selectbox("Basement Exposure", ["Gd", "Av", "Mn", "No", "NA"])
# bsmtfintype1 = st.selectbox("Basement Finish Type 1", ["GLQ", "ALQ", "BLQ", "Rec", "LwQ", "Unf", "NA"])
# bsmtfinsf1 = st.number_input("Basement Finished SF 1", min_value=0, max_value=5000, value=468)
# bsmtfintype2 = st.selectbox("Basement Finish Type 2", ["GLQ", "ALQ", "BLQ", "Rec", "LwQ", "Unf", "NA"])
# bsmtfinsf2 = st.number_input("Basement Finished SF 2", min_value=0, max_value=5000, value=144)
# bsmtunfsf = st.number_input("Basement Unfinished SF", min_value=0, max_value=5000, value=270)
# totalbsmtsf = st.number_input("Total Basement SF", min_value=0, max_value=6000, value=882)
# heating = st.selectbox("Heating", ["Floor", "GasA", "GasW", "Grav", "OthW", "Wall"])
# heatingqc = st.selectbox("Heating QC", ["Ex", "Gd", "TA", "Fa", "Po"])
# centralair = st.selectbox("Central Air", ["N", "Y"])
# electrical = st.selectbox("Electrical", ["SBrkr", "FuseA", "FuseF", "FuseP", "Mix"])
# firstflrsf = st.number_input("1st Floor SF", min_value=300, max_value=5000, value=896)
# secondflrsf = st.number_input("2nd Floor SF", min_value=0, max_value=5000, value=0)
# lowqualfinsf = st.number_input("Low Quality Finished SF", min_value=0, max_value=5000, value=0)
# grlivarea = st.number_input("Above Grade Living Area SF", min_value=300, max_value=10000, value=896)
# bsmtfullbath = st.number_input("Basement Full Bathrooms", min_value=0, max_value=3, value=0)
# bsmthalfbath = st.number_input("Basement Half Bathrooms", min_value=0, max_value=2, value=0)
# fullbath = st.number_input("Full Bathrooms", min_value=0, max_value=4, value=1)
# halfbath = st.number_input("Half Bathrooms", min_value=0, max_value=2, value=0)
# bedroomabvgr = st.number_input("Bedrooms Above Grade", min_value=0, max_value=8, value=2)
# kitchenabvgr = st.number_input("Kitchens Above Grade", min_value=0, max_value=3, value=1)
# kitchenqual = st.selectbox("Kitchen Quality", ["Ex", "Gd", "TA", "Fa", "Po"])
# totrmsabvgrd = st.number_input("Total Rooms Above Grade", min_value=2, max_value=14, value=5)
# functional = st.selectbox("Functional", ["Typ", "Min1", "Min2", "Mod", "Maj1", "Maj2", "Sev", "Sal"])
# fireplaces = st.number_input("Fireplaces", min_value=0, max_value=4, value=0)
# garagetype = st.selectbox("Garage Type", ["2Types", "Attchd", "Basment", "BuiltIn", "CarPort", "Detchd", "NA"])
# garageyrblt = st.number_input("Garage Year Built", min_value=1900, max_value=2022, value=1961)
# garagefinish = st.selectbox("Garage Finish", ["Fin", "RFn", "Unf", "NA"])
# garagecars = st.number_input("Garage Cars", min_value=0, max_value=4, value=1)
# garagearea = st.number_input("Garage Area", min_value=0, max_value=1400, value=730)
# garagequal = st.selectbox("Garage Quality", ["Ex", "Gd", "TA", "Fa", "Po", "NA"])
# garagecond = st.selectbox("Garage Condition", ["Ex", "Gd", "TA", "Fa", "Po", "NA"])
# paveddrive = st.selectbox("Paved Drive", ["Y", "P", "N"])
# wooddecksf = st.number_input("Wood Deck SF", min_value=0, max_value=900, value=140)
# openporchsf = st.number_input("Open Porch SF", min_value=0, max_value=500, value=0)
# enclosedporch = st.number_input("Enclosed Porch SF", min_value=0, max_value=500, value=0)
# threessnporch = st.number_input("Three Season Porch SF", min_value=0, max_value=500, value=0)
# screenporch = st.number_input("Screen Porch SF", min_value=0, max_value=500, value=120)
# poolarea = st.number_input("Pool Area", min_value=0, max_value=800, value=0)
# fence = st.selectbox("Fence", ["GdPrv", "MnPrv", "GdWo", "MnWw", "NA"])
# miscval = st.number_input("Misc Value", min_value=0, max_value=15000, value=0)
# mosold = st.number_input("Month Sold", min_value=1, max_value=12, value=6)
# yrsold = st.number_input("Year Sold", min_value=2006, max_value=2022, value=2010)
# saletype = st.selectbox("Sale Type", ["WD", "CWD", "VWD", "New", "COD", "Con", "ConLw", "ConLI", "ConLD", "Oth"])
# salecondition = st.selectbox("Sale Condition", ["Normal", "Abnorml", "AdjLand", "Alloca", "Family", "Partial"])

# if st.button("Predict Price"):
#     # Prepare the input data
#     input_data = {
#         "inputs": [
#             {
#                 "MSSubClass": mssubclass,
#                 "MSZoning": mszoning,
#                 "LotFrontage": lotfrontage,
#                 "LotArea": lotarea,
#                 "Street": street,
#                 "LotShape": lotshape,
#                 "LandContour": landcontour,
#                 "Utilities": utilities,
#                 "LotConfig": lotconfig,
#                 "LandSlope": landslope,
#                 "Neighborhood": neighborhood,
#                 "Condition1": condition1,
#                 "Condition2": condition2,
#                 "BldgType": bldgtype,
#                 "HouseStyle": housestyle,
#                 "OverallQual": overallqual,
#                 "OverallCond": overallcond,
#                 "YearBuilt": yearbuilt,
#                 "YearRemodAdd": yearremodadd,
#                 "RoofStyle": roofstyle,
#                 "RoofMatl": roofmatl,
#                 "Exterior1st": exterior1st,
#                 "Exterior2nd": exterior2nd,
#                 "MasVnrType": masvnrtype,
#                 "MasVnrArea": masvnrarea,
#                 "ExterQual": exterqual,
#                 "ExterCond": extercond,
#                 "Foundation": foundation,
#                 "BsmtQual": bsmtqual,
#                 "BsmtCond": bsmtcond,
#                 "BsmtExposure": bsmtexposure,
#                 "BsmtFinType1": bsmtfintype1,
#                 "BsmtFinSF1": bsmtfinsf1,
#                 "BsmtFinType2": bsmtfintype2,
#                 "BsmtFinSF2": bsmtfinsf2,
#                 "BsmtUnfSF": bsmtunfsf,
#                 "TotalBsmtSF": totalbsmtsf,
#                 "Heating": heating,
#                 "HeatingQC": heatingqc,
#                 "CentralAir": centralair,
#                 "Electrical": electrical,
#                 "1stFlrSF": firstflrsf,
#                 "2ndFlrSF": secondflrsf,
#                 "LowQualFinSF": lowqualfinsf,
#                 "GrLivArea": grlivarea,
#                 "BsmtFullBath": bsmtfullbath,
#                 "BsmtHalfBath": bsmthalfbath,
#                 "FullBath": fullbath,
#                 "HalfBath": halfbath,
#                 "BedroomAbvGr": bedroomabvgr,
#                 "KitchenAbvGr": kitchenabvgr,
#                 "KitchenQual": kitchenqual,
#                 "TotRmsAbvGrd": totrmsabvgrd,
#                 "Functional": functional,
#                 "Fireplaces": fireplaces,
#                 "GarageType": garagetype,
#                 "GarageYrBlt": garageyrblt,
#                 "GarageFinish": garagefinish,
#                 "GarageCars": garagecars,
#                 "GarageArea": garagearea,
#                 "GarageQual": garagequal,
#                 "GarageCond": garagecond,
#                 "PavedDrive": paveddrive,
#                 "WoodDeckSF": wooddecksf,
#                 "OpenPorchSF": openporchsf,
#                 "EnclosedPorch": enclosedporch,
#                 "3SsnPorch": threessnporch,
#                 "ScreenPorch": screenporch,
#                 "PoolArea": poolarea,
#                 "Fence": fence,
#                 "MiscVal": miscval,
#                 "MoSold": mosold,
#                 "YrSold": yrsold,
#                 "SaleType": saletype,
#                 "SaleCondition": salecondition
#             }
#         ]
#     }

#     # Make a POST request to the FastAPI endpoint
#     headers = {
#         "accept": "application/json",
#         "Content-Type": "application/json"
#     }
#     response = requests.post(API_URL, headers=headers, json=input_data)

#     if response.status_code == 200:
#         result = response.json()
#         predicted_price = result[0]  # Assuming the API returns a list with a single prediction
#         st.success(f"Predicted House Price: ${predicted_price:,.2f}")
#     else:
#         st.error(f"Error in prediction. Status code: {response.status_code}. Please try again.")

# st.markdown("---")
# st.markdown("This app uses a machine learning model to predict house prices based on various features.")







import streamlit as st
import requests
import json

# FastAPI endpoint URL
API_URL = "http://localhost:8001/api/v1/predict"

st.title("House Price Prediction")

# Input fields
mssubclass = st.number_input("MS SubClass", min_value=20, max_value=190, value=20)
mszoning = st.selectbox("MS Zoning", ["C", "FV", "RH", "RL", "RM"])
lotfrontage = st.number_input("Lot Frontage", min_value=0, max_value=500, value=80)
lotarea = st.number_input("Lot Area", min_value=1000, max_value=200000, value=11622)
street = st.selectbox("Street", ["Grvl", "Pave"])
lotshape = st.selectbox("Lot Shape", ["Reg", "IR1", "IR2", "IR3"])
landcontour = st.selectbox("Land Contour", ["Lvl", "Bnk", "HLS", "Low"])
utilities = st.selectbox("Utilities", ["AllPub", "NoSeWa"])
lotconfig = st.selectbox("Lot Config", ["Inside", "Corner", "CulDSac", "FR2", "FR3"])
landslope = st.selectbox("Land Slope", ["Gtl", "Mod", "Sev"])
neighborhood = st.selectbox("Neighborhood", ["Blmngtn", "Blueste", "BrDale", "BrkSide", "ClearCr", "CollgCr", "Crawfor", "Edwards", "Gilbert", "IDOTRR", "MeadowV", "Mitchel", "NAmes", "NoRidge", "NPkVill", "NridgHt", "NWAmes", "OldTown", "SWISU", "Sawyer", "SawyerW", "Somerst", "StoneBr", "Timber", "Veenker"])
condition1 = st.selectbox("Condition 1", ["Artery", "Feedr", "Norm", "RRNn", "RRAn", "PosN", "PosA", "RRNe", "RRAe"])
condition2 = st.selectbox("Condition 2", ["Artery", "Feedr", "Norm", "RRNn", "RRAn", "PosN", "PosA", "RRNe", "RRAe"])
bldgtype = st.selectbox("Building Type", ["1Fam", "2FmCon", "Duplx", "TwnhsE", "TwnhsI"])
housestyle = st.selectbox("House Style", ["1Story", "1.5Fin", "1.5Unf", "2Story", "2.5Fin", "2.5Unf", "SFoyer", "SLvl"])
overallqual = st.slider("Overall Quality", min_value=1, max_value=10, value=5)
overallcond = st.slider("Overall Condition", min_value=1, max_value=10, value=6)
yearbuilt = st.number_input("Year Built", min_value=1872, max_value=2022, value=1961)
yearremodadd = st.number_input("Year Remodeled", min_value=1950, max_value=2022, value=1961)

# ... Add more input fields for the remaining features ...

if st.button("Predict Price"):
    # Prepare the input data
    input_data = {
        "inputs": [
            {
                "MSSubClass": mssubclass,
                "MSZoning": mszoning,
                "LotFrontage": lotfrontage,
                "LotArea": lotarea,
                "Street": street,
                "LotShape": lotshape,
                "LandContour": landcontour,
                "Utilities": utilities,
                "LotConfig": lotconfig,
                "LandSlope": landslope,
                "Neighborhood": neighborhood,
                "Condition1": condition1,
                "Condition2": condition2,
                "BldgType": bldgtype,
                "HouseStyle": housestyle,
                "OverallQual": overallqual,
                "OverallCond": overallcond,
                "YearBuilt": yearbuilt,
                "YearRemodAdd": yearremodadd,
                # ... Add the remaining features here ...
            }
        ]
    }

    # Make a POST request to the FastAPI endpoint
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.post(API_URL, headers=headers, json=input_data)

    if response.status_code == 200:
        result = response.json()
        predicted_price = result[0]  # Assuming the API returns a list with a single prediction
        st.success(f"Predicted House Price: ${predicted_price:,.2f}")
    else:
        st.error(f"Error in prediction. Status code: {response.status_code}. Please try again.")

st.markdown("---")
st.markdown("This app uses a machine learning model to predict house prices based on various features.")