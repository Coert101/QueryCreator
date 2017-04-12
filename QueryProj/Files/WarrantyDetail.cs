using System;
using Yamaha.Business.Model.Base;
using Yamaha.Business.Model.Inventory;
using Yamaha.Business.Model.Warranty.Owner;
using Yamaha.Business.Model.Warranty.Product;

namespace Yamaha.Business.Model.Warranty
{
    public class WarrantyDetail : BaseModel
    {
        public string WarrantyAccountNumber { get; set; }
        public OwnerDetail Owner { get; set; }
        public string SerialNumber { get; set; }
        public StockItemSerial SerialDetail { get; set; }
        public DateTime DateOfSale { get; set; }
        public DateTime ExpiryDate { get; set; }
        public DateTime RegistrationDate { get; set; }
        public ProductDetail ProductDetail { get; set; }
        public PurchaseDetail PurchaseInfo { get; set; }
        public WarrantyStatus Status { get; set; }
        public WarrantyStatus DisplayStatus => (Status == WarrantyStatus.Active && ExpiryDate < DateTime.Now) ? WarrantyStatus.Expired : Status;
        public string TransferredFrom { get; set; }
    }
}
