using Yamaha.Business.Model.Lookup;

namespace Yamaha.Business.Model.Warranty.Owner
{
    public class AgeGroup : LookupId
    {
        public int AgeFrom { get; set; }
        public int AgeTo { get; set; }
    }
}
