using System;
using System.Collections.Generic;
using Yamaha.Business.Model.Base;
using Yamaha.Business.Model.Lookup;
using Yamaha.Business.Model.Warranty.Owner;

namespace Yamaha.Business.Model.Warranty
{
    public class WarrantyRegistration : BaseModel
    {
        public OwnerDetail Owner { get; set; }
        public DateTime CreatedOn { get; set; }
        public string CreatedBy { get; set; }
        public DateTime ChangedOn { get; set; }
        public List<WarrantyRegistrationItem> Serials { get; set; }
        public IList<MediaSource> MediaSources { get; set; }
        public YesNoQuestion PreviousOwnership { get; set; }
    }
}
