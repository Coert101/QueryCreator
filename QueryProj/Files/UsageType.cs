using Yamaha.Business.Model.Inventory;
using Yamaha.Business.Model.Lookup;
using Yamaha.Business.Model.Warranty.Owner;

namespace Yamaha.Business.Model.Warranty.Product
{
    public class UsageType : LookupCode
    {
        public EntityType Owner { get; set; }
        public ProductClass Class { get; set; }
    }
}
