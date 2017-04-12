using System.Collections.Generic;
using Yamaha.Business.Model.Base;
using Yamaha.Business.Model.Lookup;
using Yamaha.Business.Model.Warranty.Product;

namespace Yamaha.Business.Model.Warranty
{
    public class PurchaseDetail : BaseModel
    {
        public string Salesperson { get; set; }
        public string WarrantyAccountNumber { get; set; }
        public string Model { get; set; }
        public string Accessories { get; set; }
        public decimal Price { get; set; }
        public IList<UsageType> Usages { get; set; }
        public string UsageFrequency { get; set; }
        public string UsageOther { get; set; }
        public string PurchaseReason { get; set; }
        public YesNoQuestion HasSeenAdvertising { get; set; }
        public YesNoQuestion HasTradeIn { get; set; }
        public YesNoQuestion OwnsOtherYamahaProducts { get; set; }
        public string BrandsEvaluated { get; set; }
        public string ServiceDealership { get; set; }
        public IList<MediaSource> MediaSources { get; set; }
        public YesNoQuestion PreviousOwnership { get; set; }
    }
}
