using System.ComponentModel.DataAnnotations;

namespace Yamaha.Business.Model.Accounts
{
    public class Quote
    {
        [Key, MaxLength(20)]
        public string QuoteNumber { get; set; }
        [Required, MaxLength(15)]
        public string AccountCode { get; set; }
    }
}
