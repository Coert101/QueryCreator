using System.ComponentModel.DataAnnotations;

namespace Yamaha.Business.Model.Accounts
{
    public class CustomerSubaccount : CustomerAccountBase
    {
        [MaxLength(15)]
        public string CustomerMasterAccountCode { get; set; }
    }
}
