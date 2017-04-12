using Yamaha.Business.Model.Base;

namespace Yamaha.Business.Model.Warranty.Owner
{
    public class OwnerSearch : BaseModel
    {
        public string OwnerCode { get; set; }
        public string IdentificationNumber { get; set; }
        public string Name { get; set; }
        public string TelephoneNumber { get; set; }
        public string CellphoneNumber { get; set; }
        public string EmailAddress { get; set; }
    }
}


