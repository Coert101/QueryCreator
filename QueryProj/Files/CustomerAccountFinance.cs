using System.ComponentModel.DataAnnotations;

namespace Yamaha.Business.Model.Accounts
{
    public class CustomerAccountFinance
    {
        [Required, MaxLength(15)]
        public string AccountCode { get; set; }
        [Required, MaxLength(10)]
        public string BranchCode { get; set; }
        [Required]
        public decimal CreditLimit { get; set; }
        [Required]
        public decimal CurrentBalance { get; set; }
        [Required]
        public decimal OutstandingBalance { get; set; }
        [Required]
        public bool OnHold { get; set; }
    }
}
