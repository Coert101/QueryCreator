using System;
using System.Collections.Generic;
using Yamaha.Business.Model.Base;

namespace Yamaha.Business.Model.Warranty.Owner
{
    public abstract class OwnerDetail : BaseModel
    {
        public string OwnerCode { get; set; }
        public Address Address { get; set; }
        public string ContactPersonName { get; set; }
        public string ContactPersonTelephoneNumber { get; set; }
        public string ContactPersonCellphoneNumber { get; set; }
        public string ContactPersonEmailAddress { get; set; }
        public bool HasGivenConsentForCommunication { get; set; }
        public IList<MarketingGroup> MarketingPreferences { get; set; }
        public EntityType OwnerType
        {
            get
            {
                if (this.GetType() == typeof(Individual))
                    return EntityType.Individual;
                else if (this.GetType() == typeof(Corporation))
                    return EntityType.Corporation;
                else
                    throw new NotSupportedException("Unable to determine Owner Type");
            }
        }
    }
}


