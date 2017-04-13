using System;
using Yamaha.Business.Model.Base;
using Yamaha.Business.Model.Inventory;
using Yamaha.Business.Model.Warranty.Product;

//#PK=LineNumber,DateOfSale
//#FK=Owner,SerialDetail,ExpiryDate #REF=WarrantyRegistration #NAME=Owner
//#FK=Owner2,SerialDetail2,ExpiryDate2 #REF=WarrantyRegistration #NAME=Owner2

namespace Yamaha.Business.Model.Warranty
{
    public class WarrantyRegistrationItem : BaseModel
    {
        public int LineNumber { get; set; }
        public DateTime DateOfSale { get; set; }
        public DateTime ExpiryDate { get; set; }
        public StockItemSerial SerialDetail { get; set; }
        public ProductDetail ProductDetail { get; set; }
        public bool IsProductDetailComplete { get; set; }
        public PurchaseDetail PurchaseDetail { get; set; }
        public bool IsPurchaseDetailComplete { get; set; }
    }
}
