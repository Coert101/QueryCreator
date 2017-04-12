using System;
using Yamaha.Business.Model.Base;
using Yamaha.Business.Model.Inventory;
using Yamaha.Business.Model.Warranty.Product;

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
