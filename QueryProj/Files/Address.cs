using Yamaha.Business.Model.Geography;

namespace Yamaha.Business.Model.Warranty.Owner
{
    public class Address
    {
        public string PhysicalCity { get; set; }
        public string PhysicalAddressDescriptor { get; set; }
        public Country Country { get; set; }
        public Province Province { get; set; }
        public string PostalAddress { get; set; }
        public string PostalCode { get; set; }
    }
}
