from typing import Optional

from fastapi import APIRouter
from pydantic import Field

from common.base_definition import BaseDefinition
from models.correlation.correlation import correlation_function


class CorrRequest(BaseDefinition):
    dataset: str = Field(..., title="The dataset code as defined in indicatorMeta file", example="wdi")
    category: str = Field(..., title="The category of the indicator as defined in indicatorMeta file ", example="Financial Sector")
    country: str = Field(..., title="the iso-3 code for the SIDS country", example="SGP")
    year: int = Field(..., title = "The year under consideration", example= 2014)


class CorrResponse(BaseDefinition):
    country_corr: Optional[dict]




router = APIRouter(
    prefix="/correlation",
    tags=["Correlation Model"],
    responses={404: {"description": "Not found"}},
)


@router.post('/predict', response_model=CorrResponse)
async def correlation(req: CorrRequest):
    country_corr= correlation_function(req.dataset,req.category,req.country,req.year) 
    return CorrResponse(country_corr=country_corr)


