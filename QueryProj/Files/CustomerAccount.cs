using System.Collections.Generic;

namespace Yamaha.Business.Model.Accounts
{
    public class CustomerAccount : CustomerAccountBase
    {        
        public IList<CustomerSubaccount> Subaccounts { get; set; }
    }
}
