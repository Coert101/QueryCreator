using System.ComponentModel.DataAnnotations;
using System.Text;

namespace Yamaha.Business.Model.Accounts
{
    public class CustomerAccountBase
    {
        [Key, MaxLength(15)]
        public string AccountCode { get; set; }
        [Required, MaxLength(50)]
        public string AccountName { get; set; }
        public bool IsMasterAccount { get; set; }
        [Required, MaxLength(20)]
        public string ContactNumber { get; set; }
        [Required, MaxLength(20)]
        public string Salesperson { get; set; }
        [Required, MaxLength(10)]
        public string BranchCode { get; set; }
        public string Address
        {
            get
            {
                return SoldToAddress;
            }
        }
        public string SoldToAddress
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
        public string ShipToAddress
        {
            get
            {
                var builder = new StringBuilder();
                if (!string.IsNullOrWhiteSpace(ShipToAddress1))
                    builder.AppendLine(ShipToAddress1);
                if (!string.IsNullOrWhiteSpace(ShipToAddress2))
                    builder.AppendLine(ShipToAddress2);
                if (!string.IsNullOrWhiteSpace(ShipToAddress3))
                    builder.AppendLine(ShipToAddress3);
                if (!string.IsNullOrWhiteSpace(ShipToAddress3Location))
                    builder.AppendLine(ShipToAddress3Location);
                if (!string.IsNullOrWhiteSpace(ShipToAddress4))
                    builder.AppendLine(ShipToAddress4);
                if (!string.IsNullOrWhiteSpace(ShipToAddress5))
                    builder.AppendLine(ShipToAddress5);
                if (!string.IsNullOrWhiteSpace(ShipPostalCode))
                    builder.AppendLine(ShipPostalCode);

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
        [Required, MaxLength(40)]
        public string ShipToAddress1 { get; set; }
        [Required, MaxLength(40)]
        public string ShipToAddress2 { get; set; }
        [Required, MaxLength(40)]
        public string ShipToAddress3 { get; set; }
        [Required, MaxLength(40)]
        public string ShipToAddress3Location { get; set; }
        [Required, MaxLength(40)]
        public string ShipToAddress4 { get; set; }
        [Required, MaxLength(40)]
        public string ShipToAddress5 { get; set; }
        [Required, MaxLength(10)]
        public string ShipPostalCode { get; set; }
        [Required]
        public decimal CreditLimit { get; set; }
        [Required]
        public decimal CurrentBalance { get; set; }
        [Required]
        public decimal OutstandingBalance { get; set; }
        [Required]
        public decimal CreditAvailable
        {
            get
            {
                return CreditLimit - CurrentBalance - OutstandingBalance;
            }
        }
        public bool OnHold { get; set; }
    }
}
