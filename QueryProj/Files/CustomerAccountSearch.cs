using System.ComponentModel.DataAnnotations;
using System.Text;

namespace Yamaha.Business.Model.Accounts
{
    public class CustomerAccountSearch
    {
        [Required, MaxLength(15)]
        public string AccountCode { get; set; }
        [Required, MaxLength(50)]
        public string AccountName { get; set; }
        [Required, MaxLength(10)]
        public string BranchCode { get; set; }
        [Required, MaxLength(20)]
        public string ContactNumber { get; set; }
        public string Address
        {
            get
            {
                var builder = new StringBuilder();
                if (!string.IsNullOrWhiteSpace(SoldToAddress1))
                    builder.AppendLine(SoldToAddress1);
                if (!string.IsNullOrWhiteSpace(SoldToAddress2))
                    builder.AppendLine(SoldToAddress2);
                if (!string.IsNullOrWhiteSpace(SoldToAddress3))
                    builder.AppendLine(SoldToAddress3);
                if (!string.IsNullOrWhiteSpace(SoldToAddress3Location))
                    builder.AppendLine(SoldToAddress3Location);
                if (!string.IsNullOrWhiteSpace(SoldToAddress4))
                    builder.AppendLine(SoldToAddress4);
                if (!string.IsNullOrWhiteSpace(SoldToAddress5))
                    builder.AppendLine(SoldToAddress5);
                if (!string.IsNullOrWhiteSpace(SoldPostalCode))
                    builder.AppendLine(SoldPostalCode);

                return builder.ToString();
            }
        }
        [Required, MaxLength(40)]
        public string SoldToAddress1 { get; set; }
        [Required, MaxLength(40)]
        public string SoldToAddress2 { get; set; }
        [Required, MaxLength(40)]
        public string SoldToAddress3 { get; set; }
        [Required, MaxLength(40)]
        public string SoldToAddress3Location { get; set; }
        [Required, MaxLength(40)]
        public string SoldToAddress4 { get; set; }
        [Required, MaxLength(40)]
        public string SoldToAddress5 { get; set; }
        [Required, MaxLength(10)]
        public string SoldPostalCode { get; set; }
    }
}
