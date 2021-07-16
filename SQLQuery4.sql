/*

Cleaning Data in SQL Queries

*/

Select *
from PortfolioProject.dbo.NashvilleHousing

-----------------------------------------------------------------------------

-- Standardize Date Format

Select SaleDateConverted, CONVERT(Date, SaleDate)
from PortfolioProject.dbo.NashvilleHousing

ALTER TABLE NashvilleHousing
ADD SaleDateConverted Date

Update NashvilleHousing
SET SaleDate = CONVERT(Date, SaleDate)

--OR

ALTER TABLE PortfolioProject.dbo.NashvilleHousing
ALTER COLUMN SaleDate  Date

-------------------------------------------------------------------------------

-- Populate Property Address data


Select *
from PortfolioProject.dbo.NashvilleHousing
--where PropertyAddress is null
order by ParcelID


Select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress )
from PortfolioProject.dbo.NashvilleHousing a
JOIN PortfolioProject.dbo.NashvilleHousing b
    on a.ParcelID = b.ParcelID
    AND a.[UniqueID ] <> b.[UniqueID ]
where a.PropertyAddress is Null

Update a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress )
From PortfolioProject.dbo.NashvilleHousing a
JOIN PortfolioProject.dbo.NashvilleHousing b
    on a.ParcelID = b.ParcelID
    AND a.[UniqueID ] <> b.[UniqueID ]
where a.PropertyAddress is Null

-------------------------------------------------------------------------------------------------
-- Breaking out PropertyAddress into Individual Columns (Address, City)

Select PropertyAddress
from PortfolioProject.dbo.NashvilleHousing
--where PropertyAddress is null
--order by ParcelID

Select
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1) as Address,
SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress)) as Address
From PortfolioProject.dbo.NashvilleHousing

ALTER TABLE NashvilleHousing
ADD PropertySpiltAddress NVarchar(255)

Update NashvilleHousing
SET PropertySpiltAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1) 

ALTER TABLE NashvilleHousing
ADD PropertySpiltCity NVarchar(255)

Update NashvilleHousing
SET PropertySpiltCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress))

Select *
from PortfolioProject.dbo.NashvilleHousing

----------------------------------------------------------------------------------------------------------
--Breaking out OwnerAddress into Individual Columns (Address, City, State)

Select OwnerAddress
from PortfolioProject.dbo.NashvilleHousing

Select 
PARSENAME(REPLACE(OwnerAddress, ',', '.' ) , 3),
PARSENAME(REPLACE(OwnerAddress, ',', '.' ) , 2),
PARSENAME(REPLACE(OwnerAddress, ',', '.' ) , 1)
from PortfolioProject.dbo.NashvilleHousing

ALTER TABLE NashvilleHousing
ADD OwnerSplitAddress NVarchar(255)

Update NashvilleHousing
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.' ) , 3)

ALTER TABLE NashvilleHousing
ADD OwnerSpiltCity NVarchar(255)

Update NashvilleHousing
SET OwnerSpiltCity = PARSENAME(REPLACE(OwnerAddress, ',', '.' ) , 2)

ALTER TABLE NashvilleHousing
ADD OwnerSpiltState NVarchar(255)

Update NashvilleHousing
SET  OwnerSpiltState = PARSENAME(REPLACE(OwnerAddress, ',', '.' ) , 1)

------------------------------------------------------------------------------------------------

--Change Y and N to Yes and No in "Sold as Vacant" field

Select Distinct(SoldAsVacant), COUNT(SoldAsVacant)
from  PortfolioProject.dbo.NashvilleHousing
group by SoldAsVacant
order by 2

Select SoldAsVacant, 
CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
     WHEN SoldAsVacant = 'N' THEN 'No'
	 ELSE SoldAsVacant
	 END
from PortfolioProject.dbo.NashvilleHousing

Update NashvilleHousing
SET SoldAsVacant = CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
     WHEN SoldAsVacant = 'N' THEN 'No'
	 ELSE SoldAsVacant
	 END

---------------------------------------------------------------------------------------------------
--Remove Duplicates

WITH RowNumCTE AS (
Select * ,
     ROW_NUMBER() OVER(
	 PARTITION BY ParcelID,
	              PropertyAddress,
				  SalePrice,
				  SaleDate,
				  LegalReference
				  ORDER BY
				    UniqueID
					) row_num
from PortfolioProject.dbo.NashvilleHousing
--order by ParcelID
)

Delete *
From RowNumCTE
where row_num > 1
--Order by PropertyAddress



 -----------------------------------------------------------------------------------------------------------
--Delete Unused Column

Select *
from PortfolioProject.dbo.NashvilleHousing

ALTER TABLE PortfolioProject.dbo.NashvilleHousing
DROP COLUMN OwnerAddress, PropertyAddress, TaxDistrict


ALTER TABLE PortfolioProject.dbo.NashvilleHousing
DROP COLUMN SaleDate
--------------------------------------------------------------------------------------------------------------
