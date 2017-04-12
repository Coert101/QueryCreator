using System;
using Yamaha.Business.Model.Warranty.Owner;

namespace Yamaha.Business.Model.Warranty
{
    public class WarrantySearch
    {
        public string WarrantyAccountNumber { get; set; }
        public string SerialNumber { get; set; }
        public EntityType OwnerType { get; set; }
        public string OwnerCode { get; set; }
        public string OwnerIdentification { get; set; }
        public string OwnerName { get; set; }
        public string OwnerEmailAddress { get; set; }
        public string OwnerCellphoneNumber { get; set; }
        public DateTime DateOfSale { get; set; }
        public DateTime ExpiryDate { get; set; }
        public WarrantyStatus Status { get; set; }
        public WarrantyStatus DisplayStatus
        {
            get { return (Status == WarrantyStatus.Active && ExpiryDate < DateTime.Now) ? WarrantyStatus.Expired : Status; }
        }
    }
}